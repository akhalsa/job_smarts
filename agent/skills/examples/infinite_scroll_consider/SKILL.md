---
name: infinite_scroll_usv
description: Reference retrieve_jobs implementation for extracting all jobs from an infinite scroll jobs dashboard (Based on the USV dashboard on 12/29/2025)
---

# Overview
Working reference implementation in `examples/infinite_scroll_usv/retrieve_jobs.py` for Union Square Ventures' job dashboard: https://jobs.usv.com/jobs (verified 12/29/2025).

This code uses a **two-level infinite scroll approach** with automatic scrolling for VC job boards that aggregate multiple portfolio companies.

**You cannot run this script directly** - copy it to the workspace folder and adapt it based on the decisions below.

**This Script Will Almost Work On Many Boards**
This script was derived from Union Square Ventures job board. However, this is a "Consider" job board which is a 3rd party solution provider for VC job boards. This code should pretty much work on all Consider based pages. 



---

# Core Decision Framework

Follow these decisions sequentially to build your scraper:

## Step 1: Load the page and read it
Identify if this page is powered by Consider. If so, use the reference code as close to directly as possible. If not, you can still use it liberally, but just as a starting point. 

## Decision 1: Is This Infinite Scroll?

**Test:** Scroll down the page or click around. Does new content load dynamically without changing the URL?

- **YES** → This skill applies. Proceed to Decision 2.
- **NO** → This is traditional pagination or a static list. Use different approach.

**Infinite scroll indicators:**
- Content appears as you scroll
- "Load More" / "Show More" buttons
- No page number links in footer

---

## Decision 2: What's the Load Mechanism?

**Test:** Open the site with browser DevTools, scroll to bottom and observe behavior.

### Option A: Auto-Scroll (like USV)
Content automatically loads when you reach the bottom. This is what the reference implementation uses.

**Implementation:**
```python
page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
page.wait_for_timeout(2000)
```

### Option B: Load More Button
A button must be clicked to load more content.

**Implementation:**
```python
load_more = page.query_selector("button:has-text('Load More')")  # Adjust selector
if load_more and load_more.is_visible():
    load_more.click()
    page.wait_for_timeout(2000)
else:
    break  # No more content
```

**Test by:** Scroll through the page manually and observe what triggers new content.

---

## Decision 3: Single-Level or Two-Level?

**Test:** Are all jobs loaded on one page, or do company groups link to separate pages?

### Single-Level (Simpler)
All jobs can be loaded and extracted from a single page view.

**When to use:**
- Clicking company names just filters the current page
- No indicators like "See 34 other jobs from X"
- **Bias toward this if possible** - test by scrolling through entire main page

**Implementation:** One infinite scroll loop on main page, extract all jobs directly.

### Two-Level (like USV reference)
Companies have dedicated URLs, each requiring separate infinite scroll.

**When to use:**
- Company groups link to dedicated URLs like `/jobs/company-name`
- Text like "83 matching jobs at Justworks" suggests incomplete preview
- Testing reveals main page doesn't show all company jobs

**Implementation:**
- **Level 1:** Scroll main page to discover all company URLs
- **Level 2:** Visit each company URL and scroll to extract their jobs

**How to identify company URLs:** Look for links in company group headers/cards. Test by clicking 2-3 companies.

---

## Decision 4: Extract Job Data

Required fields for each job:
- **Job URL** (unique identifier)
- **Job Title**
- **Company Name** (properly formatted)
- **Date Posted** Not required but good to have

### Step 1: Find Selectors with DevTools
Inspect job cards in browser DevTools. Look for:
- Container elements that wrap each job
- Title elements
- Link elements with href
- Company name elements

### Step 2: Test Extraction Script
**Before building full scraper**, verify selectors work:

