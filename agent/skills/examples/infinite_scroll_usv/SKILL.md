---
name: infinite_scroll_usv
description: Reference retrieve_jobs implementation for extracting all jobs from an infinite scroll jobs dashboard (Based on the USV dashboard on 12/29/2025)
---

# Overview
Working reference implementation in `examples/infinite_scroll_usv/retrieve_jobs.py` for Union Square Ventures' job dashboard: https://jobs.usv.com/jobs (verified 12/29/2025).

This uses a **two-level infinite scroll approach** specific to VC job boards that aggregate multiple portfolio companies.

**You cannot run this script directly** - copy it to the workspace folder and adapt it.

---

# Decision Process: One-Level vs Two-Level Scroll

VC job boards always show multiple companies, but they differ in architecture:

## Step 1: Check if Companies Have Dedicated URLs

**Test by clicking a company group** - does it navigate to a dedicated URL like `/jobs/justworks`?

### Two-Level Pattern (like USV)
If companies have dedicated URLs:
- **Level 1:** Scroll main page to discover all company slugs/URLs
- **Level 2:** Visit each company URL and scroll to get all their jobs

**Key indicator:** Look for text that suggests the main list of jobs is incomplete - text like "See 34 other jobs from anthropic" next to just a few job postings from anthropic in the main list of jobs indicate you will need to use a two level pattern.

### One-Level Pattern
Bias towards a one level pattern if you can. You just want to first run experimental scripts that confirm all the results can be loaded into a single page. If thats the case then: 
- Use a single infinite scroll on the main page
- Extract all jobs directly as they load

## Step 2: Write Test Script to Verify

**Before implementing, test your hypothesis:**

```python
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("YOUR_VC_JOBS_URL")
    page.wait_for_timeout(2000)
    
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    
    # Find company groups and check their links
    groups = soup.select("CANDIDATE_SELECTOR")  # Inspect page to find this
    print(f"Found {len(groups)} groups")
    
    for group in groups[:3]:
        link = group.select_one("a[href]")
        if link:
            print(f"Link: {link.get('href')}")
            # Do links go to dedicated URLs or just #anchors/filters?
    
    browser.close()
```

**Critical: Test your selectors before writing the full script.** Don't guess and add fallback logic.

---

# Critical Pattern: Stability Detection

**The key challenge:** How do you know when infinite scroll is done?

## Don't Rely On:
- Fixed scroll counts (will miss items or waste time)
- Timeouts alone (unreliable with dynamic loading)

## Do This: Count Distinct Items Until Stable

```python
seen_items: Set[str] = set()
stable_checks = 5  # How many scrolls with no new items before stopping
stable_rounds = 0
last_count = 0

for scroll_num in range(max_scrolls):
    # Extract items from current page state
    current_items = extract_items(page)
    for item in current_items:
        seen_items.add(item)
    
    current_count = len(seen_items)
    
    # Stability check
    if current_count == last_count:
        stable_rounds += 1
        if stable_rounds >= stable_checks:
            print("Stable - scrolling complete!")
            break
    else:
        stable_rounds = 0  # Reset when we find new items
        last_count = current_count
    
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)
```

**Recommended parameters:**
- **Main page discovery:** `stable_checks=5`, `wait_for_timeout(2000)` (be conservative)
- **Company pages:** `stable_checks=4`, `wait_for_timeout(1500)` (can be faster)

---

# Testing Job Data Extraction

Before building the full scraper, verify you can extract **all required job information** correctly:

## Required Data Points:
- **Job URL** (unique identifier for deduplication)
- **Job Title** (e.g., "Senior Software Engineer")
- **Company Name** (properly formatted - see below)

## Company Name Formatting

**Critical:** Company names must be user-facing, not URL slugs.

❌ **Don't extract from URLs:**
```python
# URL: /jobs/company-name-llc
company_name = "company-name-llc"  # BAD - has hyphens, no proper capitalization
```

✅ **Extract from page content:**
```python
# From page: <h1>Careers at Company Name LLC</h1>
company_name = "Company Name LLC"  # GOOD - properly formatted
```

**Where to find company names:**
- Header elements (h1, h2) on company pages
- Breadcrumb navigation
- Company cards in the job list
- **Test extraction on 3+ companies** to verify consistency

## Job Parsing Test Script

Test that you can extract complete job data:

```python
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("COMPANY_OR_MAIN_PAGE_URL")
    page.wait_for_timeout(2000)
    
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    
    # Test job extraction
    job_containers = soup.select("YOUR_JOB_SELECTOR")
    print(f"Found {len(job_containers)} jobs\n")
    
    for job in job_containers[:5]:
        title_elem = job.select_one("YOUR_TITLE_SELECTOR")
        link_elem = job.select_one("a[href]")
        
        title = title_elem.get_text(strip=True) if title_elem else "MISSING"
        url = link_elem.get("href") if link_elem else "MISSING"
        
        print(f"Title: {title}")
        print(f"URL: {url}")
        print("---")
    
    # If two-level: also test company name extraction
    company_header = soup.select_one("YOUR_COMPANY_SELECTOR")
    if company_header:
        company_name = company_header.get_text(strip=True)
        print(f"\nCompany name: {company_name}")
        # Verify it's properly formatted, not a URL slug
    
    browser.close()
```

**Verify:**
- All fields extract correctly
- Company names are properly formatted (not URL slugs)
- URLs are valid and unique
- No missing data

---

# End-to-End Test Before Full Implementation

**Critical step:** Run a test that processes 2-3 companies completely, including infinite scroll.

This verifies your entire approach works before committing to the full scrape.

**What this test validates:**
- Infinite scroll stability detection works
- Job extraction selectors are correct
- Company name extraction works
- No duplicate jobs across companies
- Timing parameters (wait_for_timeout) are sufficient

**Only after this test succeeds** should you write the full production script.

---

# Selector Validation: Fail Loudly

When incorporating selectors into your final script, make them fail loudly:

❌ **Don't do this:**
```python
# Try strategy 1
# Try strategy 2
# Fallback to guessing
```

✅ **Do this:**
```python
# Tested selector
header = soup.select_one(".board-company-header h1")
if not header:
    raise ValueError(f"Selector failed for {company_slug}")
company_name = header.get_text(strip=True).replace("Careers at ", "")
```

**Why fail loudly?** You want to know immediately when your selector breaks, not get bad data silently.

---

# Adaptation Checklist for New VC Job Boards

1. **Test the architecture**
   - Do companies have dedicated URLs?
   - Click through 2-3 companies to verify
   
2. **Choose pattern**
   - Dedicated URLs → Two-level scroll (like USV reference)
   - No dedicated URLs → One-level scroll (simplify the script)
   
3. **Test job data extraction**
   - Write small test script to extract job data
   - Verify you can get job URLs, titles, and company names
   - **Critical:** Confirm company names are properly formatted (not URL slugs)
   
4. **Test selectors on multiple examples**
   - Verify selectors work on 3+ companies
   - Make selectors fail loudly (raise errors) - no fallback logic
   
5. **Run end-to-end test on 2-3 companies**
   - Test complete infinite scroll behavior (one-level or two-level)
   - Verify stability detection works
   - Confirm all data extracts correctly
   - Check for duplicates
   - **Only proceed after this test succeeds**
   
6. **Write final production script**
   - Incorporate tested selectors and patterns
   - Add progress logging
   - Run full scrape

**Key principle:** Test and verify at each step. Don't write the full script and hope it works.
