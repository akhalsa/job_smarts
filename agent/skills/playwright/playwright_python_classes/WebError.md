# WebError

Source: https://playwright.dev/python/docs/api/class-weberror

---

[WebError](Weberror.md) class represents an unhandled exception thrown in the page. It is dispatched via the [browser_context.on("weberror")](Browsercontext.md) event.

* Sync* Async

```
# Log all uncaught errors to the terminal  
context.on("weberror", lambda web_error: print(f"uncaught exception: {web_error.error}"))  
  
# Navigate to a page with an exception.  
page.goto("data:text/html,<script>throw new Error('test')</script>")
```

```
# Log all uncaught errors to the terminal  
context.on("weberror", lambda web_error: print(f"uncaught exception: {web_error.error}"))  
  
# Navigate to a page with an exception.  
await page.goto("data:text/html,<script>throw new Error('test')</script>")
```

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### error[​](#web-error-error "Direct link to error") webError.error

Unhandled error that was thrown.

**Usage**

```
web_error.error
```

**Returns**

* [Error](Error.md)

---

### page[​](#web-error-page "Direct link to page") webError.page

The page that produced this unhandled exception, if any.

**Usage**

```
web_error.page
```

**Returns**

* NoneType | [Page](Page.md)

* [Properties](#properties)
  + [error](#web-error-error)+ [page](#web-error-page)