```python
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("YOUR_URL")
    page.wait_for_timeout(2000)
    
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    
    jobs = soup.select("YOUR_JOB_SELECTOR")
    print(f"Found {len(jobs)} jobs\n")
    
    for job in jobs[:3]:
        # Test your selectors
        title = job.select_one("TITLE_SELECTOR").get_text(strip=True)
        url = job.select_one("a[href]").get("href")
        company_name = soup.select_one(".board-company-header h1").get_text(strip=True)
        print(f"{title} | {url} | {company_name}")
```

Test on 3+ examples to ensure selectors are robust.
Make sure to test that company name does not include any extra text or weird formatting. This is a common issue as the company name will be available in several places but some will have camel case, others will have hyphens etc. We need a version we can show to end users so be careful there. 

### Step 3: Company Name Formatting

**Critical:** Extract from page content, NOT from URL slugs.

❌ **Wrong:**
```python
# From URL: /jobs/company-name-llc
company = "company-name-llc"  # Has hyphens, bad formatting
```

✅ **Correct:**
```python
# From page: <h1>Careers at Company Name LLC</h1>
header = soup.select_one(".board-company-header h1")
if not header:
    raise ValueError("Selector failed")
company = header.get_text(strip=True).replace("Careers at ", "")
```

**IMPORTANT** You must extract the REAL company name, not marketing phrases.
For VC dashboards like USV, extract from the page header and normalize it, removing any surrounding text you might find (this will be common)

Required behavior:
- Select company header element (example: `.board-company-header h1`)
- Get text
- Strip wrapping phrases like:
  "Careers at "
  "Jobs at "
  "Join "
  "Work at "
  "Positions at "

If the selector fails, FAIL LOUDLY (raise / log error).
Never fallback to URL slug unless explicitly required.

**Why fail loudly?** You want to know immediately when selectors break, not get bad data silently.

---

# Universal Pattern: Stability Detection

**The Challenge:** How do you know when infinite scroll is complete?

**Don't use:** Fixed scroll counts or timeouts alone (unreliable).

**Do use:** Count distinct items until the count stabilizes.

## Algorithm

```python
seen_urls: Set[str] = set()
stable_checks = 5  # Stop after this many rounds with no new items
stable_rounds = 0
last_count = 0

for scroll_num in range(max_scrolls):
    # Extract jobs from current page
    jobs = extract_jobs(page)
    for job_url in jobs:
        seen_urls.add(job_url)
    
    current_count = len(seen_urls)
    
    if current_count == last_count:
        stable_rounds += 1
        if stable_rounds >= stable_checks:
            break  # Done!
    else:
        stable_rounds = 0
        last_count = current_count
    
    # Trigger load (scroll or button click)
    trigger_load_mechanism(page)
    page.wait_for_timeout(2000)
```

**This pattern works for:**
- Auto-scroll mechanisms
- Load More buttons
- Single-level or two-level architectures

---

# Testing Workflow

**Critical:** Test incrementally before writing the full scraper.

## Phase 1: Architecture Test
- Determine if single-level or two-level
- Identify load mechanism (scroll vs button)
- Find how to discover company URLs (if two-level)
- Write test jobs to verify every infinite scroll is working

## Phase 2: Selector Test
- Test job extraction selectors on 3+ examples
- Verify company name extraction (properly formatted)
- Confirm all required fields extract correctly

## Phase 3: End-to-End Test
Run a complete test on 2-3 companies:
- Test infinite scroll/button clicking
- Verify stability detection works
- Confirm no duplicates
- Check data quality

**Only after Phase 3 succeeds** → Write production script.

---

# Adaptation Checklist

1. ☐ **Decision 1:** Confirm this is infinite scroll
2. ☐ **Decision 2:** Identify load mechanism (scroll vs button)
3. ☐ **Decision 3:** Determine single-level vs two-level architecture
4. ☐ **Decision 4:** Test job data extraction selectors
5. ☐ **Verify company names** are properly formatted (not URL slugs)
6. ☐ **Run end-to-end test** on 2-3 companies
7. ☐ **Write production script** incorporating tested patterns

**Key principle:** Test each decision before moving to the next. Don't write the full script and hope it works.
