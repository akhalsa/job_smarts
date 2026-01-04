"""Extract all jobs from BVP's job board.

Board: https://jobs.bvp.com/jobs

This board is an infinite-scroll aggregator. Each job card contains:
- Job title (often an <a> to the external ATS, sometimes an "Apply" link)
- Metadata (location, posted date, etc.)
- An external ATS job URL (Greenhouse/Lever/Comeet/etc.)

The rendered DOM we see does *not* reliably include the company name on the main
aggregator page (at least as of this run). To ensure high-quality company_name,
we use a two-step approach:

1) Infinite-scroll the main page to collect all unique external job URLs.
2) For each external job URL, open it in Playwright and extract company name and
   job title from the destination page's metadata (OpenGraph / title tags).

We then persist each job incrementally via store_job().
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

from agent.skills.jobs_database.jobs_database_functions import store_job

START_URL = "https://jobs.bvp.com/jobs"

ATS_HOST_HINTS = [
    "greenhouse.io",
    "lever.co",
    "ashbyhq.com",
    "comeet.com",
    "workday",
    "myworkdayjobs",
    "trakstar",
    "applytojob",
    "icims.com",
]


def _abs_url(href: str) -> str:
    if not href:
        return ""
    if href.startswith("http://") or href.startswith("https://"):
        return href
    return urljoin(START_URL, href)


def _is_external_job_url(url: str) -> bool:
    if not url:
        return False
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    if re.search(r"https?://jobs\.bvp\.com/", url):
        return False
    host = urlparse(url).netloc.lower()
    return any(h in host for h in ATS_HOST_HINTS)


def _collect_job_urls(page, max_rounds: int = 60) -> list[str]:
    stable_rounds = 0
    last_count = 0
    seen: set[str] = set()

    for i in range(max_rounds):
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.select("a[href]"):
            url = _abs_url(a.get("href"))
            if _is_external_job_url(url):
                seen.add(url)

        count = len(seen)
        print(f"[scroll] round={i+1} unique_job_urls={count}")
        if count == last_count:
            stable_rounds += 1
        else:
            stable_rounds = 0
            last_count = count

        if stable_rounds >= 5:
            break

        page.mouse.wheel(0, 5000)
        page.wait_for_timeout(1500)

    return sorted(seen)


def _meta_content(soup: BeautifulSoup, selector: str) -> str:
    tag = soup.select_one(selector)
    if not tag:
        return ""
    return (tag.get("content") or "").strip()


def _extract_company_and_title_from_external(html: str, url: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")

    # Try OpenGraph first
    og_site = _meta_content(soup, 'meta[property="og:site_name"]')
    og_title = _meta_content(soup, 'meta[property="og:title"]')

    company = og_site
    title = og_title

    if not title:
        t = soup.title.get_text(" ", strip=True) if soup.title else ""
        title = t

    # Clean common patterns in og:title/title
    # e.g. "Company - Job Title" or "Job Title - Company" or "Job Title | Company"
    if title and not company:
        parts = re.split(r"\s[-|•|–|—]\s", title)
        if len(parts) >= 2:
            # Heuristic: company tends to be shortest / last
            company = parts[-1].strip()
            title = parts[0].strip()

    # Normalize
    company = (company or "").strip()
    title = (title or "").strip()

    # If og:site_name is something generic like "Greenhouse" keep parsing
    if company.lower() in {"greenhouse", "lever", "comeet", "workday"}:
        company = ""

    # Greenhouse pages often contain company name in header/logo alt
    if not company and "greenhouse" in url:
        img = soup.select_one("img[alt]")
        if img:
            alt = (img.get("alt") or "").strip()
            if alt and alt.lower() not in {"greenhouse"}:
                company = alt

    return company, title


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(START_URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2500)

        job_urls = _collect_job_urls(page)
        print(f"Discovered external job URLs: {len(job_urls)}")

        saved = 0
        for idx, job_url in enumerate(job_urls, start=1):
            try:
                print(f"[{idx}/{len(job_urls)}] visiting {job_url}")
                page.goto(job_url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(1500)
                html = page.content()
                company, title = _extract_company_and_title_from_external(html, job_url)

                if not title:
                    print(f"  - skip (no title)")
                    continue
                if not company:
                    # Still store, but company unknown is low quality; we skip to match requirements.
                    print(f"  - skip (no company identified)")
                    continue

                res = store_job(job_url=job_url, company_name=company, job_title=title, date_posted=None)
                print(res)
                if res.startswith("✓"):
                    saved += 1
            except Exception as e:
                print(f"  - error: {e}")

        browser.close()

    print(f"Saved this run: {saved}")


if __name__ == "__main__":
    main()
