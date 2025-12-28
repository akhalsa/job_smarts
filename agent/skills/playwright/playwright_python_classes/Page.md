# Page

Source: https://playwright.dev/python/docs/api/class-page

---

Page provides methods to interact with a single tab in a [Browser](Browser.md), or an [extension background page](https://developer.chrome.com/extensions/background_pages) in Chromium. One [Browser](Browser.md) instance might have multiple [Page](Page.md) instances.

This example creates a page, navigates it to a URL, and then saves a screenshot:

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = webkit.launch()  
    context = browser.new_context()  
    page = context.new_page()  
    page.goto("https://example.com")  
    page.screenshot(path="screenshot.png")  
    browser.close()  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = await webkit.launch()  
    context = await browser.new_context()  
    page = await context.new_page()  
    await page.goto("https://example.com")  
    await page.screenshot(path="screenshot.png")  
    await browser.close()  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

The Page class emits various events (described below) which can be handled using any of Node's native [`EventEmitter`](https://nodejs.org/api/events.html#events_class_eventemitter) methods, such as `on`, `once` or `removeListener`.

This example logs a message for a single page `load` event:

```
page.once("load", lambda: print("page loaded!"))
```

To unsubscribe from events use the `removeListener` method:

```
def log_request(intercepted_request):  
    print("a request was made:", intercepted_request.url)  
page.on("request", log_request)  
# sometime later...  
page.remove_listener("request", log_request)
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### add_init_script[​](#page-add-init-script "Direct link to add_init_script")

Added before v1.9
page.add_init_script

Adds a script which would be evaluated in one of the following scenarios:

* Whenever the page is navigated.
* Whenever the child frame is attached or navigated. In this case, the script is evaluated in the context of the newly attached frame.

The script is evaluated after the document was created but before any of its scripts were run. This is useful to amend the JavaScript environment, e.g. to seed `Math.random`.

**Usage**

An example of overriding `Math.random` before the page loads:

```
// preload.js  
Math.random = () => 42;
```

* Sync* Async

```
# in your playwright script, assuming the preload.js file is in same directory  
page.add_init_script(path="./preload.js")
```

```
# in your playwright script, assuming the preload.js file is in same directory  
await page.add_init_script(path="./preload.js")
```

note

The order of evaluation of multiple scripts installed via [browser_context.add_init_script()](Browsercontext.md) and [page.add_init_script()](Page.md) is not defined.

**Arguments**

* `path` Union[str, pathlib.Path] *(optional)*

  Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working directory. Optional.
* `script` str *(optional)*

  Script to be evaluated in all pages in the browser context. Optional.

**Returns**

* NoneType

---

### add_locator_handler[​](#page-add-locator-handler "Direct link to add_locator_handler") page.add_locator_handler

When testing a web page, sometimes unexpected overlays like a "Sign up" dialog appear and block actions you want to automate, e.g. clicking a button. These overlays don't always show up in the same way or at the same time, making them tricky to handle in automated tests.

This method lets you set up a special function, called a handler, that activates when it detects that overlay is visible. The handler's job is to remove the overlay, allowing your test to continue as if the overlay wasn't there.

Things to keep in mind:

* When an overlay is shown predictably, we recommend explicitly waiting for it in your test and dismissing it as a part of your normal test flow, instead of using [page.add_locator_handler()](Page.md).
* Playwright checks for the overlay every time before executing or retrying an action that requires an [actionability check](/python/docs/actionability), or before performing an auto-waiting assertion check. When overlay is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't perform any actions, the handler will not be triggered.
* After executing the handler, Playwright will ensure that overlay that triggered the handler is not visible anymore. You can opt-out of this behavior with [no_wait_after](Page.md).
* The execution time of the handler counts towards the timeout of the action/assertion that executed the handler. If your handler takes too long, it might cause timeouts.
* You can register multiple handlers. However, only a single handler will be running at a time. Make sure the actions within a handler don't depend on another handler.

warning

Running the handler will alter your page state mid-test. For example it will change the currently focused element and move the mouse. Make sure that actions that run after the handler are self-contained and do not rely on the focus and mouse state being unchanged.

For example, consider a test that calls [locator.focus()](Locator.md) followed by [keyboard.press()](Keyboard.md). If your handler clicks a button between these two actions, the focused element most likely will be wrong, and key press will happen on the unexpected element. Use [locator.press()](Locator.md) instead to avoid this problem.

Another example is a series of mouse actions, where [mouse.move()](Mouse.md) is followed by [mouse.down()](Mouse.md). Again, when the handler runs between these two actions, the mouse position will be wrong during the mouse down. Prefer self-contained actions like [locator.click()](Locator.md) that do not rely on the state being unchanged by a handler.

**Usage**

An example that closes a "Sign up to the newsletter" dialog when it appears:

* Sync* Async

```
# Setup the handler.  
def handler():  
  page.get_by_role("button", name="No thanks").click()  
page.add_locator_handler(page.get_by_text("Sign up to the newsletter"), handler)  
  
# Write the test as usual.  
page.goto("https://example.com")  
page.get_by_role("button", name="Start here").click()
```

```
# Setup the handler.  
async def handler():  
  await page.get_by_role("button", name="No thanks").click()  
await page.add_locator_handler(page.get_by_text("Sign up to the newsletter"), handler)  
  
# Write the test as usual.  
await page.goto("https://example.com")  
await page.get_by_role("button", name="Start here").click()
```

An example that skips the "Confirm your security details" page when it is shown:

* Sync* Async

```
# Setup the handler.  
def handler():  
  page.get_by_role("button", name="Remind me later").click()  
page.add_locator_handler(page.get_by_text("Confirm your security details"), handler)  
  
# Write the test as usual.  
page.goto("https://example.com")  
page.get_by_role("button", name="Start here").click()
```

```
# Setup the handler.  
async def handler():  
  await page.get_by_role("button", name="Remind me later").click()  
await page.add_locator_handler(page.get_by_text("Confirm your security details"), handler)  
  
# Write the test as usual.  
await page.goto("https://example.com")  
await page.get_by_role("button", name="Start here").click()
```

An example with a custom callback on every actionability check. It uses a `<body>` locator that is always visible, so the handler is called before every actionability check. It is important to specify [no_wait_after](Page.md), because the handler does not hide the `<body>` element.

* Sync* Async

```
# Setup the handler.  
def handler():  
  page.evaluate("window.removeObstructionsForTestIfNeeded()")  
page.add_locator_handler(page.locator("body"), handler, no_wait_after=True)  
  
# Write the test as usual.  
page.goto("https://example.com")  
page.get_by_role("button", name="Start here").click()
```

```
# Setup the handler.  
async def handler():  
  await page.evaluate("window.removeObstructionsForTestIfNeeded()")  
await page.add_locator_handler(page.locator("body"), handler, no_wait_after=True)  
  
# Write the test as usual.  
await page.goto("https://example.com")  
await page.get_by_role("button", name="Start here").click()
```

Handler takes the original locator as an argument. You can also automatically remove the handler after a number of invocations by setting [times](Page.md):

* Sync* Async

```
def handler(locator):  
  locator.click()  
page.add_locator_handler(page.get_by_label("Close"), handler, times=1)
```

```
async def handler(locator):  
  await locator.click()  
await page.add_locator_handler(page.get_by_label("Close"), handler, times=1)
```

**Arguments**

* `locator` [Locator](Locator.md)

  Locator that triggers the handler.
* `handler` Callable[[Locator](Locator.md)]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any]

  Function that should be run once [locator](Page.md) appears. This function should get rid of the element that blocks actions like click.
* `no_wait_after` bool *(optional)* 

  By default, after calling the handler Playwright will wait until the overlay becomes hidden, and only then Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of this behavior, so that overlay can stay visible after the handler has run.
* `times` int *(optional)* 

  Specifies the maximum number of times this handler should be called. Unlimited by default.

**Returns**

* NoneType

---

### add_script_tag[​](#page-add-script-tag "Direct link to add_script_tag")

Added before v1.9
page.add_script_tag

Adds a `<script>` tag into the page with the desired url or content. Returns the added tag when the script's onload fires or when the script content was injected into frame.

**Usage**

```
page.add_script_tag()  
page.add_script_tag(**kwargs)
```

**Arguments**

* `content` str *(optional)*

  Raw JavaScript content to be injected into frame.
* `path` Union[str, pathlib.Path] *(optional)*

  Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory.
* `type` str *(optional)*

  Script type. Use 'module' in order to load a JavaScript ES6 module. See [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details.
* `url` str *(optional)*

  URL of a script to be added.

**Returns**

* [ElementHandle](Elementhandle.md)

---

### add_style_tag[​](#page-add-style-tag "Direct link to add_style_tag")

Added before v1.9
page.add_style_tag

Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the content. Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

**Usage**

```
page.add_style_tag()  
page.add_style_tag(**kwargs)
```

**Arguments**

* `content` str *(optional)*

  Raw CSS content to be injected into frame.
* `path` Union[str, pathlib.Path] *(optional)*

  Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory.
* `url` str *(optional)*

  URL of the `<link>` tag.

**Returns**

* [ElementHandle](Elementhandle.md)

---

### bring_to_front[​](#page-bring-to-front "Direct link to bring_to_front")

Added before v1.9
page.bring_to_front

Brings page to front (activates tab).

**Usage**

```
page.bring_to_front()
```

**Returns**

* NoneType

---

### close[​](#page-close "Direct link to close")

Added before v1.9
page.close

If [run_before_unload](Page.md) is `false`, does not run any unload handlers and waits for the page to be closed. If [run_before_unload](Page.md) is `true` the method will run unload handlers, but will **not** wait for the page to close.

By default, `page.close()` **does not** run `beforeunload` handlers.

note

if [run_before_unload](Page.md) is passed as true, a `beforeunload` dialog might be summoned and should be handled manually via [page.on("dialog")](Page.md) event.

**Usage**

```
page.close()  
page.close(**kwargs)
```

**Arguments**

* `reason` str *(optional)* 

  The reason to be reported to the operations interrupted by the page closure.
* `run_before_unload` bool *(optional)*

  Defaults to `false`. Whether to run the [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload) page handlers.

**Returns**

* NoneType

---

### console_messages[​](#page-console-messages "Direct link to console_messages") page.console_messages

Returns up to (currently) 200 last console messages from this page. See [page.on("console")](Page.md) for more details.

**Usage**

```
page.console_messages()
```

**Returns**

* List[[ConsoleMessage](Consolemessage.md)]

---

### content[​](#page-content "Direct link to content")

Added before v1.9
page.content

Gets the full HTML contents of the page, including the doctype.

**Usage**

```
page.content()
```

**Returns**

* str

---

### drag_and_drop[​](#page-drag-and-drop "Direct link to drag_and_drop") page.drag_and_drop

This method drags the source element to the target element. It will first move to the source element, perform a `mousedown`, then move to the target element and perform a `mouseup`.

**Usage**

* Sync* Async

```
page.drag_and_drop("#source", "#target")  
# or specify exact positions relative to the top-left corners of the elements:  
page.drag_and_drop(  
  "#source",  
  "#target",  
  source_position={"x": 34, "y": 7},  
  target_position={"x": 10, "y": 20}  
)
```

```
await page.drag_and_drop("#source", "#target")  
# or specify exact positions relative to the top-left corners of the elements:  
await page.drag_and_drop(  
  "#source",  
  "#target",  
  source_position={"x": 34, "y": 7},  
  target_position={"x": 10, "y": 20}  
)
```

**Arguments**

* `source` str

  A selector to search for an element to drag. If there are multiple elements satisfying the selector, the first will be used.
* `target` str

  A selector to search for an element to drop onto. If there are multiple elements satisfying the selector, the first will be used.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `source_position` Dict *(optional)* 

  + `x` float
  + `y` float

  Clicks on the source element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used.
* `steps` int *(optional)* 

  Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between the `mousedown` and `mouseup` of the drag. When set to 1, emits a single `mousemove` event at the destination location.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `target_position` Dict *(optional)* 

  + `x` float
  + `y` float

  Drops on the target element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)*

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### emulate_media[​](#page-emulate-media "Direct link to emulate_media")

Added before v1.9
page.emulate_media

This method changes the `CSS media type` through the `media` argument, and/or the `'prefers-colors-scheme'` media feature, using the `colorScheme` argument.

**Usage**

* Sync* Async

```
page.evaluate("matchMedia('screen').matches")  
# → True  
page.evaluate("matchMedia('print').matches")  
# → False  
  
page.emulate_media(media="print")  
page.evaluate("matchMedia('screen').matches")  
# → False  
page.evaluate("matchMedia('print').matches")  
# → True  
  
page.emulate_media()  
page.evaluate("matchMedia('screen').matches")  
# → True  
page.evaluate("matchMedia('print').matches")  
# → False
```

```
await page.evaluate("matchMedia('screen').matches")  
# → True  
await page.evaluate("matchMedia('print').matches")  
# → False  
  
await page.emulate_media(media="print")  
await page.evaluate("matchMedia('screen').matches")  
# → False  
await page.evaluate("matchMedia('print').matches")  
# → True  
  
await page.emulate_media()  
await page.evaluate("matchMedia('screen').matches")  
# → True  
await page.evaluate("matchMedia('print').matches")  
# → False
```

* Sync* Async

```
page.emulate_media(color_scheme="dark")  
page.evaluate("matchMedia('(prefers-color-scheme: dark)').matches")  
# → True  
page.evaluate("matchMedia('(prefers-color-scheme: light)').matches")  
# → False
```

```
await page.emulate_media(color_scheme="dark")  
await page.evaluate("matchMedia('(prefers-color-scheme: dark)').matches")  
# → True  
await page.evaluate("matchMedia('(prefers-color-scheme: light)').matches")  
# → False
```

**Arguments**

* `color_scheme` "light" | "dark" | "no-preference" | "null" *(optional)* 

  Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. Passing `'Null'` disables color scheme emulation. `'no-preference'` is deprecated.
* `contrast` "no-preference" | "more" | "null" *(optional)* 
* `forced_colors` "active" | "none" | "null" *(optional)* 
* `media` "screen" | "print" | "null" *(optional)* 

  Changes the CSS media type of the page. The only allowed values are `'Screen'`, `'Print'` and `'Null'`. Passing `'Null'` disables CSS media emulation.
* `reduced_motion` "reduce" | "no-preference" | "null" *(optional)* 

  Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. Passing `null` disables reduced motion emulation.

**Returns**

* NoneType

---

### evaluate[​](#page-evaluate "Direct link to evaluate")

Added before v1.9
page.evaluate

Returns the value of the [expression](Page.md) invocation.

If the function passed to the [page.evaluate()](Page.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [page.evaluate()](Page.md) would wait for the promise to resolve and return its value.

If the function passed to the [page.evaluate()](Page.md) returns a non-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") value, then [page.evaluate()](Page.md) resolves to `undefined`. Playwright also supports transferring some additional values that are not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

Passing argument to [expression](Page.md):

* Sync* Async

```
result = page.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])  
print(result) # prints "56"
```

```
result = await page.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])  
print(result) # prints "56"
```

A string can also be passed in instead of a function:

* Sync* Async

```
print(page.evaluate("1 + 2")) # prints "3"  
x = 10  
print(page.evaluate(f"1 + {x}")) # prints "11"
```

```
print(await page.evaluate("1 + 2")) # prints "3"  
x = 10  
print(await page.evaluate(f"1 + {x}")) # prints "11"
```

[ElementHandle](Elementhandle.md) instances can be passed as an argument to the [page.evaluate()](Page.md):

* Sync* Async

```
body_handle = page.evaluate("document.body")  
html = page.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])  
body_handle.dispose()
```

```
body_handle = await page.evaluate("document.body")  
html = await page.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])  
await body_handle.dispose()
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Page.md).

