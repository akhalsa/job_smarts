# Playwright

Source: https://playwright.dev/python/docs/api/class-playwright

---

Playwright module provides a method to launch a browser instance. The following is a typical example of using Playwright to drive automation:

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
    chromium = playwright.chromium # or "firefox" or "webkit".  
    browser = chromium.launch()  
    page = browser.new_page()  
    page.goto("http://example.com")  
    # other actions...  
    browser.close()  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def run(playwright: Playwright):  
    chromium = playwright.chromium # or "firefox" or "webkit".  
    browser = await chromium.launch()  
    page = await browser.new_page()  
    await page.goto("http://example.com")  
    # other actions...  
    await browser.close()  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### stop[​](#playwright-stop "Direct link to stop")

Added before v1.9
playwright.stop

Terminates this instance of Playwright in case it was created bypassing the Python context manager. This is useful in REPL applications.

```
from playwright.sync_api import sync_playwright  
  
playwright = sync_playwright().start()  
  
browser = playwright.chromium.launch()  
page = browser.new_page()  
page.goto("https://playwright.dev/")  
page.screenshot(path="example.png")  
browser.close()  
  
playwright.stop()
```

**Usage**

```
playwright.stop()
```

**Returns**

* NoneType

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### chromium[​](#playwright-chromium "Direct link to chromium")

Added before v1.9
playwright.chromium

This object can be used to launch or connect to Chromium, returning instances of [Browser](Browser.md).

**Usage**

```
playwright.chromium
```

**Type**

* [BrowserType](Browsertype.md)

---

### devices[​](#playwright-devices "Direct link to devices")

Added before v1.9
playwright.devices

Returns a dictionary of devices to be used with [browser.new_context()](Browser.md) or [browser.new_page()](Browser.md).

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
    webkit = playwright.webkit  
    iphone = playwright.devices["iPhone 6"]  
    browser = webkit.launch()  
    context = browser.new_context(**iphone)  
    page = context.new_page()  
    page.goto("http://example.com")  
    # other actions...  
    browser.close()  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def run(playwright: Playwright):  
    webkit = playwright.webkit  
    iphone = playwright.devices["iPhone 6"]  
    browser = await webkit.launch()  
    context = await browser.new_context(**iphone)  
    page = await context.new_page()  
    await page.goto("http://example.com")  
    # other actions...  
    await browser.close()  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

**Usage**

```
playwright.devices
```

**Type**

* Dict

---

### firefox[​](#playwright-firefox "Direct link to firefox")

Added before v1.9
playwright.firefox

This object can be used to launch or connect to Firefox, returning instances of [Browser](Browser.md).

**Usage**

```
playwright.firefox
```

**Type**

* [BrowserType](Browsertype.md)

---

### request[​](#playwright-request "Direct link to request") playwright.request

Exposes API that can be used for the Web API testing.

**Usage**

```
playwright.request
```

**Type**

* [APIRequest](Apirequest.md)

---

### selectors[​](#playwright-selectors "Direct link to selectors")

Added before v1.9
playwright.selectors

Selectors can be used to install custom selector engines. See [extensibility](/python/docs/extensibility) for more information.

**Usage**

```
playwright.selectors
```

**Type**

* [Selectors](Selectors.md)

---

### webkit[​](#playwright-webkit "Direct link to webkit")

Added before v1.9
playwright.webkit

This object can be used to launch or connect to WebKit, returning instances of [Browser](Browser.md).

**Usage**

```
playwright.webkit
```

**Type**

* [BrowserType](Browsertype.md)
