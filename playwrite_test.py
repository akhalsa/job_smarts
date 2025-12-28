from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://jobs.usv.com"
JOBS_URL = f"{BASE_URL}/jobs"


def fetch_rendered_html(url: str) -> str:
    """
    Use Playwright to load the page (with JS) and return the rendered HTML.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        browser.close()
    return html


def fetch_rendered_full_scroll(url: str, max_tries: int = 5, idle_loops: int = 3) -> str:
    """
    Use Playwright to scroll through an infinite-scroll page until no new content loads.
    Returns the final HTML for parsing with BeautifulSoup.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        last_height = 0
        unchanged_loops = 0

        for i in range(max_tries):
            # Scroll to bottom
            print(f"Scrolling to bottom - attempt {i}")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            # Give the page some time to fetch & render new results
            page.wait_for_timeout(5000)

            new_height = page.evaluate("document.body.scrollHeight")
            print(f"new height: {new_height}")
            if new_height == last_height:
                unchanged_loops += 1
            else:
                unchanged_loops = 0
                last_height = new_height

            if unchanged_loops >= idle_loops:
                # We've scrolled a few times with no growth -> probably done
                break

        html = page.content()
        browser.close()

    return html

def main():
    html = fetch_rendered_html(JOBS_URL)
    with open("usv_initial.html", "w", encoding="utf-8") as f:
        f.write(html)
        print(f"Saved initial HTML ({len(html)} chars) -> usv_initial.html")

    
    # Infinite scroll fully loaded page
    scrolled_html = fetch_rendered_full_scroll(JOBS_URL)
    with open("usv_full_scroll.html", "w", encoding="utf-8") as f:
        f.write(scrolled_html)
        print(f"Saved fully scrolled HTML ({len(scrolled_html)} chars) -> usv_full_scroll.html")
    


if __name__ == "__main__":
    main()
