from __future__ import annotations

from urllib.parse import urljoin

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from agent.skills.jobs_database.jobs_database_functions import store_job


BASE_URL = "https://jobs.usv.com/jobs"
ROOT = "https://jobs.usv.com"


def extract_and_store_jobs_from_html(html: str, seen_urls: set[str]) -> int:
    soup = BeautifulSoup(html, "html.parser")

    saved = 0
    # Each company group contains multiple job links (mostly Greenhouse).
    for group in soup.select("div.grouped-job-result"):
        # company name is in header link to /jobs/{company_slug}
        company = None
        header_a = group.select_one(".grouped-job-result-header a[href^='/jobs/']")
        if header_a:
            company = header_a.get_text(" ", strip=True)
        if not company:
            # fallback: sometimes text may be elsewhere
            header = group.select_one(".grouped-job-result-header")
            company = header.get_text(" ", strip=True) if header else None

        # job links are absolute greenhouse links
        for a in group.select("a[href]"):
            href = a.get("href")
            if not href:
                continue

            # Only keep actual job posting links; USV board often points to Greenhouse.
            if "greenhouse.io" not in href:
                continue

            title = a.get_text(" ", strip=True)
            if not title or title.lower() == "apply":
                continue

            job_url = href.strip()
            if job_url in seen_urls:
                continue
            seen_urls.add(job_url)

            if not company:
                # As a last resort, try to infer from URL path: boards.greenhouse.io/{company}
                try:
                    company = job_url.split("boards.greenhouse.io/")[1].split("/")[0]
                except Exception:
                    company = "Unknown"

            res = store_job(job_url=job_url, company_name=company, job_title=title)
            print(res)
            if res.startswith("✓"):
                saved += 1

    return saved


def scrape_usv_jobs() -> None:
    seen_urls: set[str] = set()
    total_saved = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Loading {BASE_URL} ...")
        page.goto(BASE_URL, wait_until="networkidle")
        page.wait_for_timeout(1500)

        # The site uses infinite scroll; scroll until height stabilizes.
        last_height = 0
        stable = 0

        max_scrolls = 80
        stable_checks = 4

        for i in range(max_scrolls):
            html = page.content()
            added = extract_and_store_jobs_from_html(html, seen_urls)
            total_saved += added
            print(f"Scroll {i+1}/{max_scrolls}: seen={len(seen_urls)} saved_total={total_saved} added_this_round={added}")

            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(2000)

            new_height = page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                stable += 1
                if stable >= stable_checks:
                    print("Page height stable; ending scroll.")
                    break
            else:
                stable = 0
                last_height = new_height

        browser.close()

    print(f"Done. Total unique job URLs seen: {len(seen_urls)}. Total saved: {total_saved}.")


if __name__ == "__main__":
    scrape_usv_jobs()
