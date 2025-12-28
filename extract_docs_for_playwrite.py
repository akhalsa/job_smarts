#!/usr/bin/env python3
"""
Scrape Playwright Python class documentation into individual Markdown files
and bundle them into a ZIP archive.

- Starts at: https://playwright.dev/python/docs/api/class-playwright
- Finds all links whose href starts with /python/docs/api/class-
- For each class page:
    * Downloads HTML
    * Extracts the main content
    * Converts it to Markdown
    * Saves as <ClassName>.md in ./playwright_python_classes
- Finally creates playwright_python_classes.zip in the current directory.

Usage:
    python scrape_playwright_docs.py
"""

import os
import re
import time
import zipfile
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


from markdownify import markdownify as html_to_markdown



BASE_URL = "https://playwright.dev"
START_URL = "https://playwright.dev/python/docs/api/class-playwright"
OUTPUT_DIR = "playwright_python_classes"
ZIP_NAME = "playwright_python_classes.zip"


def fetch(url: str) -> str:
    """Fetch a URL and return its HTML as text."""
    print(f"GET {url}")
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


def get_class_urls(start_url: str) -> list[str]:
    """
    From the start page, discover all Python API class docs:
    any <a> whose href starts with '/python/docs/api/class-'.
    """
    html = fetch(start_url)
    soup = BeautifulSoup(html, "html.parser")

    links = set()
    for a in soup.find_all("a", href=True):
        href = str(a["href"])
        # Normalize relative URLs
        parsed = urlparse(href)
        # Only keep paths under /python/docs/api/class-*
        if parsed.scheme or parsed.netloc:
            # Absolute URL – keep only if it matches the path we care about
            path = parsed.path
        else:
            # Relative URL
            path = href

        if path.startswith("/python/docs/api/class-"):
            full = urljoin(BASE_URL, path)
            links.add(full)

    # Also include the start page itself to be safe
    links.add(start_url)

    urls = sorted(links)
    print(f"Discovered {len(urls)} class URLs.")
    return urls


def extract_main_content(html: str) -> tuple[str, str]:
    """
    Extract a (title, html_content) from a Playwright docs page.

    - Title: from the first <h1> on the page
    - Content: the <main> element if present, else <article>, else <body>.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Title
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else "Untitled"

    # Main content region
    main = soup.find("main")
    if main is None:
        main = soup.find("article")
    if main is None:
        main = soup.body or soup

    # Remove site-wide chrome bits like navigation / footer if they’re inside main
    # This is conservative; tweak if you want even cleaner output.
    for selector in ["header", "nav", "footer"]:
        for tag in main.find_all(selector):
            tag.decompose()

    # Convert that HTML subtree to string
    content_html = str(main)
    return title, content_html


def sanitize_filename(name: str) -> str:
    """
    Turn a class title into a safe filename, e.g. 'API Request' -> 'APIRequest.md'.
    """
    # Remove weird characters
    name = name.strip().replace("/", " ")
    # Collapse whitespace
    name = re.sub(r"\s+", " ", name)
    # Remove surrounding punctuation
    name = name.strip(" ._-")
    # Remove characters that are problematic on most filesystems
    name = re.sub(r"[^A-Za-z0-9 _.-]", "", name)
    # Remove spaces to keep it simple
    name = name.replace(" ", "")
    return f"{name or 'PlaywrightClass'}.md"


def save_markdown_for_url(url: str, out_dir: str) -> str:
    """
    Download a docs page, convert to markdown, and save it.

    Returns the path to the saved file.
    """
    html = fetch(url)
    title, main_html = extract_main_content(html)
    md_body = html_to_markdown(main_html)

    filename = sanitize_filename(title)
    out_path = os.path.join(out_dir, filename)

    # Add a simple Markdown header at the top
    md = f"# {title}\n\nSource: {url}\n\n---\n\n{md_body}"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Wrote {out_path}")
    return out_path


def ensure_output_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def zip_folder(folder: str, zip_name: str) -> None:
    """Zip all files in `folder` (non-recursive) into `zip_name`."""
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in os.listdir(folder):
            full = os.path.join(folder, fname)
            if os.path.isfile(full):
                zf.write(full, arcname=fname)
    print(f"Created {zip_name}")


def main():
    ensure_output_dir(OUTPUT_DIR)

    class_urls = get_class_urls(START_URL)

    for url in class_urls:
        try:
            save_markdown_for_url(url, OUTPUT_DIR)
            time.sleep(0.5)  # be polite, avoid hammering the server
        except Exception as e:
            print(f"!! Error processing {url}: {e}")

    zip_folder(OUTPUT_DIR, ZIP_NAME)
    print("Done.")


if __name__ == "__main__":
    main()
