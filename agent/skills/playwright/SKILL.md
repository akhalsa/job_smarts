---
name: playwright
description: A headless web browser with a python API. Use it to retrieve site content and interact with the DOM. 
---

# Playwright Web Automation

## Overview

Playwright is a headless browser automation library that allows you to programmatically control Chromium, Firefox, or WebKit browsers. Use it to navigate websites, interact with dynamic content, handle pagination, and extract rendered HTML.

**Key capabilities:**
- Navigate to URLs and wait for content to load
- Execute JavaScript and interact with the DOM
- Scroll pages and click elements
- Handle infinite scroll and pagination
- Extract fully-rendered HTML (including JavaScript-generated content)
- Wait for specific elements or network conditions

## Basic Usage Pattern

### 1. Launch Browser and Navigate

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser (headless by default)
    browser = p.chromium.launch(headless=True)
    
    # Create a new page
    page = browser.new_page()
    
    # Navigate to URL
    page.goto("https://example.com", wait_until="networkidle")
    
    # Get the rendered HTML
    html = page.content()
    
    # Close browser
    browser.close()
```

### 2. Wait Strategies

Playwright provides several wait strategies to ensure content is loaded:

```python
# Wait until network is idle (no connections for 500ms)
page.goto("https://example.com", wait_until="networkidle")

# Wait until DOM content is loaded
page.goto("https://example.com", wait_until="domcontentloaded")

# Wait until the load event fires
page.goto("https://example.com", wait_until="load")

# Wait for a specific element to appear
page.wait_for_selector(".job-card", timeout=30000)

# Wait for a specific timeout (use sparingly)
page.wait_for_timeout(2000)  # Wait 2 seconds
```

**Best Practice**: Use `wait_until="networkidle"` for initial page load, then use `wait_for_selector()` to wait for specific elements.

## Common Interactions

### Scrolling

Scrolling is essential for loading dynamic content and infinite scroll pages.

```python
# Scroll to bottom of page
page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

# Scroll by a specific amount
page.evaluate("window.scrollBy(0, 1000)")  # Scroll down 1000px

# Get current scroll height (useful for detecting when scrolling stops)
current_height = page.evaluate("document.body.scrollHeight")
```

### Clicking Elements

```python
# Click using CSS selector
page.click("button.load-more")

# Click with explicit wait
page.wait_for_selector("button.load-more")
page.click("button.load-more")

# Click with timeout
page.click("button.next-page", timeout=10000)
```

### Checking Element Visibility

```python
# Check if element exists and is visible
is_visible = page.is_visible("button.load-more")

# Check if element exists in DOM (even if hidden)
element = page.query_selector("button.load-more")
if element:
    print("Element found in DOM")
```

### Extracting Content

```python
# Get full page HTML
html = page.content()

# Get text content of specific element
text = page.inner_text(".job-title")

# Get attribute value
href = page.get_attribute("a.job-link", "href")

# Evaluate JavaScript to extract data
job_count = page.evaluate("document.querySelectorAll('.job-card').length")
```

## Pagination Patterns

### Pattern 1: Infinite Scroll

Many modern websites load content as you scroll. Here's a robust pattern:

```python
from playwright.sync_api import sync_playwright

def scroll_until_stable(page, max_scrolls=50, idle_checks=3):
    """
    Scroll to bottom repeatedly until page height stops changing.
    
    Args:
        page: Playwright page object
        max_scrolls: Maximum number of scroll attempts
        idle_checks: Number of consecutive unchanged heights to consider stable
    """
    last_height = 0
    unchanged_count = 0
    
    for i in range(max_scrolls):
        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # Wait for content to load
        page.wait_for_timeout(2000)
        
        # Check new height
        new_height = page.evaluate("document.body.scrollHeight")
        
        if new_height == last_height:
            unchanged_count += 1
            if unchanged_count >= idle_checks:
                print(f"Page stabilized after {i+1} scrolls")
                break
        else:
            unchanged_count = 0
            last_height = new_height
    
    return page.content()

# Usage
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://jobs.usv.com/jobs", wait_until="networkidle")
    
    html = scroll_until_stable(page)
    browser.close()
```

### Pattern 2: "Load More" Button

Some sites have a button to load additional content:

```python
from playwright.sync_api import sync_playwright

def click_load_more_until_done(page, button_selector, max_clicks=100):
    """
    Click 'Load More' button until it disappears or max clicks reached.
    
    Args:
        page: Playwright page object
        button_selector: CSS selector for the load more button
        max_clicks: Maximum number of clicks
    """
    clicks = 0
    
    while clicks < max_clicks:
        try:
            # Check if button exists and is visible
            if not page.is_visible(button_selector):
                print(f"Button no longer visible after {clicks} clicks")
                break
            
            # Click the button
            page.click(button_selector, timeout=5000)
            clicks += 1
            
            # Wait for new content to load
            page.wait_for_timeout(1500)
            
        except Exception as e:
            print(f"Button not found or clickable after {clicks} clicks: {e}")
            break
    
    return page.content()

# Usage
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com/jobs", wait_until="networkidle")
    
    html = click_load_more_until_done(page, "button.load-more")
    browser.close()
```

### Pattern 3: Page Numbers / Next Button

Traditional pagination with "Next" button or page numbers:

```python
from playwright.sync_api import sync_playwright

