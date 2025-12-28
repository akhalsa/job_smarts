# Dialog

Source: https://playwright.dev/python/docs/api/class-dialog

---

[Dialog](Dialog.md) objects are dispatched by page via the [page.on("dialog")](Page.md) event.

An example of using `Dialog` class:

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def handle_dialog(dialog):  
    print(dialog.message)  
    dialog.dismiss()  
  
def run(playwright: Playwright):  
    chromium = playwright.chromium  
    browser = chromium.launch()  
    page = browser.new_page()  
    page.on("dialog", handle_dialog)  
    page.evaluate("alert('1')")  
    browser.close()  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def handle_dialog(dialog):  
    print(dialog.message)  
    await dialog.dismiss()  
  
async def run(playwright: Playwright):  
    chromium = playwright.chromium  
    browser = await chromium.launch()  
    page = await browser.new_page()  
    page.on("dialog", handle_dialog)  
    page.evaluate("alert('1')")  
    await browser.close()  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

note

Dialogs are dismissed automatically, unless there is a [page.on("dialog")](Page.md) listener. When listener is present, it **must** either [dialog.accept()](Dialog.md) or [dialog.dismiss()](Dialog.md) the dialog - otherwise the page will [freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop#never_blocking) waiting for the dialog, and actions like click will never finish.

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### accept[​](#dialog-accept "Direct link to accept")

Added before v1.9
dialog.accept

Returns when the dialog has been accepted.

**Usage**

```
dialog.accept()  
dialog.accept(**kwargs)
```

**Arguments**

* `prompt_text` str *(optional)*

  A text to enter in prompt. Does not cause any effects if the dialog's `type` is not prompt. Optional.

**Returns**

* NoneType

---

### dismiss[​](#dialog-dismiss "Direct link to dismiss")

Added before v1.9
dialog.dismiss

Returns when the dialog has been dismissed.

**Usage**

```
dialog.dismiss()
```

**Returns**

* NoneType

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### default_value[​](#dialog-default-value "Direct link to default_value")

Added before v1.9
dialog.default_value

If dialog is prompt, returns default prompt value. Otherwise, returns empty string.

**Usage**

```
dialog.default_value
```

**Returns**

* str

---

### message[​](#dialog-message "Direct link to message")

Added before v1.9
dialog.message

A message displayed in the dialog.

**Usage**

```
dialog.message
```

**Returns**

* str

---

### page[​](#dialog-page "Direct link to page") dialog.page

The page that initiated this dialog, if available.

**Usage**

```
dialog.page
```

**Returns**

* NoneType | [Page](Page.md)

---

### type[​](#dialog-type "Direct link to type")

Added before v1.9
dialog.type

Returns dialog's type, can be one of `alert`, `beforeunload`, `confirm` or `prompt`.

**Usage**

```
dialog.type
```

**Returns**

* str