**Returns**

* Dict

---

### evaluate_handle[​](#page-evaluate-handle "Direct link to evaluate_handle")

Added before v1.9
page.evaluate_handle

Returns the value of the [expression](Page.md) invocation as a [JSHandle](Jshandle.md).

The only difference between [page.evaluate()](Page.md) and [page.evaluate_handle()](Page.md) is that [page.evaluate_handle()](Page.md) returns [JSHandle](Jshandle.md).

If the function passed to the [page.evaluate_handle()](Page.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [page.evaluate_handle()](Page.md) would wait for the promise to resolve and return its value.

**Usage**

* Sync* Async

```
a_window_handle = page.evaluate_handle("Promise.resolve(window)")  
a_window_handle # handle for the window object.
```

```
a_window_handle = await page.evaluate_handle("Promise.resolve(window)")  
a_window_handle # handle for the window object.
```

A string can also be passed in instead of a function:

* Sync* Async

```
a_handle = page.evaluate_handle("document") # handle for the "document"
```

```
a_handle = await page.evaluate_handle("document") # handle for the "document"
```

[JSHandle](Jshandle.md) instances can be passed as an argument to the [page.evaluate_handle()](Page.md):

* Sync* Async

```
a_handle = page.evaluate_handle("document.body")  
result_handle = page.evaluate_handle("body => body.innerHTML", a_handle)  
print(result_handle.json_value())  
result_handle.dispose()
```

```
a_handle = await page.evaluate_handle("document.body")  
result_handle = await page.evaluate_handle("body => body.innerHTML", a_handle)  
print(await result_handle.json_value())  
await result_handle.dispose()
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Page.md).

**Returns**

* [JSHandle](Jshandle.md)

---

### expect_console_message[​](#page-wait-for-console-message "Direct link to expect_console_message") page.expect_console_message

Performs action and waits for a [ConsoleMessage](Consolemessage.md) to be logged by in the page. If predicate is provided, it passes [ConsoleMessage](Consolemessage.md) value into the `predicate` function and waits for `predicate(message)` to return a truthy value. Will throw an error if the page is closed before the [page.on("console")](Page.md) event is fired.

**Usage**

```
page.expect_console_message()  
page.expect_console_message(**kwargs)
```

**Arguments**

* `predicate` Callable[[ConsoleMessage](Consolemessage.md)]:bool *(optional)*

  Receives the [ConsoleMessage](Consolemessage.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[ConsoleMessage](Consolemessage.md)]

---

### expect_download[​](#page-wait-for-download "Direct link to expect_download") page.expect_download

Performs action and waits for a new [Download](Download.md). If predicate is provided, it passes [Download](Download.md) value into the `predicate` function and waits for `predicate(download)` to return a truthy value. Will throw an error if the page is closed before the download event is fired.

**Usage**

```
page.expect_download()  
page.expect_download(**kwargs)
```

**Arguments**

* `predicate` Callable[[Download](Download.md)]:bool *(optional)*

  Receives the [Download](Download.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[Download](Download.md)]

---

### expect_event[​](#page-wait-for-event "Direct link to expect_event")

Added before v1.9
page.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

**Usage**

* Sync* Async

```
with page.expect_event("framenavigated") as event_info:  
    page.get_by_role("button")  
frame = event_info.value
```

```
async with page.expect_event("framenavigated") as event_info:  
    await page.get_by_role("button")  
frame = await event_info.value
```

**Arguments**

* `event` str

  Event name, same one typically passed into `*.on(event)`.
* `predicate` Callable *(optional)*

  Receives the event data and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager

---

### expect_file_chooser[​](#page-wait-for-file-chooser "Direct link to expect_file_chooser") page.expect_file_chooser

Performs action and waits for a new [FileChooser](Filechooser.md) to be created. If predicate is provided, it passes [FileChooser](Filechooser.md) value into the `predicate` function and waits for `predicate(fileChooser)` to return a truthy value. Will throw an error if the page is closed before the file chooser is opened.

**Usage**

```
page.expect_file_chooser()  
page.expect_file_chooser(**kwargs)
```

**Arguments**

* `predicate` Callable[[FileChooser](Filechooser.md)]:bool *(optional)*

  Receives the [FileChooser](Filechooser.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[FileChooser](Filechooser.md)]

---

### expect_popup[​](#page-wait-for-popup "Direct link to expect_popup") page.expect_popup

Performs action and waits for a popup [Page](Page.md). If predicate is provided, it passes [Popup] value into the `predicate` function and waits for `predicate(page)` to return a truthy value. Will throw an error if the page is closed before the popup event is fired.

**Usage**

```
page.expect_popup()  
page.expect_popup(**kwargs)
```

**Arguments**

* `predicate` Callable[[Page](Page.md)]:bool *(optional)*

  Receives the [Page](Page.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[Page](Page.md)]

---

### expect_request[​](#page-wait-for-request "Direct link to expect_request")

Added before v1.9
page.expect_request

Waits for the matching request and returns it. See [waiting for event](/python/docs/events#waiting-for-event) for more details about events.

**Usage**

* Sync* Async

```
with page.expect_request("http://example.com/resource") as first:  
    page.get_by_text("trigger request").click()  
first_request = first.value  
  
# or with a lambda  
with page.expect_request(lambda request: request.url == "http://example.com" and request.method == "get") as second:  
    page.get_by_text("trigger request").click()  
second_request = second.value
```

```
async with page.expect_request("http://example.com/resource") as first:  
    await page.get_by_text("trigger request").click()  
first_request = await first.value  
  
# or with a lambda  
async with page.expect_request(lambda request: request.url == "http://example.com" and request.method == "get") as second:  
    await page.get_by_text("trigger request").click()  
second_request = await second.value
```

**Arguments**

* `url_or_predicate` str | Pattern | Callable[[Request](Request.md)]:bool

  Request URL string, regex or predicate receiving [Request](Request.md) object. When a [base_url](Browser.md) via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor.
* `timeout` float *(optional)*

  Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the [page.set_default_timeout()](Page.md) method.

**Returns**

* EventContextManager[[Request](Request.md)]

---

### expect_request_finished[​](#page-wait-for-request-finished "Direct link to expect_request_finished") page.expect_request_finished

Performs action and waits for a [Request](Request.md) to finish loading. If predicate is provided, it passes [Request](Request.md) value into the `predicate` function and waits for `predicate(request)` to return a truthy value. Will throw an error if the page is closed before the [page.on("requestfinished")](Page.md) event is fired.

**Usage**

```
page.expect_request_finished()  
page.expect_request_finished(**kwargs)
```

**Arguments**

* `predicate` Callable[[Request](Request.md)]:bool *(optional)*

  Receives the [Request](Request.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[Request](Request.md)]

---

### expect_response[​](#page-wait-for-response "Direct link to expect_response")

Added before v1.9
page.expect_response

Returns the matched response. See [waiting for event](/python/docs/events#waiting-for-event) for more details about events.

**Usage**

* Sync* Async

```
with page.expect_response("https://example.com/resource") as response_info:  
    page.get_by_text("trigger response").click()  
response = response_info.value  
return response.ok  
  
# or with a lambda  
with page.expect_response(lambda response: response.url == "https://example.com" and response.status == 200 and response.request.method == "get") as response_info:  
    page.get_by_text("trigger response").click()  
response = response_info.value  
return response.ok
```

```
async with page.expect_response("https://example.com/resource") as response_info:  
    await page.get_by_text("trigger response").click()  
response = await response_info.value  
return response.ok  
  
# or with a lambda  
async with page.expect_response(lambda response: response.url == "https://example.com" and response.status == 200 and response.request.method == "get") as response_info:  
    await page.get_by_text("trigger response").click()  
response = await response_info.value  
return response.ok
```

**Arguments**

* `url_or_predicate` str | Pattern | Callable[[Response](Response.md)]:bool

  Request URL string, regex or predicate receiving [Response](Response.md) object. When a [base_url](Browser.md) via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor.
* `timeout` float *(optional)*

  Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* EventContextManager[[Response](Response.md)]

---

### expect_websocket[​](#page-wait-for-web-socket "Direct link to expect_websocket") page.expect_websocket

Performs action and waits for a new [WebSocket](Websocket.md). If predicate is provided, it passes [WebSocket](Websocket.md) value into the `predicate` function and waits for `predicate(webSocket)` to return a truthy value. Will throw an error if the page is closed before the WebSocket event is fired.

**Usage**

```
page.expect_websocket()  
page.expect_websocket(**kwargs)
```

**Arguments**

* `predicate` Callable[[WebSocket](Websocket.md)]:bool *(optional)*

  Receives the [WebSocket](Websocket.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[WebSocket](Websocket.md)]

---

### expect_worker[​](#page-wait-for-worker "Direct link to expect_worker") page.expect_worker

Performs action and waits for a new [Worker](Worker.md). If predicate is provided, it passes [Worker](Worker.md) value into the `predicate` function and waits for `predicate(worker)` to return a truthy value. Will throw an error if the page is closed before the worker event is fired.

**Usage**

```
page.expect_worker()  
page.expect_worker(**kwargs)
```

**Arguments**

* `predicate` Callable[[Worker](Worker.md)]:bool *(optional)*

  Receives the [Worker](Worker.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[Worker](Worker.md)]

---

### expose_binding[​](#page-expose-binding "Direct link to expose_binding")

Added before v1.9
page.expose_binding

The method adds a function called [name](Page.md) on the `window` object of every frame in this page. When called, the function executes [callback](Page.md) and returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise") which resolves to the return value of [callback](Page.md). If the [callback](Page.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), it will be awaited.

The first argument of the [callback](Page.md) function contains information about the caller: `{ browserContext: BrowserContext, page: Page, frame: Frame }`.

See [browser_context.expose_binding()](Browsercontext.md) for the context-wide version.

note

Functions installed via [page.expose_binding()](Page.md) survive navigations.

**Usage**

An example of exposing page URL to all frames in a page:

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = webkit.launch(headless=False)  
    context = browser.new_context()  
    page = context.new_page()  
    page.expose_binding("pageURL", lambda source: source["page"].url)  
    page.set_content("""  
    <script>  
      async function onClick() {  
        document.querySelector('div').textContent = await window.pageURL();  
      }  
    </script>  
    <button onclick="onClick()">Click me</button>  
    <div></div>  
    """)  
    page.click("button")  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = await webkit.launch(headless=False)  
    context = await browser.new_context()  
    page = await context.new_page()  
    await page.expose_binding("pageURL", lambda source: source["page"].url)  
    await page.set_content("""  
    <script>  
      async function onClick() {  
        document.querySelector('div').textContent = await window.pageURL();  
      }  
    </script>  
    <button onclick="onClick()">Click me</button>  
    <div></div>  
    """)  
    await page.click("button")  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

**Arguments**

* `name` str

  Name of the function on the window object.
* `callback` Callable

  Callback function that will be called in the Playwright's context.
* `handle` bool *(optional)*

  Deprecated

  This option will be removed in the future.

  Whether to pass the argument as a handle, instead of passing by value. When passing a handle, only one argument is supported. When passing by value, multiple arguments are supported.

**Returns**

* NoneType

---

### expose_function[​](#page-expose-function "Direct link to expose_function")

Added before v1.9
page.expose_function

The method adds a function called [name](Page.md) on the `window` object of every frame in the page. When called, the function executes [callback](Page.md) and returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise") which resolves to the return value of [callback](Page.md).

If the [callback](Page.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), it will be awaited.

See [browser_context.expose_function()](Browsercontext.md) for context-wide exposed function.

note

Functions installed via [page.expose_function()](Page.md) survive navigations.

**Usage**

An example of adding a `sha256` function to the page:

* Sync* Async

```
import hashlib  
from playwright.sync_api import sync_playwright, Playwright  
  
def sha256(text):  
    m = hashlib.sha256()  
    m.update(bytes(text, "utf8"))  
    return m.hexdigest()  
  
  
def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = webkit.launch(headless=False)  
    page = browser.new_page()  
    page.expose_function("sha256", sha256)  
    page.set_content("""  
        <script>  
          async function onClick() {  
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');  
          }  
        </script>  
        <button onclick="onClick()">Click me</button>  
        <div></div>  
    """)  
    page.click("button")  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
import hashlib  
from playwright.async_api import async_playwright, Playwright  
  
def sha256(text):  
    m = hashlib.sha256()  
    m.update(bytes(text, "utf8"))  
    return m.hexdigest()  
  
  
async def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = await webkit.launch(headless=False)  
    page = await browser.new_page()  
    await page.expose_function("sha256", sha256)  
    await page.set_content("""  
        <script>  
          async function onClick() {  
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');  
          }  
        </script>  
        <button onclick="onClick()">Click me</button>  
        <div></div>  
    """)  
    await page.click("button")  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

**Arguments**

* `name` str

  Name of the function on the window object
* `callback` Callable

  Callback function which will be called in Playwright's context.

**Returns**

* NoneType

---

### frame[​](#page-frame "Direct link to frame")

Added before v1.9
page.frame

Returns frame matching the specified criteria. Either `name` or `url` must be specified.

**Usage**

```
frame = page.frame(name="frame-name")
```

```
frame = page.frame(url=r".*domain.*")
```

**Arguments**

* `name` str *(optional)*

  Frame name specified in the `iframe`'s `name` attribute. Optional.
* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool *(optional)*

  A glob pattern, regex pattern or predicate receiving frame's `url` as a [URL](https://en.wikipedia.org/wiki/URL "URL") object. Optional.

**Returns**

* NoneType | [Frame](Frame.md)

---

### frame_locator[​](#page-frame-locator "Direct link to frame_locator") page.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements in that iframe.

**Usage**

Following snippet locates element with text "Submit" in the iframe with id `my-frame`, like `<iframe id="my-frame">`:

* Sync* Async

```
locator = page.frame_locator("#my-iframe").get_by_text("Submit")  
locator.click()
```

```
locator = page.frame_locator("#my-iframe").get_by_text("Submit")  
await locator.click()
```

**Arguments**

* `selector` str

  A selector to use when resolving DOM element.

**Returns**

* [FrameLocator](Framelocator.md)

---

### get_by_alt_text[​](#page-get-by-alt-text "Direct link to get_by_alt_text") page.get_by_alt_text

Allows locating elements by their alt text.

**Usage**

For example, this method will find the image by alt text "Playwright logo":

```
<img alt='Playwright logo'>
```

* Sync* Async

```
page.get_by_alt_text("Playwright logo").click()
```

```
await page.get_by_alt_text("Playwright logo").click()
```

**Arguments**

* `text` str | Pattern

  Text to locate the element for.
* `exact` bool *(optional)*

  Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

* [Locator](Locator.md)

---

### get_by_label[​](#page-get-by-label "Direct link to get_by_label") page.get_by_label

Allows locating input elements by the text of the associated `<label>` or `aria-labelledby` element, or by the `aria-label` attribute.

**Usage**

For example, this method will find inputs by label "Username" and "Password" in the following DOM:

```
<input aria-label="Username">  
<label for="password-input">Password:</label>  
<input id="password-input">
```

* Sync* Async

```
page.get_by_label("Username").fill("john")  
page.get_by_label("Password").fill("secret")
```

```
await page.get_by_label("Username").fill("john")  
await page.get_by_label("Password").fill("secret")
```

**Arguments**

* `text` str | Pattern

  Text to locate the element for.
* `exact` bool *(optional)*

  Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

* [Locator](Locator.md)

---

### get_by_placeholder[​](#page-get-by-placeholder "Direct link to get_by_placeholder") page.get_by_placeholder

Allows locating input elements by the placeholder text.

**Usage**

For example, consider the following DOM structure.

```
<input type="email" placeholder="name@example.com" />
```

You can fill the input after locating it by the placeholder text:

* Sync* Async

```
page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
```

```
await page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
```

**Arguments**

* `text` str | Pattern

  Text to locate the element for.
* `exact` bool *(optional)*

  Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

* [Locator](Locator.md)

---

### get_by_role[​](#page-get-by-role "Direct link to get_by_role") page.get_by_role

Allows locating elements by their [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles), [ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes) and [accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

Consider the following DOM structure.

```
<h3>Sign up</h3>  
<label>  
  <input type="checkbox" /> Subscribe  
</label>  
<br/>  
<button>Submit</button>
```

You can locate each element by it's implicit role:

* Sync* Async

```
expect(page.get_by_role("heading", name="Sign up")).to_be_visible()  
  
page.get_by_role("checkbox", name="Subscribe").check()  
  
page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
```

```
await expect(page.get_by_role("heading", name="Sign up")).to_be_visible()  
  
await page.get_by_role("checkbox", name="Subscribe").check()  
  
await page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
```

**Arguments**

* `role` "alert" | "alertdialog" | "application" | "article" | "banner" | "blockquote" | "button" | "caption" | "cell" | "checkbox" | "code" | "columnheader" | "combobox" | "complementary" | "contentinfo" | "definition" | "deletion" | "dialog" | "directory" | "document" | "emphasis" | "feed" | "figure" | "form" | "generic" | "grid" | "gridcell" | "group" | "heading" | "img" | "insertion" | "link" | "list" | "listbox" | "listitem" | "log" | "main" | "marquee" | "math" | "meter" | "menu" | "menubar" | "menuitem" | "menuitemcheckbox" | "menuitemradio" | "navigation" | "none" | "note" | "option" | "paragraph" | "presentation" | "progressbar" | "radio" | "radiogroup" | "region" | "row" | "rowgroup" | "rowheader" | "scrollbar" | "search" | "searchbox" | "separator" | "slider" | "spinbutton" | "status" | "strong" | "subscript" | "superscript" | "switch" | "tab" | "table" | "tablist" | "tabpanel" | "term" | "textbox" | "time" | "timer" | "toolbar" | "tooltip" | "tree" | "treegrid" | "treeitem"

  Required aria role.
* `checked` bool *(optional)*

  An attribute that is usually set by `aria-checked` or native `<input type=checkbox>` controls.

  Learn more about [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked).
* `disabled` bool *(optional)*

  An attribute that is usually set by `aria-disabled` or `disabled`.

  note

  Unlike most other attributes, `disabled` is inherited through the DOM hierarchy. Learn more about [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled).
* `exact` bool *(optional)* 

  Whether [name](Page.md) is matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when [name](Page.md) is a regular expression. Note that exact match still trims whitespace.
* `expanded` bool *(optional)*

  An attribute that is usually set by `aria-expanded`.

  Learn more about [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded).
* `include_hidden` bool *(optional)*

  Option that controls whether hidden elements are matched. By default, only non-hidden elements, as [defined by ARIA](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion), are matched by role selector.

  Learn more about [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden).
* `level` int *(optional)*

  A number attribute that is usually present for roles `heading`, `listitem`, `row`, `treeitem`, with default values for `<h1>-<h6>` elements.

  Learn more about [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level).
* `name` str | Pattern *(optional)*

  Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use [exact](Page.md) to control this behavior.

  Learn more about [accessible name](https://w3c.github.io/accname/#dfn-accessible-name).
* `pressed` bool *(optional)*

  An attribute that is usually set by `aria-pressed`.

  Learn more about [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed).
* `selected` bool *(optional)*

  An attribute that is usually set by `aria-selected`.

  Learn more about [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected).

**Returns**

* [Locator](Locator.md)

**Details**

Role selector **does not replace** accessibility audits and conformance tests, but rather gives early feedback about the ARIA guidelines.

Many html elements have an implicitly [defined role](https://w3c.github.io/html-aam/#html-element-role-mappings) that is recognized by the role selector. You can find all the [supported roles here](https://www.w3.org/TR/wai-aria-1.2/#role_definitions). ARIA guidelines **do not recommend** duplicating implicit roles and attributes by setting `role` and/or `aria-*` attributes to default values.

---

### get_by_test_id[​](#page-get-by-test-id "Direct link to get_by_test_id") page.get_by_test_id

Locate element by the test id.

**Usage**

Consider the following DOM structure.

```
<button data-testid="directions">Itinéraire</button>
```

You can locate the element by it's test id:

* Sync* Async

```
page.get_by_test_id("directions").click()
```

```
await page.get_by_test_id("directions").click()
```

**Arguments**

* `test_id` str | Pattern

  Id to locate the element by.

**Returns**

* [Locator](Locator.md)

**Details**

By default, the `data-testid` attribute is used as a test id. Use [selectors.set_test_id_attribute()](Selectors.md) to configure a different test id attribute if necessary.

---

### get_by_text[​](#page-get-by-text "Direct link to get_by_text") page.get_by_text

Allows locating elements that contain given text.

See also [locator.filter()](Locator.md) that allows to match by another criteria, like an accessible role, and then filter by the text content.

**Usage**

Consider the following DOM structure:

```
<div>Hello <span>world</span></div>  
<div>Hello</div>
```

You can locate by text substring, exact string, or a regular expression:

* Sync* Async

```
# Matches <span>  
page.get_by_text("world")  
  
# Matches first <div>  
page.get_by_text("Hello world")  
  
# Matches second <div>  
page.get_by_text("Hello", exact=True)  
  
# Matches both <div>s  
page.get_by_text(re.compile("Hello"))  
  
# Matches second <div>  
page.get_by_text(re.compile("^hello$", re.IGNORECASE))
```

```
# Matches <span>  
page.get_by_text("world")  
  
# Matches first <div>  
page.get_by_text("Hello world")  
  
# Matches second <div>  
page.get_by_text("Hello", exact=True)  
  
# Matches both <div>s  
page.get_by_text(re.compile("Hello"))  
  
# Matches second <div>  
page.get_by_text(re.compile("^hello$", re.IGNORECASE))
```

**Arguments**

* `text` str | Pattern

  Text to locate the element for.
* `exact` bool *(optional)*

  Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

* [Locator](Locator.md)

**Details**

Matching by text always normalizes whitespace, even with exact match. For example, it turns multiple spaces into one, turns line breaks into spaces and ignores leading and trailing whitespace.

Input elements of the type `button` and `submit` are matched by their `value` instead of the text content. For example, locating by text `"Log in"` matches `<input type=button value="Log in">`.

---

### get_by_title[​](#page-get-by-title "Direct link to get_by_title") page.get_by_title

Allows locating elements by their title attribute.

**Usage**

Consider the following DOM structure.

```
<span title='Issues count'>25 issues</span>
```

You can check the issues count after locating it by the title text:

* Sync* Async

```
expect(page.get_by_title("Issues count")).to_have_text("25 issues")
```

```
await expect(page.get_by_title("Issues count")).to_have_text("25 issues")
```

**Arguments**

* `text` str | Pattern

  Text to locate the element for.
* `exact` bool *(optional)*

  Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

**Returns**

* [Locator](Locator.md)

---

### go_back[​](#page-go-back "Direct link to go_back")

Added before v1.9
page.go_back

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect. If cannot go back, returns `null`.

Navigate to the previous page in history.

**Usage**

```
page.go_back()  
page.go_back(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.
* `wait_until` "load" | "domcontentloaded" | "networkidle" | "commit" *(optional)*

  When to consider operation succeeded, defaults to `load`. Events can be either:

  + `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
  + `'load'` - consider operation to be finished when the `load` event is fired.
  + `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
  + `'commit'` - consider operation to be finished when network response is received and the document started loading.

**Returns**

* NoneType | [Response](Response.md)

---

### go_forward[​](#page-go-forward "Direct link to go_forward")

Added before v1.9
page.go_forward

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect. If cannot go forward, returns `null`.

Navigate to the next page in history.

**Usage**

```
page.go_forward()  
page.go_forward(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.
* `wait_until` "load" | "domcontentloaded" | "networkidle" | "commit" *(optional)*

  When to consider operation succeeded, defaults to `load`. Events can be either:

  + `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
  + `'load'` - consider operation to be finished when the `load` event is fired.
  + `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
  + `'commit'` - consider operation to be finished when network response is received and the document started loading.

**Returns**

* NoneType | [Response](Response.md)

---

### goto[​](#page-goto "Direct link to goto")

Added before v1.9
page.goto

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the first non-redirect response.

The method will throw an error if:

* there's an SSL error (e.g. in case of self-signed certificates).
* target URL is invalid.
* the [timeout](Page.md) is exceeded during navigation.
* the remote server does not respond or is unreachable.
* the main resource failed to load.

The method will not throw an error when any valid HTTP status code is returned by the remote server, including 404 "Not Found" and 500 "Internal Server Error". The status code for such responses can be retrieved by calling [response.status](Response.md).

note

The method either throws an error or returns a main resource response. The only exceptions are navigation to `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.

note

Headless mode doesn't support navigation to a PDF document. See the [upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

**Usage**

```
page.goto(url)  
page.goto(url, **kwargs)
```

**Arguments**

* `url` str

  URL to navigate page to. The url should include scheme, e.g. `https://`. When a [base_url](Browser.md) via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor.
* `referer` str *(optional)*

  Referer header value. If provided it will take preference over the referer header value set by [page.set_extra_http_headers()](Page.md).
* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.
* `wait_until` "load" | "domcontentloaded" | "networkidle" | "commit" *(optional)*

  When to consider operation succeeded, defaults to `load`. Events can be either:

  + `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
  + `'load'` - consider operation to be finished when the `load` event is fired.
  + `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
  + `'commit'` - consider operation to be finished when network response is received and the document started loading.

**Returns**

* NoneType | [Response](Response.md)

---

### locator[​](#page-locator "Direct link to locator") page.locator

The method returns an element locator that can be used to perform actions on this page / frame. Locator is resolved to the element immediately before performing an action, so a series of actions on the same locator can in fact be performed on different DOM elements. That would happen if the DOM structure between those actions has changed.

[Learn more about locators](/python/docs/locators).

**Usage**

```
page.locator(selector)  
page.locator(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to use when resolving DOM element.
* `has` [Locator](Locator.md) *(optional)*

  Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.

  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.

  Note that outer and inner locators must belong to the same frame. Inner locator must not contain [FrameLocator](Framelocator.md)s.
* `has_not` [Locator](Locator.md) *(optional)* 

  Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.

  Note that outer and inner locators must belong to the same frame. Inner locator must not contain [FrameLocator](Framelocator.md)s.
* `has_not_text` str | Pattern *(optional)* 

  Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring.
* `has_text` str | Pattern *(optional)*

  Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`.

**Returns**

* [Locator](Locator.md)

---

### opener[​](#page-opener "Direct link to opener")

Added before v1.9
page.opener

Returns the opener for popup pages and `null` for others. If the opener has been closed already the returns `null`.

**Usage**

```
page.opener()
```

**Returns**

* NoneType | [Page](Page.md)

---

### page_errors[​](#page-page-errors "Direct link to page_errors") page.page_errors

Returns up to (currently) 200 last page errors from this page. See [page.on("pageerror")](Page.md) for more details.

**Usage**

```
page.page_errors()
```

**Returns**

* List[[Error](Error.md)]

---

### pause[​](#page-pause "Direct link to pause") page.pause

Pauses script execution. Playwright will stop executing the script and wait for the user to either press the 'Resume' button in the page overlay or to call `playwright.resume()` in the DevTools console.

User can inspect selectors or perform manual steps while paused. Resume will continue running the original script from the place it was paused.

note

This method requires Playwright to be started in a headed mode, with a falsy [headless](Browsertype.md) option.

**Usage**

```
page.pause()
```

**Returns**

* NoneType

---

### pdf[​](#page-pdf "Direct link to pdf")

Added before v1.9
page.pdf

Returns the PDF buffer.

`page.pdf()` generates a pdf of the page with `print` css media. To generate a pdf with `screen` media, call [page.emulate_media()](Page.md) before calling `page.pdf()`:

note

By default, `page.pdf()` generates a pdf with modified colors for printing. Use the [`-webkit-print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-print-color-adjust) property to force rendering of exact colors.

**Usage**

* Sync* Async

```
# generates a pdf with "screen" media type.  
page.emulate_media(media="screen")  
page.pdf(path="page.pdf")
```

```
# generates a pdf with "screen" media type.  
await page.emulate_media(media="screen")  
await page.pdf(path="page.pdf")
```

The [width](Page.md), [height](Page.md), and [margin](Page.md) options accept values labeled with units. Unlabeled values are treated as pixels.

A few examples:

* `page.pdf({width: 100})` - prints with width set to 100 pixels
* `page.pdf({width: '100px'})` - prints with width set to 100 pixels
* `page.pdf({width: '10cm'})` - prints with width set to 10 centimeters.

All possible units are:

* `px` - pixel
* `in` - inch
* `cm` - centimeter
* `mm` - millimeter

The [format](Page.md) options are:

* `Letter`: 8.5in x 11in
* `Legal`: 8.5in x 14in
* `Tabloid`: 11in x 17in
* `Ledger`: 17in x 11in
* `A0`: 33.1in x 46.8in
* `A1`: 23.4in x 33.1in
* `A2`: 16.54in x 23.4in
* `A3`: 11.7in x 16.54in
* `A4`: 8.27in x 11.7in
* `A5`: 5.83in x 8.27in
* `A6`: 4.13in x 5.83in

note

[header_template](Page.md) and [footer_template](Page.md) markup have the following limitations: > 1. Script tags inside templates are not evaluated. > 2. Page styles are not visible inside templates.

**Arguments**

* `display_header_footer` bool *(optional)*

  Display header and footer. Defaults to `false`.
* `footer_template` str *(optional)*

  HTML template for the print footer. Should use the same format as the [header_template](Page.md).
* `format` str *(optional)*

  Paper format. If set, takes priority over [width](Page.md) or [height](Page.md) options. Defaults to 'Letter'.
* `header_template` str *(optional)*

  HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them:

  + `'date'` formatted print date
  + `'title'` document title
  + `'url'` document location
  + `'pageNumber'` current page number
  + `'totalPages'` total pages in the document
* `height` str | float *(optional)*

  Paper height, accepts values labeled with units.
* `landscape` bool *(optional)*

  Paper orientation. Defaults to `false`.
* `margin` Dict *(optional)*

  + `top` str | float *(optional)*

    Top margin, accepts values labeled with units. Defaults to `0`.
  + `right` str | float *(optional)*

    Right margin, accepts values labeled with units. Defaults to `0`.
  + `bottom` str | float *(optional)*

    Bottom margin, accepts values labeled with units. Defaults to `0`.
  + `left` str | float *(optional)*

    Left margin, accepts values labeled with units. Defaults to `0`.

  Paper margins, defaults to none.
* `outline` bool *(optional)* 

  Whether or not to embed the document outline into the PDF. Defaults to `false`.
* `page_ranges` str *(optional)*

  Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.
* `path` Union[str, pathlib.Path] *(optional)*

  The file path to save the PDF to. If [path](Page.md) is a relative path, then it is resolved relative to the current working directory. If no path is provided, the PDF won't be saved to the disk.
* `prefer_css_page_size` bool *(optional)*

  Give any CSS `@page` size declared in the page priority over what is declared in [width](Page.md) and [height](Page.md) or [format](Page.md) options. Defaults to `false`, which will scale the content to fit the paper size.
* `print_background` bool *(optional)*

  Print background graphics. Defaults to `false`.
* `scale` float *(optional)*

  Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.
* `tagged` bool *(optional)* 

  Whether or not to generate tagged (accessible) PDF. Defaults to `false`.
* `width` str | float *(optional)*

  Paper width, accepts values labeled with units.

**Returns**

* bytes

---

### reload[​](#page-reload "Direct link to reload")

Added before v1.9
page.reload

This method reloads the current page, in the same way as if the user had triggered a browser refresh. Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect.

**Usage**

```
page.reload()  
page.reload(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.
* `wait_until` "load" | "domcontentloaded" | "networkidle" | "commit" *(optional)*

  When to consider operation succeeded, defaults to `load`. Events can be either:

  + `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
  + `'load'` - consider operation to be finished when the `load` event is fired.
  + `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
  + `'commit'` - consider operation to be finished when network response is received and the document started loading.

**Returns**

* NoneType | [Response](Response.md)

---

### remove_locator_handler[​](#page-remove-locator-handler "Direct link to remove_locator_handler") page.remove_locator_handler

Removes all locator handlers added by [page.add_locator_handler()](Page.md) for a specific locator.

**Usage**

```
page.remove_locator_handler(locator)
```

**Arguments**

* `locator` [Locator](Locator.md)

  Locator passed to [page.add_locator_handler()](Page.md).

**Returns**

* NoneType

---

### request_gc[​](#page-request-gc "Direct link to request_gc") page.request_gc

Request the page to perform garbage collection. Note that there is no guarantee that all unreachable objects will be collected.

This is useful to help detect memory leaks. For example, if your page has a large object `'suspect'` that might be leaked, you can check that it does not leak by using a [`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef).

* Sync* Async

```
# 1. In your page, save a WeakRef for the "suspect".  
page.evaluate("globalThis.suspectWeakRef = new WeakRef(suspect)")  
# 2. Request garbage collection.  
page.request_gc()  
# 3. Check that weak ref does not deref to the original object.  
assert page.evaluate("!globalThis.suspectWeakRef.deref()")
```

```
# 1. In your page, save a WeakRef for the "suspect".  
await page.evaluate("globalThis.suspectWeakRef = new WeakRef(suspect)")  
# 2. Request garbage collection.  
await page.request_gc()  
# 3. Check that weak ref does not deref to the original object.  
assert await page.evaluate("!globalThis.suspectWeakRef.deref()")
```

**Usage**

```
page.request_gc()
```

**Returns**

* NoneType

---

### requests[​](#page-requests "Direct link to requests") page.requests

Returns up to (currently) 100 last network request from this page. See [page.on("request")](Page.md) for more details.

Returned requests should be accessed immediately, otherwise they might be collected to prevent unbounded memory growth as new requests come in. Once collected, retrieving most information about the request is impossible.

Note that requests reported through the [page.on("request")](Page.md) request are not collected, so there is a trade off between efficient memory usage with [page.requests()](Page.md) and the amount of available information reported through [page.on("request")](Page.md).

**Usage**

```
page.requests()
```

**Returns**

* List[[Request](Request.md)]

---

### route[​](#page-route "Direct link to route")

Added before v1.9
page.route

Routing provides the capability to modify network requests that are made by a page.

Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

note

The handler will only be called for the first url if the response is a redirect.

note

[page.route()](Page.md) will not intercept requests intercepted by Service Worker. See [this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when using request interception by setting [service_workers](Browser.md) to `'block'`.

note

[page.route()](Page.md) will not intercept the first request of a popup page. Use [browser_context.route()](Browsercontext.md) instead.

**Usage**

An example of a naive handler that aborts all image requests:

* Sync* Async

```
page = browser.new_page()  
page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())  
page.goto("https://example.com")  
browser.close()
```

```
page = await browser.new_page()  
await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())  
await page.goto("https://example.com")  
await browser.close()
```

or the same snippet using a regex pattern instead:

* Sync* Async

```
page = browser.new_page()  
page.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())  
page.goto("https://example.com")  
browser.close()
```

```
page = await browser.new_page()  
await page.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())  
await page.goto("https://example.com")  
await browser.close()
```

It is possible to examine the request to decide the route action. For example, mocking all requests that contain some post data, and leaving all other requests as is:

* Sync* Async

```
def handle_route(route: Route):  
  if ("my-string" in route.request.post_data):  
    route.fulfill(body="mocked-data")  
  else:  
    route.continue_()  
page.route("/api/**", handle_route)
```

```
async def handle_route(route: Route):  
  if ("my-string" in route.request.post_data):  
    await route.fulfill(body="mocked-data")  
  else:  
    await route.continue_()  
await page.route("/api/**", handle_route)
```

Page routes take precedence over browser context routes (set up with [browser_context.route()](Browsercontext.md)) when request matches both handlers.

To remove a route with its handler you can use [page.unroute()](Page.md).

note

Enabling routing disables http cache.

**Arguments**

* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool

  A glob pattern, regex pattern, or predicate that receives a [URL](https://en.wikipedia.org/wiki/URL "URL") to match during routing. If [base_url](Browser.md) is set in the context options and the provided URL is a string that does not start with `*`, it is resolved using the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor.
* `handler` Callable[[Route](Route.md), [Request](Request.md)]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any] | Any

  handler function to route the request.
* `times` int *(optional)* 

  How often a route should be used. By default it will be used every time.

**Returns**

* NoneType

---

### route_from_har[​](#page-route-from-har "Direct link to route_from_har") page.route_from_har

If specified the network requests that are made in the page will be served from the HAR file. Read more about [Replaying from HAR](/python/docs/mock#replaying-from-har).

Playwright will not serve requests intercepted by Service Worker from the HAR file. See [this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when using request interception by setting [service_workers](Browser.md) to `'block'`.

**Usage**

```
page.route_from_har(har)  
page.route_from_har(har, **kwargs)
```

**Arguments**

* `har` Union[str, pathlib.Path]

  Path to a [HAR](http://www.softwareishard.com/blog/har-12-spec) file with prerecorded network data. If `path` is a relative path, then it is resolved relative to the current working directory.
* `not_found` "abort" | "fallback" *(optional)*

  + If set to 'abort' any request not found in the HAR file will be aborted.
  + If set to 'fallback' missing requests will be sent to the network.

  Defaults to abort.
* `update` bool *(optional)*

  If specified, updates the given HAR with the actual network information instead of serving from file. The file is written to disk when [browser_context.close()](Browsercontext.md) is called.
* `update_content` "embed" | "attach" *(optional)* 

  Optional setting to control resource content management. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file.
* `update_mode` "full" | "minimal" *(optional)* 

  When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `minimal`.
* `url` str | Pattern *(optional)*

  A glob pattern, regular expression or predicate to match the request URL. Only requests with URL matching the pattern will be served from the HAR file. If not specified, all requests are served from the HAR file.

**Returns**

* NoneType

---

### route_web_socket[​](#page-route-web-socket "Direct link to route_web_socket") page.route_web_socket

This method allows to modify websocket connections that are made by the page.

Note that only `WebSocket`s created after this method was called will be routed. It is recommended to call this method before navigating the page.

**Usage**

Below is an example of a simple mock that responds to a single message. See [WebSocketRoute](Websocketroute.md) for more details and examples.

* Sync* Async

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message == "request":  
    ws.send("response")  
  
def handler(ws: WebSocketRoute):  
  ws.on_message(lambda message: message_handler(ws, message))  
  
page.route_web_socket("/ws", handler)
```

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message == "request":  
    ws.send("response")  
  
def handler(ws: WebSocketRoute):  
  ws.on_message(lambda message: message_handler(ws, message))  
  
await page.route_web_socket("/ws", handler)
```

**Arguments**

* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool

  Only WebSockets with the url matching this pattern will be routed. A string pattern can be relative to the [base_url](Browser.md) context option.
* `handler` Callable[[WebSocketRoute](Websocketroute.md)]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any] | Any

  Handler function to route the WebSocket.

**Returns**

* NoneType

---

### screenshot[​](#page-screenshot "Direct link to screenshot")

Added before v1.9
page.screenshot

Returns the buffer with the captured screenshot.

**Usage**

```
page.screenshot()  
page.screenshot(**kwargs)
```

**Arguments**

* `animations` "disabled" | "allow" *(optional)*

  When set to `"disabled"`, stops CSS animations, CSS transitions and Web Animations. Animations get different treatment depending on their duration:

  + finite animations are fast-forwarded to completion, so they'll fire `transitionend` event.
  + infinite animations are canceled to initial state, and then played over after the screenshot.

  Defaults to `"allow"` that leaves animations untouched.
* `caret` "hide" | "initial" *(optional)*

  When set to `"hide"`, screenshot will hide text caret. When set to `"initial"`, text caret behavior will not be changed. Defaults to `"hide"`.
* `clip` Dict *(optional)*

  + `x` float

    x-coordinate of top-left corner of clip area
  + `y` float

    y-coordinate of top-left corner of clip area
  + `width` float

    width of clipping area
  + `height` float

    height of clipping area

  An object which specifies clipping of the resulting image.
* `full_page` bool *(optional)*

  When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Defaults to `false`.
* `mask` List[[Locator](Locator.md)] *(optional)*

  Specify locators that should be masked when the screenshot is taken. Masked elements will be overlaid with a pink box `#FF00FF` (customized by [mask_color](Page.md)) that completely covers its bounding box. The mask is also applied to invisible elements, see [Matching only visible elements](/python/docs/locators#matching-only-visible-elements) to disable that.
* `mask_color` str *(optional)* 

  Specify the color of the overlay box for masked elements, in [CSS color format](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value). Default color is pink `#FF00FF`.
* `omit_background` bool *(optional)*

  Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images. Defaults to `false`.
* `path` Union[str, pathlib.Path] *(optional)*

  The file path to save the image to. The screenshot type will be inferred from file extension. If [path](Page.md) is a relative path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to the disk.
* `quality` int *(optional)*

  The quality of the image, between 0-100. Not applicable to `png` images.
* `scale` "css" | "device" *(optional)*

  When set to `"css"`, screenshot will have a single pixel per each css pixel on the page. For high-dpi devices, this will keep screenshots small. Using `"device"` option will produce a single pixel per each device pixel, so screenshots of high-dpi devices will be twice as large or even larger.

  Defaults to `"device"`.
* `style` str *(optional)* 

  Text of the stylesheet to apply while making the screenshot. This is where you can hide dynamic elements, make elements invisible or change their properties to help you creating repeatable screenshots. This stylesheet pierces the Shadow DOM and applies to the inner frames.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `type` "png" | "jpeg" *(optional)*

  Specify screenshot type, defaults to `png`.

**Returns**

* bytes

---

### set_content[​](#page-set-content "Direct link to set_content")

Added before v1.9
page.set_content

This method internally calls [document.write()](https://developer.mozilla.org/en-US/docs/Web/API/Document/write), inheriting all its specific characteristics and behaviors.

**Usage**

```
page.set_content(html)  
page.set_content(html, **kwargs)
```

**Arguments**

* `html` str

  HTML markup to assign to the page.
* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.
* `wait_until` "load" | "domcontentloaded" | "networkidle" | "commit" *(optional)*

  When to consider operation succeeded, defaults to `load`. Events can be either:

  + `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
  + `'load'` - consider operation to be finished when the `load` event is fired.
  + `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
  + `'commit'` - consider operation to be finished when network response is received and the document started loading.

**Returns**

* NoneType

---

### set_default_navigation_timeout[​](#page-set-default-navigation-timeout "Direct link to set_default_navigation_timeout")

Added before v1.9
page.set_default_navigation_timeout

This setting will change the default maximum navigation time for the following methods and related shortcuts:

* [page.go_back()](Page.md)
* [page.go_forward()](Page.md)
* [page.goto()](Page.md)
* [page.reload()](Page.md)
* [page.set_content()](Page.md)
* [page.expect_navigation()](Page.md)
* [page.wait_for_url()](Page.md)

note

[page.set_default_navigation_timeout()](Page.md) takes priority over [page.set_default_timeout()](Page.md), [browser_context.set_default_timeout()](Browsercontext.md) and [browser_context.set_default_navigation_timeout()](Browsercontext.md).

**Usage**

```
page.set_default_navigation_timeout(timeout)
```

**Arguments**

* `timeout` float

  Maximum navigation time in milliseconds

---

### set_default_timeout[​](#page-set-default-timeout "Direct link to set_default_timeout")

Added before v1.9
page.set_default_timeout

This setting will change the default maximum time for all the methods accepting [timeout](Page.md) option.

note

[page.set_default_navigation_timeout()](Page.md) takes priority over [page.set_default_timeout()](Page.md).

**Usage**

```
page.set_default_timeout(timeout)
```

**Arguments**

* `timeout` float

  Maximum time in milliseconds. Pass `0` to disable timeout.

---

### set_extra_http_headers[​](#page-set-extra-http-headers "Direct link to set_extra_http_headers")

Added before v1.9
page.set_extra_http_headers

The extra HTTP headers will be sent with every request the page initiates.

note

[page.set_extra_http_headers()](Page.md) does not guarantee the order of headers in the outgoing requests.

**Usage**

```
page.set_extra_http_headers(headers)
```

**Arguments**

* `headers` Dict[str, str]

  An object containing additional HTTP headers to be sent with every request. All header values must be strings.

**Returns**

* NoneType

---

### set_viewport_size[​](#page-set-viewport-size "Direct link to set_viewport_size")

Added before v1.9
page.set_viewport_size

In the case of multiple pages in a single browser, each page can have its own viewport size. However, [browser.new_context()](Browser.md) allows to set viewport size (and more) for all pages in the context at once.

[page.set_viewport_size()](Page.md) will resize the page. A lot of websites don't expect phones to change size, so you should set the viewport size before navigating to the page. [page.set_viewport_size()](Page.md) will also reset `screen` size, use [browser.new_context()](Browser.md) with `screen` and `viewport` parameters if you need better control of these properties.

**Usage**

* Sync* Async

```
page = browser.new_page()  
page.set_viewport_size({"width": 640, "height": 480})  
page.goto("https://example.com")
```

```
page = await browser.new_page()  
await page.set_viewport_size({"width": 640, "height": 480})  
await page.goto("https://example.com")
```

**Arguments**

* `viewport_size` Dict
  + `width` int

    page width in pixels.
  + `height` int

    page height in pixels.

**Returns**

* NoneType

---

### title[​](#page-title "Direct link to title")

Added before v1.9
page.title

Returns the page's title.

**Usage**

```
page.title()
```

**Returns**

* str

---

### unroute[​](#page-unroute "Direct link to unroute")

Added before v1.9
page.unroute

Removes a route created with [page.route()](Page.md). When [handler](Page.md) is not specified, removes all routes for the [url](Page.md).

**Usage**

```
page.unroute(url)  
page.unroute(url, **kwargs)
```

**Arguments**

* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool

  A glob pattern, regex pattern or predicate receiving [URL](https://en.wikipedia.org/wiki/URL "URL") to match while routing.
* `handler` Callable[[Route](Route.md), [Request](Request.md)]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any] | Any *(optional)*

  Optional handler function to route the request.

**Returns**

* NoneType

---

### unroute_all[​](#page-unroute-all "Direct link to unroute_all") page.unroute_all

Removes all routes created with [page.route()](Page.md) and [page.route_from_har()](Page.md).

**Usage**

```
page.unroute_all()  
page.unroute_all(**kwargs)
```

**Arguments**

* `behavior` "wait" | "ignoreErrors" | "default" *(optional)*

  Specifies whether to wait for already running handlers and what to do if they throw errors:

  + `'default'` - do not wait for current handler calls (if any) to finish, if unrouted handler throws, it may result in unhandled error
  + `'wait'` - wait for current handler calls (if any) to finish
  + `'ignoreErrors'` - do not wait for current handler calls (if any) to finish, all errors thrown by the handlers after unrouting are silently caught

**Returns**

* NoneType

---

### wait_for_event[​](#page-wait-for-event-2 "Direct link to wait_for_event")

Added before v1.9
page.wait_for_event

note

In most cases, you should use [page.expect_event()](Page.md).

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function and waits for `predicate(event)` to return a truthy value. Will throw an error if the page is closed before the `event` is fired.

**Usage**

```
page.wait_for_event(event)  
page.wait_for_event(event, **kwargs)
```

**Arguments**

* `event` str

  Event name, same one typically passed into `*.on(event)`.
* `predicate` Callable *(optional)*

  Receives the event data and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* Any

---

### wait_for_function[​](#page-wait-for-function "Direct link to wait_for_function")

Added before v1.9
page.wait_for_function

Returns when the [expression](Page.md) returns a truthy value. It resolves to a JSHandle of the truthy value.

**Usage**

The [page.wait_for_function()](Page.md) can be used to observe viewport size change:

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = webkit.launch()  
    page = browser.new_page()  
    page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")  
    page.wait_for_function("() => window.x > 0")  
    browser.close()  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = await webkit.launch()  
    page = await browser.new_page()  
    await page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")  
    await page.wait_for_function("() => window.x > 0")  
    await browser.close()  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

To pass an argument to the predicate of [page.wait_for_function()](Page.md) function:

* Sync* Async

```
selector = ".foo"  
page.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

```
selector = ".foo"  
await page.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Page.md).
* `polling` float | "raf" *(optional)*

  If [polling](Page.md) is `'raf'`, then [expression](Page.md) is constantly executed in `requestAnimationFrame` callback. If [polling](Page.md) is a number, then it is treated as an interval in milliseconds at which the function would be executed. Defaults to `raf`.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* [JSHandle](Jshandle.md)

---

### wait_for_load_state[​](#page-wait-for-load-state "Direct link to wait_for_load_state")

Added before v1.9
page.wait_for_load_state

Returns when the required load state has been reached.

This resolves when the page reaches a required load state, `load` by default. The navigation must have been committed when this method is called. If current document has already reached the required state, resolves immediately.

note

Most of the time, this method is not needed because Playwright [auto-waits before every action](/python/docs/actionability).

**Usage**

* Sync* Async

```
page.get_by_role("button").click() # click triggers navigation.  
page.wait_for_load_state() # the promise resolves after "load" event.
```

```
await page.get_by_role("button").click() # click triggers navigation.  
await page.wait_for_load_state() # the promise resolves after "load" event.
```

* Sync* Async

```
with page.expect_popup() as page_info:  
    page.get_by_role("button").click() # click triggers a popup.  
popup = page_info.value  
# Wait for the "DOMContentLoaded" event.  
popup.wait_for_load_state("domcontentloaded")  
print(popup.title()) # popup is ready to use.
```

```
async with page.expect_popup() as page_info:  
    await page.get_by_role("button").click() # click triggers a popup.  
popup = await page_info.value  
# Wait for the "DOMContentLoaded" event.  
await popup.wait_for_load_state("domcontentloaded")  
print(await popup.title()) # popup is ready to use.
```

**Arguments**

* `state` "load" | "domcontentloaded" | "networkidle" *(optional)*

  Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current document, the method resolves immediately. Can be one of:

  + `'load'` - wait for the `load` event to be fired.
  + `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired.
  + `'networkidle'` - **DISCOURAGED** wait until there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### wait_for_url[​](#page-wait-for-url "Direct link to wait_for_url") page.wait_for_url

Waits for the main frame to navigate to the given URL.

**Usage**

* Sync* Async

```
page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation  
page.wait_for_url("**/target.html")
```

```
await page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation  
await page.wait_for_url("**/target.html")
```

**Arguments**

* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool

  A glob pattern, regex pattern or predicate receiving [URL](https://en.wikipedia.org/wiki/URL "URL") to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string.
* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.
* `wait_until` "load" | "domcontentloaded" | "networkidle" | "commit" *(optional)*

  When to consider operation succeeded, defaults to `load`. Events can be either:

  + `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
  + `'load'` - consider operation to be finished when the `load` event is fired.
  + `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
  + `'commit'` - consider operation to be finished when network response is received and the document started loading.

**Returns**

* NoneType

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### clock[​](#page-clock "Direct link to clock") page.clock

Playwright has ability to mock clock and passage of time.

**Usage**

```
page.clock
```

**Type**

* [Clock](Clock.md)

---

### context[​](#page-context "Direct link to context")

Added before v1.9
page.context

Get the browser context that the page belongs to.

**Usage**

```
page.context
```

**Returns**

* [BrowserContext](Browsercontext.md)

---

### frames[​](#page-frames "Direct link to frames")

Added before v1.9
page.frames

An array of all frames attached to the page.

**Usage**

```
page.frames
```

**Returns**

* List[[Frame](Frame.md)]

---

### is_closed[​](#page-is-closed "Direct link to is_closed")

Added before v1.9
page.is_closed

Indicates that the page has been closed.

**Usage**

```
page.is_closed()
```

**Returns**

* bool

---

### keyboard[​](#page-keyboard "Direct link to keyboard")

Added before v1.9
page.keyboard

**Usage**

```
page.keyboard
```

**Type**

* [Keyboard](Keyboard.md)

---

### main_frame[​](#page-main-frame "Direct link to main_frame")

Added before v1.9
page.main_frame

The page's main frame. Page is guaranteed to have a main frame which persists during navigations.

**Usage**

```
page.main_frame
```

**Returns**

* [Frame](Frame.md)

---

### mouse[​](#page-mouse "Direct link to mouse")

Added before v1.9
page.mouse

**Usage**

```
page.mouse
```

**Type**

* [Mouse](Mouse.md)

---

### request[​](#page-request "Direct link to request") page.request

API testing helper associated with this page. This method returns the same instance as [browser_context.request](Browsercontext.md) on the page's context. See [browser_context.request](Browsercontext.md) for more details.

**Usage**

```
page.request
```

**Type**

* [APIRequestContext](Apirequestcontext.md)

---

### touchscreen[​](#page-touchscreen "Direct link to touchscreen")

Added before v1.9
page.touchscreen

**Usage**

```
page.touchscreen
```

**Type**

* [Touchscreen](Touchscreen.md)

---

### url[​](#page-url "Direct link to url")

Added before v1.9
page.url

**Usage**

```
page.url
```

**Returns**

* str

---

### video[​](#page-video "Direct link to video")

Added before v1.9
page.video

Video object associated with this page.

**Usage**

```
page.video
```

**Returns**

* NoneType | [Video](Video.md)

---

### viewport_size[​](#page-viewport-size "Direct link to viewport_size")

Added before v1.9
page.viewport_size

**Usage**

```
page.viewport_size
```

**Returns**

* NoneType | Dict
  + `width` int

    page width in pixels.
  + `height` int

    page height in pixels.

---

### workers[​](#page-workers "Direct link to workers")

Added before v1.9
page.workers

This method returns all of the dedicated [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) associated with the page.

note

This does not contain ServiceWorkers

**Usage**

```
page.workers
```

**Returns**

* List[[Worker](Worker.md)]

---

Events[​](#events "Direct link to Events")
------------------------------------------

### on("close")[​](#page-event-close "Direct link to on(\"close\")")

Added before v1.9
page.on("close")

Emitted when the page closes.

**Usage**

```
page.on("close", handler)
```

**Event data**

* [Page](Page.md)

---

### on("console")[​](#page-event-console "Direct link to on(\"console\")")

Added before v1.9
page.on("console")

Emitted when JavaScript within the page calls one of console API methods, e.g. `console.log` or `console.dir`.

The arguments passed into `console.log` are available on the [ConsoleMessage](Consolemessage.md) event handler argument.

**Usage**

* Sync* Async

```
def print_args(msg):  
    for arg in msg.args:  
        print(arg.json_value())  
  
page.on("console", print_args)  
page.evaluate("console.log('hello', 5, { foo: 'bar' })")
```

```
async def print_args(msg):  
    values = []  
    for arg in msg.args:  
        values.append(await arg.json_value())  
    print(values)  
  
page.on("console", print_args)  
await page.evaluate("console.log('hello', 5, { foo: 'bar' })")
```

**Event data**

* [ConsoleMessage](Consolemessage.md)

---

### on("crash")[​](#page-event-crash "Direct link to on(\"crash\")")

Added before v1.9
page.on("crash")

Emitted when the page crashes. Browser pages might crash if they try to allocate too much memory. When the page crashes, ongoing and subsequent operations will throw.

The most common way to deal with crashes is to catch an exception:

* Sync* Async

```
try:  
    # crash might happen during a click.  
    page.click("button")  
    # or while waiting for an event.  
    page.wait_for_event("popup")  
except Error as e:  
    pass  
    # when the page crashes, exception message contains "crash".
```

```
try:  
    # crash might happen during a click.  
    await page.click("button")  
    # or while waiting for an event.  
    await page.wait_for_event("popup")  
except Error as e:  
    pass  
    # when the page crashes, exception message contains "crash".
```

**Usage**

```
page.on("crash", handler)
```

**Event data**

* [Page](Page.md)

---

### on("dialog")[​](#page-event-dialog "Direct link to on(\"dialog\")")

Added before v1.9
page.on("dialog")

Emitted when a JavaScript dialog appears, such as `alert`, `prompt`, `confirm` or `beforeunload`. Listener **must** either [dialog.accept()](Dialog.md) or [dialog.dismiss()](Dialog.md) the dialog - otherwise the page will [freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop#never_blocking) waiting for the dialog, and actions like click will never finish.

**Usage**

```
page.on("dialog", lambda dialog: dialog.accept())
```

note

When no [page.on("dialog")](Page.md) or [browser_context.on("dialog")](Browsercontext.md) listeners are present, all dialogs are automatically dismissed.

**Event data**

* [Dialog](Dialog.md)

---

### on("domcontentloaded")[​](#page-event-dom-content-loaded "Direct link to on(\"domcontentloaded\")") page.on("domcontentloaded")

Emitted when the JavaScript [`DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/Events/DOMContentLoaded) event is dispatched.

**Usage**

```
page.on("domcontentloaded", handler)
```

**Event data**

* [Page](Page.md)

---

### on("download")[​](#page-event-download "Direct link to on(\"download\")")

Added before v1.9
page.on("download")

Emitted when attachment download started. User can access basic file operations on downloaded content via the passed [Download](Download.md) instance.

**Usage**

```
page.on("download", handler)
```

**Event data**

* [Download](Download.md)

---

### on("filechooser")[​](#page-event-file-chooser "Direct link to on(\"filechooser\")") page.on("filechooser")

Emitted when a file chooser is supposed to appear, such as after clicking the `<input type=file>`. Playwright can respond to it via setting the input files using [file_chooser.set_files()](Filechooser.md) that can be uploaded after that.

```
page.on("filechooser", lambda file_chooser: file_chooser.set_files("/tmp/myfile.pdf"))
```

**Usage**

```
page.on("filechooser", handler)
```

**Event data**

* [FileChooser](Filechooser.md)

---

### on("frameattached")[​](#page-event-frame-attached "Direct link to on(\"frameattached\")") page.on("frameattached")

Emitted when a frame is attached.

**Usage**

```
page.on("frameattached", handler)
```

**Event data**

* [Frame](Frame.md)

---

### on("framedetached")[​](#page-event-frame-detached "Direct link to on(\"framedetached\")") page.on("framedetached")

Emitted when a frame is detached.

**Usage**

```
page.on("framedetached", handler)
```

**Event data**

* [Frame](Frame.md)

---

### on("framenavigated")[​](#page-event-frame-navigated "Direct link to on(\"framenavigated\")") page.on("framenavigated")

Emitted when a frame is navigated to a new url.

**Usage**

```
page.on("framenavigated", handler)
```

**Event data**

* [Frame](Frame.md)

---

### on("load")[​](#page-event-load "Direct link to on(\"load\")")

Added before v1.9
page.on("load")

Emitted when the JavaScript [`load`](https://developer.mozilla.org/en-US/docs/Web/Events/load) event is dispatched.

**Usage**

```
page.on("load", handler)
```

**Event data**

* [Page](Page.md)

---

### on("pageerror")[​](#page-event-page-error "Direct link to on(\"pageerror\")") page.on("pageerror")

Emitted when an uncaught exception happens within the page.

* Sync* Async

```
# Log all uncaught errors to the terminal  
page.on("pageerror", lambda exc: print(f"uncaught exception: {exc}"))  
  
# Navigate to a page with an exception.  
page.goto("data:text/html,<script>throw new Error('test')</script>")
```

```
# Log all uncaught errors to the terminal  
page.on("pageerror", lambda exc: print(f"uncaught exception: {exc}"))  
  
# Navigate to a page with an exception.  
await page.goto("data:text/html,<script>throw new Error('test')</script>")
```

**Usage**

```
page.on("pageerror", handler)
```

**Event data**

* [Error](Error.md)

---

### on("popup")[​](#page-event-popup "Direct link to on(\"popup\")")

Added before v1.9
page.on("popup")

Emitted when the page opens a new tab or window. This event is emitted in addition to the [browser_context.on("page")](Browsercontext.md), but only for popups relevant to this page.

The earliest moment that page is available is when it has navigated to the initial url. For example, when opening a popup with `window.open('http://example.com')`, this event will fire when the network request to "<http://example.com>" is done and its response has started loading in the popup. If you would like to route/listen to this network request, use [browser_context.route()](Browsercontext.md) and [browser_context.on("request")](Browsercontext.md) respectively instead of similar methods on the [Page](Page.md).

* Sync* Async

```
with page.expect_event("popup") as page_info:  
    page.get_by_text("open the popup").click()  
popup = page_info.value  
print(popup.evaluate("location.href"))
```

```
async with page.expect_event("popup") as page_info:  
    await page.get_by_text("open the popup").click()  
popup = await page_info.value  
print(await popup.evaluate("location.href"))
```

note

Use [page.wait_for_load_state()](Page.md) to wait until the page gets to a particular state (you should not need it in most cases).

**Usage**

```
page.on("popup", handler)
```

**Event data**

* [Page](Page.md)

---

### on("request")[​](#page-event-request "Direct link to on(\"request\")")

Added before v1.9
page.on("request")

Emitted when a page issues a request. The [request](Request.md) object is read-only. In order to intercept and mutate requests, see [page.route()](Page.md) or [browser_context.route()](Browsercontext.md).

**Usage**

```
page.on("request", handler)
```

**Event data**

* [Request](Request.md)

---

### on("requestfailed")[​](#page-event-request-failed "Direct link to on(\"requestfailed\")") page.on("requestfailed")

Emitted when a request fails, for example by timing out.

```
page.on("requestfailed", lambda request: print(request.url + " " + request.failure.error_text))
```

note

HTTP Error responses, such as 404 or 503, are still successful responses from HTTP standpoint, so request will complete with [page.on("requestfinished")](Page.md) event and not with [page.on("requestfailed")](Page.md). A request will only be considered failed when the client cannot get an HTTP response from the server, e.g. due to network error net::ERR_FAILED.

**Usage**

```
page.on("requestfailed", handler)
```

**Event data**

* [Request](Request.md)

---

### on("requestfinished")[​](#page-event-request-finished "Direct link to on(\"requestfinished\")") page.on("requestfinished")

Emitted when a request finishes successfully after downloading the response body. For a successful response, the sequence of events is `request`, `response` and `requestfinished`.

**Usage**

```
page.on("requestfinished", handler)
```

**Event data**

* [Request](Request.md)

---

### on("response")[​](#page-event-response "Direct link to on(\"response\")")

Added before v1.9
page.on("response")

Emitted when [response](Response.md) status and headers are received for a request. For a successful response, the sequence of events is `request`, `response` and `requestfinished`.

**Usage**

```
page.on("response", handler)
```

**Event data**

* [Response](Response.md)

---

### on("websocket")[​](#page-event-web-socket "Direct link to on(\"websocket\")") page.on("websocket")

Emitted when [WebSocket](Websocket.md) request is sent.

**Usage**

```
page.on("websocket", handler)
```

**Event data**

* [WebSocket](Websocket.md)

---

### on("worker")[​](#page-event-worker "Direct link to on(\"worker\")")

Added before v1.9
page.on("worker")

Emitted when a dedicated [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) is spawned by the page.

**Usage**

```
page.on("worker", handler)
```

**Event data**

* [Worker](Worker.md)

---

Deprecated[​](#deprecated "Direct link to Deprecated")
------------------------------------------------------

### check[​](#page-check "Direct link to check")

Added before v1.9
page.check

Discouraged

Use locator-based [locator.check()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method checks an element matching [selector](Page.md) by performing the following steps:

1. Find an element matching [selector](Page.md). If there is none, wait until a matching element is attached to the DOM.
2. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is already checked, this method returns immediately.
3. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Page.md) option is set. If the element is detached during the checks, the whole action is retried.
4. Scroll the element into view if needed.
5. Use [page.mouse](Page.md) to click in the center of the element.
6. Ensure that the element is now checked. If not, this method throws.

When all steps combined have not finished during the specified [timeout](Page.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
page.check(selector)  
page.check(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `position` Dict *(optional)* 

  + `x` float
  + `y` float

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### click[​](#page-click "Direct link to click")

Added before v1.9
page.click

Discouraged

Use locator-based [locator.click()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method clicks an element matching [selector](Page.md) by performing the following steps:

1. Find an element matching [selector](Page.md). If there is none, wait until a matching element is attached to the DOM.
2. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Page.md) option is set. If the element is detached during the checks, the whole action is retried.
3. Scroll the element into view if needed.
4. Use [page.mouse](Page.md) to click in the center of the element, or the specified [position](Page.md).
5. Wait for initiated navigations to either succeed or fail, unless [no_wait_after](Page.md) option is set.

When all steps combined have not finished during the specified [timeout](Page.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
page.click(selector)  
page.click(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `button` "left" | "right" | "middle" *(optional)*

  Defaults to `left`.
* `click_count` int *(optional)*

  defaults to 1. See [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail").
* `delay` float *(optional)*

  Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `modifiers` List["Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"] *(optional)*

  Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option will default to `true` in the future.

  Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`.
* `position` Dict *(optional)*

  + `x` float
  + `y` float

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

---

### dblclick[​](#page-dblclick "Direct link to dblclick")

Added before v1.9
page.dblclick

Discouraged

Use locator-based [locator.dblclick()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method double clicks an element matching [selector](Page.md) by performing the following steps:

1. Find an element matching [selector](Page.md). If there is none, wait until a matching element is attached to the DOM.
2. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Page.md) option is set. If the element is detached during the checks, the whole action is retried.
3. Scroll the element into view if needed.
4. Use [page.mouse](Page.md) to double click in the center of the element, or the specified [position](Page.md).

When all steps combined have not finished during the specified [timeout](Page.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

note

`page.dblclick()` dispatches two `click` events and a single `dblclick` event.

**Usage**

```
page.dblclick(selector)  
page.dblclick(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `button` "left" | "right" | "middle" *(optional)*

  Defaults to `left`.
* `delay` float *(optional)*

  Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `modifiers` List["Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"] *(optional)*

  Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `position` Dict *(optional)*

  + `x` float
  + `y` float

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

---

### dispatch_event[​](#page-dispatch-event "Direct link to dispatch_event")

Added before v1.9
page.dispatch_event

Discouraged

Use locator-based [locator.dispatch_event()](Locator.md) instead. Read more about [locators](/python/docs/locators).

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element, `click` is dispatched. This is equivalent to calling [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

* Sync* Async

```
page.dispatch_event("button#submit", "click")
```

```
await page.dispatch_event("button#submit", "click")
```

Under the hood, it creates an instance of an event based on the given [type](Page.md), initializes it with [event_init](Page.md) properties and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

Since [event_init](Page.md) is event-specific, please refer to the events documentation for the lists of initial properties:

* [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/DeviceMotionEvent)
* [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/DeviceOrientationEvent)
* [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
* [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)
* [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
* [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
* [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
* [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
* [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
* [WheelEvent](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/WheelEvent)

You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

* Sync* Async

```
# note you can only create data_transfer in chromium and firefox  
data_transfer = page.evaluate_handle("new DataTransfer()")  
page.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

```
# note you can only create data_transfer in chromium and firefox  
data_transfer = await page.evaluate_handle("new DataTransfer()")  
await page.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `type` str

  DOM event type: `"click"`, `"dragstart"`, etc.
* `event_init` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional event-specific initialization properties.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### eval_on_selector[​](#page-eval-on-selector "Direct link to eval_on_selector") page.eval_on_selector

Discouraged

This method does not wait for the element to pass actionability checks and therefore can lead to the flaky tests. Use [locator.evaluate()](Locator.md), other [Locator](Locator.md) helper methods or web-first assertions instead.

The method finds an element matching the specified selector within the page and passes it as a first argument to [expression](Page.md). If no elements match the selector, the method throws an error. Returns the value of [expression](Page.md).

If [expression](Page.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [page.eval_on_selector()](Page.md) would wait for the promise to resolve and return its value.

**Usage**

* Sync* Async

```
search_value = page.eval_on_selector("#search", "el => el.value")  
preload_href = page.eval_on_selector("link[rel=preload]", "el => el.href")  
html = page.eval_on_selector(".main-container", "(e, suffix) => e.outer_html + suffix", "hello")
```

```
search_value = await page.eval_on_selector("#search", "el => el.value")  
preload_href = await page.eval_on_selector("link[rel=preload]", "el => el.href")  
html = await page.eval_on_selector(".main-container", "(e, suffix) => e.outer_html + suffix", "hello")
```

**Arguments**

* `selector` str

  A selector to query for.
* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Page.md).
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

**Returns**

* Dict

---

### eval_on_selector_all[​](#page-eval-on-selector-all "Direct link to eval_on_selector_all") page.eval_on_selector_all

Discouraged

In most cases, [locator.evaluate_all()](Locator.md), other [Locator](Locator.md) helper methods and web-first assertions do a better job.

The method finds all elements matching the specified selector within the page and passes an array of matched elements as a first argument to [expression](Page.md). Returns the result of [expression](Page.md) invocation.

If [expression](Page.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [page.eval_on_selector_all()](Page.md) would wait for the promise to resolve and return its value.

**Usage**

* Sync* Async

```
div_counts = page.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
```

```
div_counts = await page.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
```

**Arguments**

* `selector` str

  A selector to query for.
* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Page.md).

**Returns**

* Dict

---

### expect_navigation[​](#page-wait-for-navigation "Direct link to expect_navigation")

Added before v1.9
page.expect_navigation

Deprecated

This method is inherently racy, please use [page.wait_for_url()](Page.md) instead.

Waits for the main frame navigation and returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or navigation due to History API usage, the navigation will resolve with `null`.

**Usage**

This resolves when the page navigates to a new URL or reloads. It is useful for when you run code which will indirectly cause the page to navigate. e.g. The click target has an `onclick` handler that triggers navigation from a `setTimeout`. Consider this example:

* Sync* Async

```
with page.expect_navigation():  
    # This action triggers the navigation after a timeout.  
    page.get_by_text("Navigate after timeout").click()  
# Resolves after navigation has finished
```

```
async with page.expect_navigation():  
    # This action triggers the navigation after a timeout.  
    await page.get_by_text("Navigate after timeout").click()  
# Resolves after navigation has finished
```

note

Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL is considered a navigation.

**Arguments**

* `timeout` float *(optional)*

  Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_navigation_timeout()](Browsercontext.md), [browser_context.set_default_timeout()](Browsercontext.md), [page.set_default_navigation_timeout()](Page.md) or [page.set_default_timeout()](Page.md) methods.
* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool *(optional)*

  A glob pattern, regex pattern or predicate receiving [URL](https://en.wikipedia.org/wiki/URL "URL") to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string.
* `wait_until` "load" | "domcontentloaded" | "networkidle" | "commit" *(optional)*

  When to consider operation succeeded, defaults to `load`. Events can be either:

  + `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
  + `'load'` - consider operation to be finished when the `load` event is fired.
  + `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
  + `'commit'` - consider operation to be finished when network response is received and the document started loading.

**Returns**

* EventContextManager[[Response](Response.md)]

---

### fill[​](#page-fill "Direct link to fill")

Added before v1.9
page.fill

Discouraged

Use locator-based [locator.fill()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method waits for an element matching [selector](Page.md), waits for [actionability](/python/docs/actionability) checks, focuses the element, fills it and triggers an `input` event after filling. Note that you can pass an empty string to clear the input field.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled instead.

To send fine-grained keyboard events, use [locator.press_sequentially()](Locator.md).

**Usage**

```
page.fill(selector, value)  
page.fill(selector, value, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `value` str

  Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element.
* `force` bool *(optional)* 

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### focus[​](#page-focus "Direct link to focus")

Added before v1.9
page.focus

Discouraged

Use locator-based [locator.focus()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method fetches an element with [selector](Page.md) and focuses it. If there's no element matching [selector](Page.md), the method waits until a matching element appears in the DOM.

**Usage**

```
page.focus(selector)  
page.focus(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### get_attribute[​](#page-get-attribute "Direct link to get_attribute")

Added before v1.9
page.get_attribute

Discouraged

Use locator-based [locator.get_attribute()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns element attribute value.

**Usage**

```
page.get_attribute(selector, name)  
page.get_attribute(selector, name, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `name` str

  Attribute name to get the value for.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType | str

---

### hover[​](#page-hover "Direct link to hover")

Added before v1.9
page.hover

Discouraged

Use locator-based [locator.hover()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method hovers over an element matching [selector](Page.md) by performing the following steps:

1. Find an element matching [selector](Page.md). If there is none, wait until a matching element is attached to the DOM.
2. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Page.md) option is set. If the element is detached during the checks, the whole action is retried.
3. Scroll the element into view if needed.
4. Use [page.mouse](Page.md) to hover over the center of the element, or the specified [position](Page.md).

When all steps combined have not finished during the specified [timeout](Page.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
page.hover(selector)  
page.hover(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `modifiers` List["Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"] *(optional)*

  Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
* `no_wait_after` bool *(optional)* 

  Deprecated

  This option has no effect.

  This option has no effect.
* `position` Dict *(optional)*

  + `x` float
  + `y` float

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

---

### inner_html[​](#page-inner-html "Direct link to inner_html")

Added before v1.9
page.inner_html

Discouraged

Use locator-based [locator.inner_html()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns `element.innerHTML`.

**Usage**

```
page.inner_html(selector)  
page.inner_html(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

---

### inner_text[​](#page-inner-text "Direct link to inner_text")

Added before v1.9
page.inner_text

Discouraged

Use locator-based [locator.inner_text()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns `element.innerText`.

**Usage**

```
page.inner_text(selector)  
page.inner_text(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

---

### input_value[​](#page-input-value "Direct link to input_value") page.input_value

Discouraged

Use locator-based [locator.input_value()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns `input.value` for the selected `<input>` or `<textarea>` or `<select>` element.

Throws for non-input elements. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the control.

**Usage**

```
page.input_value(selector)  
page.input_value(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

---

### is_checked[​](#page-is-checked "Direct link to is_checked")

Added before v1.9
page.is_checked

Discouraged

Use locator-based [locator.is_checked()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

**Usage**

```
page.is_checked(selector)  
page.is_checked(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_disabled[​](#page-is-disabled "Direct link to is_disabled")

Added before v1.9
page.is_disabled

Discouraged

Use locator-based [locator.is_disabled()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is disabled, the opposite of [enabled](/python/docs/actionability#enabled).

**Usage**

```
page.is_disabled(selector)  
page.is_disabled(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_editable[​](#page-is-editable "Direct link to is_editable")

Added before v1.9
page.is_editable

Discouraged

Use locator-based [locator.is_editable()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is [editable](/python/docs/actionability#editable).

**Usage**

```
page.is_editable(selector)  
page.is_editable(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_enabled[​](#page-is-enabled "Direct link to is_enabled")

Added before v1.9
page.is_enabled

Discouraged

Use locator-based [locator.is_enabled()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is [enabled](/python/docs/actionability#enabled).

**Usage**

```
page.is_enabled(selector)  
page.is_enabled(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_hidden[​](#page-is-hidden "Direct link to is_hidden")

Added before v1.9
page.is_hidden

Discouraged

Use locator-based [locator.is_hidden()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is hidden, the opposite of [visible](/python/docs/actionability#visible). [selector](Page.md) that does not match any elements is considered hidden.

**Usage**

```
page.is_hidden(selector)  
page.is_hidden(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Deprecated

  This option is ignored. [page.is_hidden()](Page.md) does not wait for the element to become hidden and returns immediately.

**Returns**

* bool

---

### is_visible[​](#page-is-visible "Direct link to is_visible")

Added before v1.9
page.is_visible

Discouraged

Use locator-based [locator.is_visible()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is [visible](/python/docs/actionability#visible). [selector](Page.md) that does not match any elements is considered not visible.

**Usage**

```
page.is_visible(selector)  
page.is_visible(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Deprecated

  This option is ignored. [page.is_visible()](Page.md) does not wait for the element to become visible and returns immediately.

**Returns**

* bool

---

### press[​](#page-press "Direct link to press")

Added before v1.9
page.press

Discouraged

Use locator-based [locator.press()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Focuses the element, and then uses [keyboard.down()](Keyboard.md) and [keyboard.up()](Keyboard.md).

[key](Page.md) can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character to generate the text for. A superset of the [key](Page.md) values can be found [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the [key](Page.md) in the upper case.

If [key](Page.md) is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

**Usage**

* Sync* Async

```
page = browser.new_page()  
page.goto("https://keycode.info")  
page.press("body", "A")  
page.screenshot(path="a.png")  
page.press("body", "ArrowLeft")  
page.screenshot(path="arrow_left.png")  
page.press("body", "Shift+O")  
page.screenshot(path="o.png")  
browser.close()
```

```
page = await browser.new_page()  
await page.goto("https://keycode.info")  
await page.press("body", "A")  
await page.screenshot(path="a.png")  
await page.press("body", "ArrowLeft")  
await page.screenshot(path="arrow_left.png")  
await page.press("body", "Shift+O")  
await page.screenshot(path="o.png")  
await browser.close()
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `key` str

  Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
* `delay` float *(optional)*

  Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option will default to `true` in the future.

  Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### query_selector[​](#page-query-selector "Direct link to query_selector") page.query_selector

Discouraged

Use locator-based [page.locator()](Page.md) instead. Read more about [locators](/python/docs/locators).

The method finds an element matching the specified selector within the page. If no elements match the selector, the return value resolves to `null`. To wait for an element on the page, use [locator.wait_for()](Locator.md).

**Usage**

```
page.query_selector(selector)  
page.query_selector(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to query for.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

**Returns**

* NoneType | [ElementHandle](Elementhandle.md)

---

### query_selector_all[​](#page-query-selector-all "Direct link to query_selector_all") page.query_selector_all

Discouraged

Use locator-based [page.locator()](Page.md) instead. Read more about [locators](/python/docs/locators).

The method finds all elements matching the specified selector within the page. If no elements match the selector, the return value resolves to `[]`.

**Usage**

```
page.query_selector_all(selector)
```

**Arguments**

* `selector` str

  A selector to query for.

**Returns**

* List[[ElementHandle](Elementhandle.md)]

---

### select_option[​](#page-select-option "Direct link to select_option")

Added before v1.9
page.select_option

Discouraged

Use locator-based [locator.select_option()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method waits for an element matching [selector](Page.md), waits for [actionability](/python/docs/actionability) checks, waits until all specified options are present in the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

* Sync* Async

```
# Single selection matching the value or label  
page.select_option("select#colors", "blue")  
# single selection matching both the label  
page.select_option("select#colors", label="blue")  
# multiple selection  
page.select_option("select#colors", value=["red", "green", "blue"])
```

```
# Single selection matching the value or label  
await page.select_option("select#colors", "blue")  
# single selection matching the label  
await page.select_option("select#colors", label="blue")  
# multiple selection  
await page.select_option("select#colors", value=["red", "green", "blue"])
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `force` bool *(optional)* 

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `element` [ElementHandle](Elementhandle.md) | List[[ElementHandle](Elementhandle.md)] *(optional)*

  Option elements to select. Optional.
* `index` int | List[int] *(optional)*

  Options to select by index. Optional.
* `value` str | List[str] *(optional)*

  Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional.
* `label` str | List[str] *(optional)*

  Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional.

**Returns**

* List[str]

---

### set_checked[​](#page-set-checked "Direct link to set_checked") page.set_checked

Discouraged

Use locator-based [locator.set_checked()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method checks or unchecks an element matching [selector](Page.md) by performing the following steps:

1. Find an element matching [selector](Page.md). If there is none, wait until a matching element is attached to the DOM.
2. Ensure that matched element is a checkbox or a radio input. If not, this method throws.
3. If the element already has the right checked state, this method returns immediately.
4. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Page.md) option is set. If the element is detached during the checks, the whole action is retried.
5. Scroll the element into view if needed.
6. Use [page.mouse](Page.md) to click in the center of the element.
7. Ensure that the element is now checked or unchecked. If not, this method throws.

When all steps combined have not finished during the specified [timeout](Page.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
page.set_checked(selector, checked)  
page.set_checked(selector, checked, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `checked` bool

  Whether to check or uncheck the checkbox.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `position` Dict *(optional)*

  + `x` float
  + `y` float

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.
* `strict` bool *(optional)*

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)*

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### set_input_files[​](#page-set-input-files "Direct link to set_input_files")

Added before v1.9
page.set_input_files

Discouraged

Use locator-based [locator.set_input_files()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they are resolved relative to the current working directory. For empty array, clears the selected files. For inputs with a `[webkitdirectory]` attribute, only a single directory path is supported.

This method expects [selector](Page.md) to point to an [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

**Usage**

```
page.set_input_files(selector, files)  
page.set_input_files(selector, files, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `files` Union[str, pathlib.Path] | List[Union[str, pathlib.Path]] | Dict | List[Dict]

  + `name` str

    File name
  + `mimeType` str

    File type
  + `buffer` bytes

    File content
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### tap[​](#page-tap "Direct link to tap")

Added before v1.9
page.tap

Discouraged

Use locator-based [locator.tap()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method taps an element matching [selector](Page.md) by performing the following steps:

1. Find an element matching [selector](Page.md). If there is none, wait until a matching element is attached to the DOM.
2. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Page.md) option is set. If the element is detached during the checks, the whole action is retried.
3. Scroll the element into view if needed.
4. Use [page.touchscreen](Page.md) to tap the center of the element, or the specified [position](Page.md).

When all steps combined have not finished during the specified [timeout](Page.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

note

[page.tap()](Page.md) the method will throw if [has_touch](Browser.md) option of the browser context is false.

**Usage**

```
page.tap(selector)  
page.tap(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `modifiers` List["Alt" | "Control" | "ControlOrMeta" | "Meta" | "Shift"] *(optional)*

  Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `position` Dict *(optional)*

  + `x` float
  + `y` float

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

---

### text_content[​](#page-text-content "Direct link to text_content")

Added before v1.9
page.text_content

Discouraged

Use locator-based [locator.text_content()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns `element.textContent`.

**Usage**

```
page.text_content(selector)  
page.text_content(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType | str

---

### type[​](#page-type "Direct link to type")

Added before v1.9
page.type

Deprecated

In most cases, you should use [locator.fill()](Locator.md) instead. You only need to press keys one by one if there is special keyboard handling on the page - in this case use [locator.press_sequentially()](Locator.md).

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `page.type` can be used to send fine-grained keyboard events. To fill values in form fields, use [page.fill()](Page.md).

To press a special key, like `Control` or `ArrowDown`, use [keyboard.press()](Keyboard.md).

**Usage**

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `text` str

  A text to type into a focused element.
* `delay` float *(optional)*

  Time to wait between key presses in milliseconds. Defaults to 0.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### uncheck[​](#page-uncheck "Direct link to uncheck")

Added before v1.9
page.uncheck

Discouraged

Use locator-based [locator.uncheck()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method unchecks an element matching [selector](Page.md) by performing the following steps:

1. Find an element matching [selector](Page.md). If there is none, wait until a matching element is attached to the DOM.
2. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is already unchecked, this method returns immediately.
3. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Page.md) option is set. If the element is detached during the checks, the whole action is retried.
4. Scroll the element into view if needed.
5. Use [page.mouse](Page.md) to click in the center of the element.
6. Ensure that the element is now unchecked. If not, this method throws.

When all steps combined have not finished during the specified [timeout](Page.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
page.uncheck(selector)  
page.uncheck(selector, **kwargs)
```

**Arguments**

* `selector` str

  A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.
* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `position` Dict *(optional)* 

  + `x` float
  + `y` float

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### wait_for_selector[​](#page-wait-for-selector "Direct link to wait_for_selector")

Added before v1.9
page.wait_for_selector

Discouraged

Use web assertions that assert visibility or a locator-based [locator.wait_for()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns when element specified by selector satisfies [state](Page.md) option. Returns `null` if waiting for `hidden` or `detached`.

note

Playwright automatically waits for element to be ready before performing an action. Using [Locator](Locator.md) objects and web-first assertions makes the code wait-for-selector-free.

Wait for the [selector](Page.md) to satisfy [state](Page.md) option (either appear/disappear from dom, or become visible/hidden). If at the moment of calling the method [selector](Page.md) already satisfies the condition, the method will return immediately. If the selector doesn't satisfy the condition for the [timeout](Page.md) milliseconds, the function will throw.

**Usage**

This method works across navigations:

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
    chromium = playwright.chromium  
    browser = chromium.launch()  
    page = browser.new_page()  
    for current_url in ["https://google.com", "https://bbc.com"]:  
        page.goto(current_url, wait_until="domcontentloaded")  
        element = page.wait_for_selector("img")  
        print("Loaded image: " + str(element.get_attribute("src")))  
    browser.close()  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def run(playwright: Playwright):  
    chromium = playwright.chromium  
    browser = await chromium.launch()  
    page = await browser.new_page()  
    for current_url in ["https://google.com", "https://bbc.com"]:  
        await page.goto(current_url, wait_until="domcontentloaded")  
        element = await page.wait_for_selector("img")  
        print("Loaded image: " + str(await element.get_attribute("src")))  
    await browser.close()  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
asyncio.run(main())
```

**Arguments**

* `selector` str

  A selector to query for.
* `state` "attached" | "detached" | "visible" | "hidden" *(optional)*

  Defaults to `'visible'`. Can be either:

  + `'attached'` - wait for element to be present in DOM.
  + `'detached'` - wait for element to not be present in DOM.
  + `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without any content or with `display:none` has an empty bounding box and is not considered visible.
  + `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`. This is opposite to the `'visible'` option.
* `strict` bool *(optional)* 

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType | [ElementHandle](Elementhandle.md)

---

### wait_for_timeout[​](#page-wait-for-timeout "Direct link to wait_for_timeout")

Added before v1.9
page.wait_for_timeout

Discouraged

Never wait for timeout in production. Tests that wait for time are inherently flaky. Use [Locator](Locator.md) actions and web assertions that wait automatically.

Waits for the given [timeout](Page.md) in milliseconds.

Note that `page.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going to be flaky. Use signals such as network events, selectors becoming visible and others instead.

**Usage**

* Sync* Async

```
# wait for 1 second  
page.wait_for_timeout(1000)
```

```
# wait for 1 second  
await page.wait_for_timeout(1000)
```

**Arguments**

* `timeout` float

  A timeout to wait for

**Returns**

* NoneType