def scrape_all_pages(start_url, next_button_selector):
    """
    Navigate through paginated results using Next button.
    
    Args:
        start_url: Initial URL
        next_button_selector: CSS selector for the next page button
    
    Returns:
        List of HTML content from each page
    """
    pages_html = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(start_url, wait_until="networkidle")
        
        page_num = 1
        while True:
            print(f"Scraping page {page_num}")
            
            # Get current page HTML
            pages_html.append(page.content())
            
            # Check if next button exists and is enabled
            if not page.is_visible(next_button_selector):
                print("No more pages")
                break
            
            # Click next button
            page.click(next_button_selector)
            
            # Wait for navigation/content to load
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(1000)
            
            page_num += 1
        
        browser.close()
    
    return pages_html
```

## Advanced Techniques

### Detecting When Scrolling Has Loaded All Content

```python
def has_reached_end(page, selector=".job-card"):
    """
    Check if scrolling has loaded all content by comparing counts.
    """
    # Get initial count
    initial_count = page.evaluate(f"document.querySelectorAll('{selector}').length")
    
    # Scroll
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)
    
    # Get new count
    new_count = page.evaluate(f"document.querySelectorAll('{selector}').length")
    
    return new_count == initial_count
```

### Handling Lazy-Loaded Images

```python
# Wait for images to load
page.wait_for_load_state("networkidle")

# Or wait for specific image
page.wait_for_selector("img[src*='logo']")
```

### Taking Screenshots (Debugging)

```python
# Take screenshot of full page
page.screenshot(path="debug.png", full_page=True)

# Take screenshot of specific element
element = page.query_selector(".job-listing")
element.screenshot(path="element.png")
```

### Custom Viewport Size

```python
# Set custom viewport (useful for mobile testing)
browser = p.chromium.launch()
context = browser.new_context(
    viewport={"width": 1920, "height": 1080}
)
page = context.new_page()
```

## Best Practices

### 1. Always Use Context Managers or Explicit Cleanup

```python
# Good: Using context manager
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    # ... do work ...
    browser.close()

# Also good: Explicit cleanup
p = sync_playwright().start()
browser = p.chromium.launch()
try:
    page = browser.new_page()
    # ... do work ...
finally:
    browser.close()
    p.stop()
```

### 2. Use Appropriate Wait Strategies

```python
# Bad: Hard-coded sleeps
page.goto("https://example.com")
page.wait_for_timeout(5000)  # Arbitrary wait

# Good: Wait for specific conditions
page.goto("https://example.com", wait_until="networkidle")
page.wait_for_selector(".content-loaded")
```

### 3. Handle Errors Gracefully

```python
try:
    page.click("button.optional", timeout=3000)
except:
    print("Optional button not found, continuing...")

# Continue with scraping
```

### 4. Avoid Loading Unnecessary Resources (Optional Optimization)

```python
# Block images and stylesheets to speed up scraping
def block_resources(route):
    if route.request.resource_type in ["image", "stylesheet", "font"]:
        route.abort()
    else:
        route.continue_()

page.route("**/*", block_resources)
```

### 5. Use Headless Mode in Production

```python
# Headless mode (faster, no GUI)
browser = p.chromium.launch(headless=True)

# Headed mode (for debugging only)
browser = p.chromium.launch(headless=False)
```

## Common Selectors

```python
# CSS Selectors
page.query_selector(".job-card")           # Class
page.query_selector("#main-content")        # ID
page.query_selector("div.job-card")         # Element with class
page.query_selector("a[href*='apply']")     # Attribute contains

# XPath (alternative)
page.query_selector("xpath=//button[@class='next']")

# Text content
page.get_by_text("Next Page")
page.get_by_role("button", name="Submit")
```

## Complete Example: Job Board Scraper

```python
from playwright.sync_api import sync_playwright

def scrape_job_board(url):
    """
    Complete example: Scrape a job board with infinite scroll.
    """
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to job board
        print(f"Loading {url}")
        page.goto(url, wait_until="networkidle")
        
        # Wait for job listings to appear
        page.wait_for_selector(".job-card", timeout=10000)
        
        # Scroll to load all jobs
        print("Scrolling to load all jobs...")
        last_height = 0
        unchanged_count = 0
        scroll_count = 0
        
        while scroll_count < 50:
            # Scroll to bottom
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            
            # Wait for content
            page.wait_for_timeout(2000)
            
            # Check if height changed
            new_height = page.evaluate("document.body.scrollHeight")
            
            if new_height == last_height:
                unchanged_count += 1
                if unchanged_count >= 3:
                    print(f"Finished scrolling after {scroll_count} attempts")
                    break
            else:
                unchanged_count = 0
                last_height = new_height
                
            scroll_count += 1
        
        # Get final HTML with all jobs loaded
        html = page.content()
        
        # Get job count for verification
        job_count = page.evaluate("document.querySelectorAll('.job-card').length")
        print(f"Found {job_count} jobs")
        
        browser.close()
        
        return html

# Usage
html_content = scrape_job_board("https://jobs.usv.com/jobs")
```

## Troubleshooting

### Page Not Loading
- Increase timeout: `page.goto(url, timeout=60000)`
- Check wait_until strategy
- Verify URL is accessible

### Elements Not Found
- Use `page.screenshot()` to see what's actually rendered
- Check if element is in an iframe: `frame = page.frame("frame-name")`
- Wait longer: `page.wait_for_selector("selector", timeout=30000)`

### Scroll Not Working
- Some sites prevent programmatic scrolling
- Try: `page.evaluate("window.scrollBy(0, window.innerHeight)")`
- Or use mouse wheel: `page.mouse.wheel(0, 1000)`

### Memory Issues
- Close browser after each batch of URLs
- Don't keep too many pages in memory
- Consider processing HTML immediately rather than storing
