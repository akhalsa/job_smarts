from __future__ import annotations

from typing import List, Set, Tuple
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, Page

from agent.skills.jobs_database.jobs_database_functions import store_job


BASE_URL = "https://jobs.usv.com/jobs"
ROOT = "https://jobs.usv.com"


# ---------------------------------------------------------------------------
# Company discovery (infinite scroll on main board)
# ---------------------------------------------------------------------------

def discover_all_companies(page: Page) -> List[str]:
    """
    Infinite scroll on main /jobs page to discover all company slugs.

    Returns:
        List of company slugs (e.g., ['kickstarter', 'remora', ...])
    """
    print(f"Discovering companies on {BASE_URL}...")
    print("(Using infinite scroll to load all company groups)\n")

    page.goto(BASE_URL, wait_until="networkidle")
    page.wait_for_timeout(1500)

    company_slugs: Set[str] = set()
    max_scrolls = 200          # generous upper bound
    stable_checks = 5          # how many rounds with no new companies before stopping
    stable_rounds = 0
    last_count = 0

    for i in range(max_scrolls):
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        # This selector is based on your original script and should work for the main board
        for group in soup.select("div.grouped-job-result"):
            header_a = group.select_one(".grouped-job-result-header a[href^='/jobs/']")
            if not header_a:
                continue
            href = header_a.get("href")
            if not href or not isinstance(href, str):
                continue

            slug = href.replace("/jobs/", "").strip().strip("/")
            if slug:
                company_slugs.add(slug)

        current_count = len(company_slugs)
        print(f"  Scroll {i+1}/{max_scrolls}: Found {current_count} companies so far...")

        if current_count == last_count:
            stable_rounds += 1
            if stable_rounds >= stable_checks:
                print("  No new companies discovered after several scrolls. Discovery complete!\n")
                break
        else:
            stable_rounds = 0
            last_count = current_count

        # Scroll down
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000)

    company_list = sorted(company_slugs)
    print(f"✓ Discovered {len(company_list)} companies total\n")
    return company_list


# ---------------------------------------------------------------------------
# Company name extraction
# ---------------------------------------------------------------------------

def extract_company_name(page: Page, company_slug: str) -> str:
    """
    Extract the properly formatted company name from a company page.

    Args:
        page: Current page (already navigated to company page)
        company_slug: Company slug for fallback

    Returns:
        Properly formatted company name
    """
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    # Extract company name from tested selector
    header = soup.select_one(".board-company-header h1")
    if not header:
        raise ValueError(f"Could not find company header for {company_slug}")

    company_name = header.get_text(strip=True).replace("Careers at ", "")
    return company_name



# ---------------------------------------------------------------------------
# Job extraction for a single company (second-level infinite scroll)
# ---------------------------------------------------------------------------

def _extract_jobs_from_html(html: str) -> List[Tuple[str, str]]:
    """
    Extract (job_title, job_url) pairs from a single HTML snapshot.

    This is intentionally robust & heuristic-based, since we don't want to rely
    on one brittle selector.
    """
    soup = BeautifulSoup(html, "html.parser")
    jobs: List[Tuple[str, str]] = []

    # First, try some likely job container patterns
    job_containers = soup.select(
        ".job-list-job"
    )
    print(f"Found {len(job_containers)} job containers")
    for jc in job_containers:
        # Sometimes the container itself is a link; otherwise, find first <a>
        a = jc if jc.name == "a" else jc.find("a", href=True)
        if not a:
            continue

        href = a.get("href")
        if not href or not isinstance(href, str):
            continue

        title = a.get_text(" ", strip=True)
        if not title:
            continue

        lower_title = title.lower()

        # Skip obvious non-job links
        if any(
            bad in lower_title
            for bad in [
                "view all",
                "show more",
                "view more",
                "learn more",
                "share these results",
                "back to",
            ]
        ):
            continue

        # Normalize relative URLs
        job_url = urljoin(ROOT, href.strip())

        # Skip hash-only or javascript links
        if job_url.endswith("#") or job_url.startswith("javascript:"):
            continue

        jobs.append((title, job_url))

    return jobs


