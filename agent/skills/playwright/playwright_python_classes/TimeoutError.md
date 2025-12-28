# TimeoutError

Source: https://playwright.dev/python/docs/api/class-timeouterror

---

* extends: [Error](Error.md)

TimeoutError is emitted whenever certain operations are terminated due to timeout, e.g. [locator.wait_for()](Locator.md) or [browser_type.launch()](Browsertype.md).

* Sync* Async

```
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError  
  
with sync_playwright() as p:  
    browser = p.chromium.launch()  
    page = browser.new_page()  
    try:  
      page.locator("text=Example").click(timeout=100)  
    except PlaywrightTimeoutError:  
      print("Timeout!")  
    browser.close()
```

```
import asyncio  
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError, Playwright  
  
async def run(playwright: Playwright):  
    browser = await playwright.chromium.launch()  
    page = await browser.new_page()  
    try:  
      await page.locator("text=Example").click(timeout=100)  
    except PlaywrightTimeoutError:  
      print("Timeout!")  
    await browser.close()  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
  
asyncio.run(main())
```
