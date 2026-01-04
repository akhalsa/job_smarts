import re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

URL = "https://jobs.bvp.com/jobs"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2000)

        # Try to trigger any infinite scroll
        for _ in range(6):
            page.mouse.wheel(0, 2500)
            page.wait_for_timeout(1500)

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")

    # Print some candidate job links
    links = soup.select("a[href]")
    job_links = []
    for a in links:
        href = a.get("href")
        if not href:
            continue
        if "/jobs/" in href and not href.endswith("/jobs"):
            job_links.append(href)
    job_links = list(dict.fromkeys(job_links))

    print(f"Total links: {len(links)}")
    print(f"Candidate job links: {len(job_links)}")
    for href in job_links[:40]:
        print(href)

    # Look for job card containers
    for sel in ["[data-testid]", ".job", ".jobs", "li", "article", "div"]:
        nodes = soup.select(sel)
        print(sel, len(nodes))


if __name__ == "__main__":
    main()
