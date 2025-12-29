from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from agent.skills.jobs_database.jobs_database_functions import store_job

BASE = "https://jobs.usv.com"
START_URL = f"{BASE}/jobs"


def extract_company_pages(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for a in soup.select('a[href^="/jobs/"]'):
        href = a.get("href")
        if not href or href == "/jobs/":
            continue
        urls.append(urljoin(BASE, href))

    # de-dupe
    seen = set()
    out = []
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        out.append(u)
    return out


def extract_jobs_from_company_page(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    # Company name appears in header; fall back to title
    company_name = None
    h1 = soup.select_one("h1")
    if h1:
        company_name = h1.get_text(" ", strip=True)
    if company_name:
        # Often "All jobs at X" or "X"
        company_name = re.sub(r"^All jobs at\s+", "", company_name, flags=re.I).strip()

    jobs = []

    # Actual job postings are outbound links (greenhouse, lever, ashby, etc.)
    for a in soup.select("a[href]"):
        href = a.get("href")
        if not href:
            continue
        if href.startswith("/"):
            continue

        # Skip internal navigation links
        if href.startswith(BASE):
            continue

        text = a.get_text(" ", strip=True)
        if not text or text.lower() == "apply":
            continue

        # Basic heuristic: job links tend to have /jobs/ or gh_jid, etc.
        if not (
            "greenhouse" in href
            or "lever.co" in href
            or "ashbyhq" in href
            or "/jobs/" in href
            or "gh_jid" in href
        ):
            continue

        jobs.append(
            {
                "job_url": href,
                "job_title": text,
                "company_name": company_name,
            }
        )

    # de-dupe by url
    seen = set()
    out = []
    for j in jobs:
        if j["job_url"] in seen:
            continue
        seen.add(j["job_url"])
        out.append(j)

    return out


def main() -> None:
    jobs_saved = 0
    seen_job_urls: set[str] = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Loading start page: {START_URL}")
        page.goto(START_URL, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(1500)

        company_pages = extract_company_pages(page.content())
        print(f"Found {len(company_pages)} company pages")

        for idx, company_url in enumerate(company_pages, start=1):
            print(f"\n[{idx}/{len(company_pages)}] Loading company page: {company_url}")
            page.goto(company_url, wait_until="networkidle", timeout=60000)
            page.wait_for_timeout(1500)

            jobs = extract_jobs_from_company_page(page.content())
            print(f"Found {len(jobs)} outbound job links on page")

            for j in jobs:
                job_url = j.get("job_url")
                company_name = j.get("company_name") or "Unknown"
                job_title = j.get("job_title") or "Unknown"

                if not job_url or job_url in seen_job_urls:
                    continue
                seen_job_urls.add(job_url)

                try:
                    result = store_job(
                        job_url=job_url,
                        company_name=company_name,
                        job_title=job_title,
                    )
                    print(result)
                    if result.startswith("✓"):
                        jobs_saved += 1
                except Exception as e:
                    print(f"✗ Error saving job {job_title} at {company_name}: {e}")

        browser.close()

    print(f"\nDone. Saved {jobs_saved} jobs (unique URLs: {len(seen_job_urls)}).")


if __name__ == "__main__":
    main()