def scrape_company_jobs(page: Page, company_slug: str, seen_urls: Set[str]) -> Tuple[str, int]:
    """
    Scrape all jobs for a single company using infinite scroll on their page.

    Args:
        page: Playwright page object
        company_slug: Company slug (e.g., 'kickstarter')
        seen_urls: Global set of seen job URLs

    Returns:
        Tuple of (company_name, jobs_saved_count)
    """
    company_url = urljoin(ROOT, f"/jobs/{company_slug}")

    print(f"→ Scraping {company_slug}...")
    page.goto(company_url, wait_until="networkidle", timeout=15000)
    page.wait_for_timeout(1000)

    company_name = extract_company_name(page, company_slug)

    jobs_saved = 0
    max_scrolls = 80
    stable_checks = 4
    stable_rounds = 0
    last_jobs_seen = 0  # per company

    for scroll_num in range(max_scrolls):
        html = page.content()
        candidate_jobs = _extract_jobs_from_html(html)

        newly_seen = 0
        for title, job_url in candidate_jobs:
            if job_url in seen_urls:
                continue
            seen_urls.add(job_url)

            # Persist via your existing function
            result = store_job(
                job_url=job_url,
                company_name=company_name,
                job_title=title,
            )
            if isinstance(result, str) and result.startswith("✓"):
                jobs_saved += 1
            newly_seen += 1

        total_jobs_seen = last_jobs_seen + newly_seen

        # Stopping condition: if we've seen no new jobs for several scrolls
        if total_jobs_seen == last_jobs_seen:
            stable_rounds += 1
            if stable_rounds >= stable_checks:
                break
        else:
            stable_rounds = 0
            last_jobs_seen = total_jobs_seen

        # Scroll down for more jobs
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1500)

    print(f"  ✓ {company_name}: Saved {jobs_saved} jobs\n")
    return company_name, jobs_saved


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def scrape_usv_jobs() -> None:
    """
    Main scraper using two-level infinite scroll approach.

    Level 1: Infinite scroll on main page to discover all companies
    Level 2: For each company, infinite scroll on their page to get all jobs
    """
    print("=" * 70)
    print("USV JOBS SCRAPER - Two-Level Infinite Scroll")
    print("=" * 70)
    print()

    seen_urls: Set[str] = set()
    total_jobs_saved = 0
    companies_processed: List[Tuple[str, int]] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # LOOP 1: Discover all companies via infinite scroll
            company_slugs = discover_all_companies(page)

            # LOOP 2: For each company, scrape all their jobs via infinite scroll
            print(f"Starting job extraction from {len(company_slugs)} companies...")
            print("=" * 70)
            print()

            for idx, slug in enumerate(company_slugs, 1):
                print(f"[{idx}/{len(company_slugs)}] ", end="")
                try:
                    company_name, jobs_count = scrape_company_jobs(page, slug, seen_urls)
                    total_jobs_saved += jobs_count
                    companies_processed.append((company_name, jobs_count))
                except Exception as e:
                    print(f"  ✗ Error scraping {slug}: {e}\n")
                    continue

        finally:
            browser.close()

    # Final report
    print()
    print("=" * 70)
    print("SCRAPING COMPLETE!")
    print("=" * 70)
    print(f"Companies processed: {len(companies_processed)}")
    print(f"Total jobs saved: {total_jobs_saved}")
    print(f"Unique job URLs: {len(seen_urls)}")
    print("=" * 70)

    # Show top companies by job count
    if companies_processed:
        print("\nTop 10 companies by job count:")
        top_companies = sorted(companies_processed, key=lambda x: x[1], reverse=True)[:10]
        for company, count in top_companies:
            print(f"  • {company}: {count} jobs")
    print()


if __name__ == "__main__":
    scrape_usv_jobs()
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=True)  # turn off headless for debugging
    #     page = browser.new_page()
    #     slugs = ["abridge", "justworks", "upgrade"]  # or any 2–3 you know exist

    #     seen_urls: Set[str] = set()
    #     for slug in slugs:
    #         scrape_company_jobs(page, slug, seen_urls)
