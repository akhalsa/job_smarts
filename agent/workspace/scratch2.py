from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

URL = "https://jobs.bvp.com/jobs"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2000)
        for _ in range(15):
            page.mouse.wheel(0, 4000)
            page.wait_for_timeout(1200)
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")

    external = []
    for a in soup.select("a[href]"):
        href = a.get("href")
        if href and href.startswith("http") and "jobs.bvp.com" not in href:
            txt = a.get_text(" ", strip=True)
            external.append((href, txt))

    print("external links", len(external))
    for href, txt in external[:30]:
        print("-", txt[:80], "=>", href)

    # For a few external links, print surrounding text to find company/title patterns
    # pick links that look like ATS job postings
    ats_idxs = []
    for i, (href, txt) in enumerate(external):
        if any(host in href for host in [
            "greenhouse.io", "lever.co", "ashbyhq.com", "comeet.com", "workday", "trakstar", "applytojob", "myworkdayjobs",
        ]):
            ats_idxs.append(i)
        if len(ats_idxs) >= 3:
            break

    for idx in ats_idxs:
        if idx >= len(external):
            continue
        href, txt = external[idx]
        a = soup.find("a", href=href)
        print("\n--- sample", idx, "---")
        print("anchor text:", txt)
        container = a.find_parent(["li", "div", "article"])
        if not container:
            container = a.parent
        print("container name:", container.name)
        print("container text:")
        print(container.get_text(" | ", strip=True)[:500])
        # show internal company links in container
        comps = container.select('a[href^="/jobs/"]')
        print("internal company links in container:", [c.get_text(" ", strip=True) for c in comps][:10])


if __name__ == "__main__":
    main()
