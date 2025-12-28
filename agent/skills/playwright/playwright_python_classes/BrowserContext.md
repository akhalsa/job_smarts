# BrowserContext

Source: https://playwright.dev/python/docs/api/class-browsercontext

---

BrowserContexts provide a way to operate multiple independent browser sessions.

If a page opens another page, e.g. with a `window.open` call, the popup will belong to the parent page's browser context.

Playwright allows creating isolated non-persistent browser contexts with [browser.new_context()](Browser.md) method. Non-persistent browser contexts don't write any browsing data to disk.

* Sync* Async

```
# create a new incognito browser context  
context = browser.new_context()  
# create a new page inside context.  
page = context.new_page()  
page.goto("https://example.com")  
# dispose context once it is no longer needed.  
context.close()
```

```
# create a new incognito browser context  
context = await browser.new_context()  
# create a new page inside context.  
page = await context.new_page()  
await page.goto("https://example.com")  
# dispose context once it is no longer needed.  
await context.close()
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### add_cookies[​](#browser-context-add-cookies "Direct link to add_cookies")

Added before v1.9
browserContext.add_cookies

Adds cookies into this browser context. All pages within this context will have these cookies installed. Cookies can be obtained via [browser_context.cookies()](Browsercontext.md).

**Usage**

* Sync* Async

```
browser_context.add_cookies([cookie_object1, cookie_object2])
```

```
await browser_context.add_cookies([cookie_object1, cookie_object2])
```

**Arguments**

* `cookies` List[Dict]
  + `name` str
  + `value` str
  + `url` str *(optional)*

    Either `url` or both `domain` and `path` are required. Optional.
  + `domain` str *(optional)*

    For the cookie to apply to all subdomains as well, prefix domain with a dot, like this: ".example.com". Either `url` or both `domain` and `path` are required. Optional.
  + `path` str *(optional)*

    Either `url` or both `domain` and `path` are required. Optional.
  + `expires` float *(optional)*

    Unix time in seconds. Optional.
  + `httpOnly` bool *(optional)*

    Optional.
  + `secure` bool *(optional)*

    Optional.
  + `sameSite` "Strict" | "Lax" | "None" *(optional)*

    Optional.
  + `partitionKey` str *(optional)*

    For partitioned third-party cookies (aka [CHIPS](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Privacy_sandbox/Partitioned_cookies)), the partition key. Optional.

**Returns**

* NoneType

---

### add_init_script[​](#browser-context-add-init-script "Direct link to add_init_script")

Added before v1.9
browserContext.add_init_script

Adds a script which would be evaluated in one of the following scenarios:

* Whenever a page is created in the browser context or is navigated.
* Whenever a child frame is attached or navigated in any page in the browser context. In this case, the script is evaluated in the context of the newly attached frame.

The script is evaluated after the document was created but before any of its scripts were run. This is useful to amend the JavaScript environment, e.g. to seed `Math.random`.

**Usage**

An example of overriding `Math.random` before the page loads:

```
// preload.js  
Math.random = () => 42;
```

* Sync* Async

```
# in your playwright script, assuming the preload.js file is in same directory.  
browser_context.add_init_script(path="preload.js")
```

```
# in your playwright script, assuming the preload.js file is in same directory.  
await browser_context.add_init_script(path="preload.js")
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

### clear_cookies[​](#browser-context-clear-cookies "Direct link to clear_cookies")

Added before v1.9
browserContext.clear_cookies

Removes cookies from context. Accepts optional filter.

**Usage**

* Sync* Async

```
context.clear_cookies()  
context.clear_cookies(name="session-id")  
context.clear_cookies(domain="my-origin.com")  
context.clear_cookies(path="/api/v1")  
context.clear_cookies(name="session-id", domain="my-origin.com")
```

```
await context.clear_cookies()  
await context.clear_cookies(name="session-id")  
await context.clear_cookies(domain="my-origin.com")  
await context.clear_cookies(path="/api/v1")  
await context.clear_cookies(name="session-id", domain="my-origin.com")
```

**Arguments**

* `domain` str | Pattern *(optional)* 

  Only removes cookies with the given domain.
* `name` str | Pattern *(optional)* 

  Only removes cookies with the given name.
* `path` str | Pattern *(optional)* 

  Only removes cookies with the given path.

**Returns**

* NoneType

---

### clear_permissions[​](#browser-context-clear-permissions "Direct link to clear_permissions")

Added before v1.9
browserContext.clear_permissions

Clears all permission overrides for the browser context.

**Usage**

* Sync* Async

```
context = browser.new_context()  
context.grant_permissions(["clipboard-read"])  
# do stuff ..  
context.clear_permissions()
```

```
context = await browser.new_context()  
await context.grant_permissions(["clipboard-read"])  
# do stuff ..  
context.clear_permissions()
```

**Returns**

* NoneType

---

### close[​](#browser-context-close "Direct link to close")

Added before v1.9
browserContext.close

Closes the browser context. All the pages that belong to the browser context will be closed.

note

The default browser context cannot be closed.

**Usage**

```
browser_context.close()  
browser_context.close(**kwargs)
```

**Arguments**

* `reason` str *(optional)* 

  The reason to be reported to the operations interrupted by the context closure.

**Returns**

* NoneType

---

### cookies[​](#browser-context-cookies "Direct link to cookies")

Added before v1.9
browserContext.cookies

If no URLs are specified, this method returns all cookies. If URLs are specified, only cookies that affect those URLs are returned.

**Usage**

```
browser_context.cookies()  
browser_context.cookies(**kwargs)
```

**Arguments**

* `urls` str | List[str] *(optional)*

  Optional list of URLs.

**Returns**

* List[Dict]
  + `name` str
  + `value` str
  + `domain` str
  + `path` str
  + `expires` float

    Unix time in seconds.
  + `httpOnly` bool
  + `secure` bool
  + `sameSite` "Strict" | "Lax" | "None"
  + `partitionKey` str *(optional)*

---

### expect_console_message[​](#browser-context-wait-for-console-message "Direct link to expect_console_message") browserContext.expect_console_message

Performs action and waits for a [ConsoleMessage](Consolemessage.md) to be logged by in the pages in the context. If predicate is provided, it passes [ConsoleMessage](Consolemessage.md) value into the `predicate` function and waits for `predicate(message)` to return a truthy value. Will throw an error if the page is closed before the [browser_context.on("console")](Browsercontext.md) event is fired.

**Usage**

```
browser_context.expect_console_message()  
browser_context.expect_console_message(**kwargs)
```

**Arguments**

* `predicate` Callable[[ConsoleMessage](Consolemessage.md)]:bool *(optional)*

  Receives the [ConsoleMessage](Consolemessage.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[ConsoleMessage](Consolemessage.md)]

---

### expect_event[​](#browser-context-wait-for-event "Direct link to expect_event")

Added before v1.9
browserContext.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy value. Will throw an error if the context closes before the event is fired. Returns the event data value.

**Usage**

* Sync* Async

```
with context.expect_event("page") as event_info:  
    page.get_by_role("button").click()  
page = event_info.value
```

```
async with context.expect_event("page") as event_info:  
    await page.get_by_role("button").click()  
page = await event_info.value
```

**Arguments**

* `event` str

  Event name, same one would pass into `browserContext.on(event)`.
* `predicate` Callable *(optional)*

  Receives the event data and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager

---

### expect_page[​](#browser-context-wait-for-page "Direct link to expect_page") browserContext.expect_page

Performs action and waits for a new [Page](Page.md) to be created in the context. If predicate is provided, it passes [Page](Page.md) value into the `predicate` function and waits for `predicate(event)` to return a truthy value. Will throw an error if the context closes before new [Page](Page.md) is created.

**Usage**

```
browser_context.expect_page()  
browser_context.expect_page(**kwargs)
```

**Arguments**

* `predicate` Callable[[Page](Page.md)]:bool *(optional)*

  Receives the [Page](Page.md) object and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager[[Page](Page.md)]

---

### expose_binding[​](#browser-context-expose-binding "Direct link to expose_binding")

Added before v1.9
browserContext.expose_binding

The method adds a function called [name](Browsercontext.md) on the `window` object of every frame in every page in the context. When called, the function executes [callback](Browsercontext.md) and returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise") which resolves to the return value of [callback](Browsercontext.md). If the [callback](Browsercontext.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), it will be awaited.

The first argument of the [callback](Browsercontext.md) function contains information about the caller: `{ browserContext: BrowserContext, page: Page, frame: Frame }`.

See [page.expose_binding()](Page.md) for page-only version.

**Usage**

An example of exposing page URL to all frames in all pages in the context:

* Sync* Async

```
from playwright.sync_api import sync_playwright, Playwright  
  
def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = webkit.launch(headless=False)  
    context = browser.new_context()  
    context.expose_binding("pageURL", lambda source: source["page"].url)  
    page = context.new_page()  
    page.set_content("""  
    <script>  
      async function onClick() {  
        document.querySelector('div').textContent = await window.pageURL();  
      }  
    </script>  
    <button onclick="onClick()">Click me</button>  
    <div></div>  
    """)  
    page.get_by_role("button").click()  
  
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
    await context.expose_binding("pageURL", lambda source: source["page"].url)  
    page = await context.new_page()  
    await page.set_content("""  
    <script>  
      async function onClick() {  
        document.querySelector('div').textContent = await window.pageURL();  
      }  
    </script>  
    <button onclick="onClick()">Click me</button>  
    <div></div>  
    """)  
    await page.get_by_role("button").click()  
  
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

### expose_function[​](#browser-context-expose-function "Direct link to expose_function")

Added before v1.9
browserContext.expose_function

The method adds a function called [name](Browsercontext.md) on the `window` object of every frame in every page in the context. When called, the function executes [callback](Browsercontext.md) and returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise") which resolves to the return value of [callback](Browsercontext.md).

If the [callback](Browsercontext.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), it will be awaited.

See [page.expose_function()](Page.md) for page-only version.

**Usage**

An example of adding a `sha256` function to all pages in the context:

* Sync* Async

```
import hashlib  
from playwright.sync_api import sync_playwright  
  
def sha256(text: str) -> str:  
    m = hashlib.sha256()  
    m.update(bytes(text, "utf8"))  
    return m.hexdigest()  
  
  
def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = webkit.launch(headless=False)  
    context = browser.new_context()  
    context.expose_function("sha256", sha256)  
    page = context.new_page()  
    page.set_content("""  
        <script>  
          async function onClick() {  
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');  
          }  
        </script>  
        <button onclick="onClick()">Click me</button>  
        <div></div>  
    """)  
    page.get_by_role("button").click()  
  
with sync_playwright() as playwright:  
    run(playwright)
```

```
import asyncio  
import hashlib  
from playwright.async_api import async_playwright, Playwright  
  
def sha256(text: str) -> str:  
    m = hashlib.sha256()  
    m.update(bytes(text, "utf8"))  
    return m.hexdigest()  
  
  
async def run(playwright: Playwright):  
    webkit = playwright.webkit  
    browser = await webkit.launch(headless=False)  
    context = await browser.new_context()  
    await context.expose_function("sha256", sha256)  
    page = await context.new_page()  
    await page.set_content("""  
        <script>  
          async function onClick() {  
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');  
          }  
        </script>  
        <button onclick="onClick()">Click me</button>  
        <div></div>  
    """)  
    await page.get_by_role("button").click()  
  
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

**Returns**

* NoneType

---

### grant_permissions[​](#browser-context-grant-permissions "Direct link to grant_permissions")

Added before v1.9
browserContext.grant_permissions

Grants specified permissions to the browser context. Only grants corresponding permissions to the given origin if specified.

**Usage**

```
browser_context.grant_permissions(permissions)  
browser_context.grant_permissions(permissions, **kwargs)
```

**Arguments**

* `permissions` List[str]

  A list of permissions to grant.

  danger

  Supported permissions differ between browsers, and even between different versions of the same browser. Any permission may stop working after an update.

  Here are some permissions that may be supported by some browsers:

  + `'accelerometer'`
  + `'ambient-light-sensor'`
  + `'background-sync'`
  + `'camera'`
  + `'clipboard-read'`
  + `'clipboard-write'`
  + `'geolocation'`
  + `'gyroscope'`
  + `'local-fonts'`
  + `'local-network-access'`
  + `'magnetometer'`
  + `'microphone'`
  + `'midi-sysex'` (system-exclusive midi)
  + `'midi'`
  + `'notifications'`
  + `'payment-handler'`
  + `'storage-access'`
* `origin` str *(optional)*

  The [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin "Origin") to grant permissions to, e.g. "<https://example.com>".

**Returns**

* NoneType

---

### new_cdp_session[​](#browser-context-new-cdp-session "Direct link to new_cdp_session") browserContext.new_cdp_session

note

CDP sessions are only supported on Chromium-based browsers.

Returns the newly created session.

**Usage**

```
browser_context.new_cdp_session(page)
```

**Arguments**

* `page` [Page](Page.md) | [Frame](Frame.md)

  Target to create new session for. For backwards-compatibility, this parameter is named `page`, but it can be a `Page` or `Frame` type.

**Returns**

* [CDPSession](Cdpsession.md)

---

### new_page[​](#browser-context-new-page "Direct link to new_page")

Added before v1.9
browserContext.new_page

Creates a new page in the browser context.

**Usage**

```
browser_context.new_page()
```

**Returns**

* [Page](Page.md)

---

### route[​](#browser-context-route "Direct link to route")

Added before v1.9
browserContext.route

Routing provides the capability to modify network requests that are made by any page in the browser context. Once route is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

note

[browser_context.route()](Browsercontext.md) will not intercept requests intercepted by Service Worker. See [this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when using request interception by setting [service_workers](Browser.md) to `'block'`.

**Usage**

An example of a naive handler that aborts all image requests:

* Sync* Async

```
context = browser.new_context()  
page = context.new_page()  
context.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())  
page.goto("https://example.com")  
browser.close()
```

```
context = await browser.new_context()  
page = await context.new_page()  
await context.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())  
await page.goto("https://example.com")  
await browser.close()
```

or the same snippet using a regex pattern instead:

* Sync* Async

```
context = browser.new_context()  
page = context.new_page()  
context.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())  
page = await context.new_page()  
page = context.new_page()  
page.goto("https://example.com")  
browser.close()
```

```
context = await browser.new_context()  
page = await context.new_page()  
await context.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())  
page = await context.new_page()  
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
context.route("/api/**", handle_route)
```

```
async def handle_route(route: Route):  
  if ("my-string" in route.request.post_data):  
    await route.fulfill(body="mocked-data")  
  else:  
    await route.continue_()  
await context.route("/api/**", handle_route)
```

Page routes (set up with [page.route()](Page.md)) take precedence over browser context routes when request matches both handlers.

To remove a route with its handler you can use [browser_context.unroute()](Browsercontext.md).

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

### route_from_har[​](#browser-context-route-from-har "Direct link to route_from_har") browserContext.route_from_har

If specified the network requests that are made in the context will be served from the HAR file. Read more about [Replaying from HAR](/python/docs/mock#replaying-from-har).

Playwright will not serve requests intercepted by Service Worker from the HAR file. See [this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when using request interception by setting [service_workers](Browser.md) to `'block'`.

**Usage**

```
browser_context.route_from_har(har)  
browser_context.route_from_har(har, **kwargs)
```

**Arguments**

* `har` Union[str, pathlib.Path]

  Path to a [HAR](http://www.softwareishard.com/blog/har-12-spec) file with prerecorded network data. If `path` is a relative path, then it is resolved relative to the current working directory.
* `not_found` "abort" | "fallback" *(optional)*

  + If set to 'abort' any request not found in the HAR file will be aborted.
  + If set to 'fallback' falls through to the next route handler in the handler chain.

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

### route_web_socket[​](#browser-context-route-web-socket "Direct link to route_web_socket") browserContext.route_web_socket

This method allows to modify websocket connections that are made by any page in the browser context.

Note that only `WebSocket`s created after this method was called will be routed. It is recommended to call this method before creating any pages.

**Usage**

Below is an example of a simple handler that blocks some websocket messages. See [WebSocketRoute](Websocketroute.md) for more details and examples.

* Sync* Async

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message == "to-be-blocked":  
    return  
  ws.send(message)  
  
def handler(ws: WebSocketRoute):  
  ws.route_send(lambda message: message_handler(ws, message))  
  ws.connect()  
  
context.route_web_socket("/ws", handler)
```

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message == "to-be-blocked":  
    return  
  ws.send(message)  
  
async def handler(ws: WebSocketRoute):  
  ws.route_send(lambda message: message_handler(ws, message))  
  await ws.connect()  
  
await context.route_web_socket("/ws", handler)
```

**Arguments**

* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool

  Only WebSockets with the url matching this pattern will be routed. A string pattern can be relative to the [base_url](Browser.md) context option.
* `handler` Callable[[WebSocketRoute](Websocketroute.md)]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any] | Any

  Handler function to route the WebSocket.

**Returns**

* NoneType

---

### set_default_navigation_timeout[​](#browser-context-set-default-navigation-timeout "Direct link to set_default_navigation_timeout")

Added before v1.9
browserContext.set_default_navigation_timeout

This setting will change the default maximum navigation time for the following methods and related shortcuts:

* [page.go_back()](Page.md)
* [page.go_forward()](Page.md)
* [page.goto()](Page.md)
* [page.reload()](Page.md)
* [page.set_content()](Page.md)
* [page.expect_navigation()](Page.md)

note

[page.set_default_navigation_timeout()](Page.md) and [page.set_default_timeout()](Page.md) take priority over [browser_context.set_default_navigation_timeout()](Browsercontext.md).

**Usage**

```
browser_context.set_default_navigation_timeout(timeout)
```

**Arguments**

* `timeout` float

  Maximum navigation time in milliseconds

---

### set_default_timeout[​](#browser-context-set-default-timeout "Direct link to set_default_timeout")

Added before v1.9
browserContext.set_default_timeout

This setting will change the default maximum time for all the methods accepting [timeout](Browsercontext.md) option.

note

[page.set_default_navigation_timeout()](Page.md), [page.set_default_timeout()](Page.md) and [browser_context.set_default_navigation_timeout()](Browsercontext.md) take priority over [browser_context.set_default_timeout()](Browsercontext.md).

**Usage**

```
browser_context.set_default_timeout(timeout)
```

**Arguments**

* `timeout` float

  Maximum time in milliseconds. Pass `0` to disable timeout.

---

### set_extra_http_headers[​](#browser-context-set-extra-http-headers "Direct link to set_extra_http_headers")

Added before v1.9
browserContext.set_extra_http_headers

The extra HTTP headers will be sent with every request initiated by any page in the context. These headers are merged with page-specific extra HTTP headers set with [page.set_extra_http_headers()](Page.md). If page overrides a particular header, page-specific header value will be used instead of the browser context header value.

note

[browser_context.set_extra_http_headers()](Browsercontext.md) does not guarantee the order of headers in the outgoing requests.

**Usage**

```
browser_context.set_extra_http_headers(headers)
```

**Arguments**

* `headers` Dict[str, str]

  An object containing additional HTTP headers to be sent with every request. All header values must be strings.

**Returns**

* NoneType

---

### set_geolocation[​](#browser-context-set-geolocation "Direct link to set_geolocation")

Added before v1.9
browserContext.set_geolocation

Sets the context's geolocation. Passing `null` or `undefined` emulates position unavailable.

**Usage**

* Sync* Async

```
browser_context.set_geolocation({"latitude": 59.95, "longitude": 30.31667})
```

```
await browser_context.set_geolocation({"latitude": 59.95, "longitude": 30.31667})
```

note

Consider using [browser_context.grant_permissions()](Browsercontext.md) to grant permissions for the browser context pages to read its geolocation.

**Arguments**

* `geolocation` NoneType | Dict
  + `latitude` float

    Latitude between -90 and 90.
  + `longitude` float

    Longitude between -180 and 180.
  + `accuracy` float *(optional)*

    Non-negative accuracy value. Defaults to `0`.

**Returns**

* NoneType

---

### set_offline[​](#browser-context-set-offline "Direct link to set_offline")

Added before v1.9
browserContext.set_offline

**Usage**

```
browser_context.set_offline(offline)
```

**Arguments**

* `offline` bool

  Whether to emulate network being offline for the browser context.

**Returns**

* NoneType

---

### storage_state[​](#browser-context-storage-state "Direct link to storage_state")

Added before v1.9
browserContext.storage_state

Returns storage state for this browser context, contains current cookies, local storage snapshot and IndexedDB snapshot.

**Usage**

```
browser_context.storage_state()  
browser_context.storage_state(**kwargs)
```

**Arguments**

* `indexed_db` bool *(optional)* 

  Set to `true` to include [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) in the storage state snapshot. If your application uses IndexedDB to store authentication tokens, like Firebase Authentication, enable this.
* `path` Union[str, pathlib.Path] *(optional)*

  The file path to save the storage state to. If [path](Browsercontext.md) is a relative path, then it is resolved relative to current working directory. If no path is provided, storage state is still returned, but won't be saved to the disk.

**Returns**

* Dict
  + `cookies` List[Dict]

    - `name` str
    - `value` str
    - `domain` str
    - `path` str
    - `expires` float

      Unix time in seconds.
    - `httpOnly` bool
    - `secure` bool
    - `sameSite` "Strict" | "Lax" | "None"
  + `origins` List[Dict]

    - `origin` str
    - `localStorage` List[Dict]

      * `name` str
      * `value` str

---

### unroute[​](#browser-context-unroute "Direct link to unroute")

Added before v1.9
browserContext.unroute

Removes a route created with [browser_context.route()](Browsercontext.md). When [handler](Browsercontext.md) is not specified, removes all routes for the [url](Browsercontext.md).

**Usage**

```
browser_context.unroute(url)  
browser_context.unroute(url, **kwargs)
```

**Arguments**

* `url` str | Pattern | Callable[[URL](https://en.wikipedia.org/wiki/URL "URL")]:bool

  A glob pattern, regex pattern or predicate receiving [URL](https://en.wikipedia.org/wiki/URL "URL") used to register a routing with [browser_context.route()](Browsercontext.md).
* `handler` Callable[[Route](Route.md), [Request](Request.md)]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any] | Any *(optional)*

  Optional handler function used to register a routing with [browser_context.route()](Browsercontext.md).

**Returns**

* NoneType

---

### unroute_all[​](#browser-context-unroute-all "Direct link to unroute_all") browserContext.unroute_all

Removes all routes created with [browser_context.route()](Browsercontext.md) and [browser_context.route_from_har()](Browsercontext.md).

**Usage**

```
browser_context.unroute_all()  
browser_context.unroute_all(**kwargs)
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

### wait_for_event[​](#browser-context-wait-for-event-2 "Direct link to wait_for_event")

Added before v1.9
browserContext.wait_for_event

note

In most cases, you should use [browser_context.expect_event()](Browsercontext.md).

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function and waits for `predicate(event)` to return a truthy value. Will throw an error if the browser context is closed before the `event` is fired.

**Usage**

```
browser_context.wait_for_event(event)  
browser_context.wait_for_event(event, **kwargs)
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

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### browser[​](#browser-context-browser "Direct link to browser")

Added before v1.9
browserContext.browser

Gets the browser instance that owns the context. Returns `null` if the context is created outside of normal browser, e.g. Android or Electron.

**Usage**

```
browser_context.browser
```

**Returns**

* NoneType | [Browser](Browser.md)

---

### clock[​](#browser-context-clock "Direct link to clock") browserContext.clock

Playwright has ability to mock clock and passage of time.

**Usage**

```
browser_context.clock
```

**Type**

* [Clock](Clock.md)

---

### pages[​](#browser-context-pages "Direct link to pages")

Added before v1.9
browserContext.pages

Returns all open pages in the context.

**Usage**

```
browser_context.pages
```

**Returns**

* List[[Page](Page.md)]

---

### request[​](#browser-context-request "Direct link to request") browserContext.request

API testing helper associated with this context. Requests made with this API will use context cookies.

**Usage**

```
browser_context.request
```

**Type**

* [APIRequestContext](Apirequestcontext.md)

---

### service_workers[​](#browser-context-service-workers "Direct link to service_workers") browserContext.service_workers

note

Service workers are only supported on Chromium-based browsers.

All existing service workers in the context.

**Usage**

```
browser_context.service_workers
```

**Returns**

* List[[Worker](Worker.md)]

---

### tracing[​](#browser-context-tracing "Direct link to tracing") browserContext.tracing

**Usage**

```
browser_context.tracing
```

**Type**

* [Tracing](Tracing.md)

---

Events[​](#events "Direct link to Events")
------------------------------------------

### on("close")[​](#browser-context-event-close "Direct link to on(\"close\")")

Added before v1.9
browserContext.on("close")

Emitted when Browser context gets closed. This might happen because of one of the following:

* Browser context is closed.
* Browser application is closed or crashed.
* The [browser.close()](Browser.md) method was called.

**Usage**

```
browser_context.on("close", handler)
```

**Event data**

* [BrowserContext](Browsercontext.md)

---

### on("console")[​](#browser-context-event-console "Direct link to on(\"console\")") browserContext.on("console")

Emitted when JavaScript within the page calls one of console API methods, e.g. `console.log` or `console.dir`.

The arguments passed into `console.log` and the page are available on the [ConsoleMessage](Consolemessage.md) event handler argument.

**Usage**

* Sync* Async

```
def print_args(msg):  
    for arg in msg.args:  
        print(arg.json_value())  
  
context.on("console", print_args)  
page.evaluate("console.log('hello', 5, { foo: 'bar' })")
```

```
async def print_args(msg):  
    values = []  
    for arg in msg.args:  
        values.append(await arg.json_value())  
    print(values)  
  
context.on("console", print_args)  
await page.evaluate("console.log('hello', 5, { foo: 'bar' })")
```

**Event data**

* [ConsoleMessage](Consolemessage.md)

---

### on("dialog")[​](#browser-context-event-dialog "Direct link to on(\"dialog\")") browserContext.on("dialog")

Emitted when a JavaScript dialog appears, such as `alert`, `prompt`, `confirm` or `beforeunload`. Listener **must** either [dialog.accept()](Dialog.md) or [dialog.dismiss()](Dialog.md) the dialog - otherwise the page will [freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop#never_blocking) waiting for the dialog, and actions like click will never finish.

**Usage**

```
context.on("dialog", lambda dialog: dialog.accept())
```

note

When no [page.on("dialog")](Page.md) or [browser_context.on("dialog")](Browsercontext.md) listeners are present, all dialogs are automatically dismissed.

**Event data**

* [Dialog](Dialog.md)

---

### on("page")[​](#browser-context-event-page "Direct link to on(\"page\")")

Added before v1.9
browserContext.on("page")

The event is emitted when a new Page is created in the BrowserContext. The page may still be loading. The event will also fire for popup pages. See also [page.on("popup")](Page.md) to receive events about popups relevant to a specific page.

The earliest moment that page is available is when it has navigated to the initial url. For example, when opening a popup with `window.open('http://example.com')`, this event will fire when the network request to "<http://example.com>" is done and its response has started loading in the popup. If you would like to route/listen to this network request, use [browser_context.route()](Browsercontext.md) and [browser_context.on("request")](Browsercontext.md) respectively instead of similar methods on the [Page](Page.md).

* Sync* Async

```
with context.expect_page() as page_info:  
    page.get_by_text("open new page").click(),  
page = page_info.value  
print(page.evaluate("location.href"))
```

```
async with context.expect_page() as page_info:  
    await page.get_by_text("open new page").click(),  
page = await page_info.value  
print(await page.evaluate("location.href"))
```

note

Use [page.wait_for_load_state()](Page.md) to wait until the page gets to a particular state (you should not need it in most cases).

**Usage**

```
browser_context.on("page", handler)
```

**Event data**

* [Page](Page.md)

---

### on("request")[​](#browser-context-event-request "Direct link to on(\"request\")") browserContext.on("request")

Emitted when a request is issued from any pages created through this context. The [request](Request.md) object is read-only. To only listen for requests from a particular page, use [page.on("request")](Page.md).

In order to intercept and mutate requests, see [browser_context.route()](Browsercontext.md) or [page.route()](Page.md).

**Usage**

```
browser_context.on("request", handler)
```

**Event data**

* [Request](Request.md)

---

### on("requestfailed")[​](#browser-context-event-request-failed "Direct link to on(\"requestfailed\")") browserContext.on("requestfailed")

Emitted when a request fails, for example by timing out. To only listen for failed requests from a particular page, use [page.on("requestfailed")](Page.md).

note

HTTP Error responses, such as 404 or 503, are still successful responses from HTTP standpoint, so request will complete with [browser_context.on("requestfinished")](Browsercontext.md) event and not with [browser_context.on("requestfailed")](Browsercontext.md).

**Usage**

```
browser_context.on("requestfailed", handler)
```

**Event data**

* [Request](Request.md)

---

### on("requestfinished")[​](#browser-context-event-request-finished "Direct link to on(\"requestfinished\")") browserContext.on("requestfinished")

Emitted when a request finishes successfully after downloading the response body. For a successful response, the sequence of events is `request`, `response` and `requestfinished`. To listen for successful requests from a particular page, use [page.on("requestfinished")](Page.md).

**Usage**

```
browser_context.on("requestfinished", handler)
```

**Event data**

* [Request](Request.md)

---

### on("response")[​](#browser-context-event-response "Direct link to on(\"response\")") browserContext.on("response")

Emitted when [response](Response.md) status and headers are received for a request. For a successful response, the sequence of events is `request`, `response` and `requestfinished`. To listen for response events from a particular page, use [page.on("response")](Page.md).

**Usage**

```
browser_context.on("response", handler)
```

**Event data**

* [Response](Response.md)

---

### on("serviceworker")[​](#browser-context-event-service-worker "Direct link to on(\"serviceworker\")") browserContext.on("serviceworker")

note

Service workers are only supported on Chromium-based browsers.

Emitted when new service worker is created in the context.

**Usage**

```
browser_context.on("serviceworker", handler)
```

**Event data**

* [Worker](Worker.md)

---

### on("weberror")[​](#browser-context-event-web-error "Direct link to on(\"weberror\")") browserContext.on("weberror")

Emitted when exception is unhandled in any of the pages in this context. To listen for errors from a particular page, use [page.on("pageerror")](Page.md) instead.

**Usage**

```
browser_context.on("weberror", handler)
```

**Event data**

* [WebError](Weberror.md)

---

Deprecated[​](#deprecated "Direct link to Deprecated")
------------------------------------------------------

### on("backgroundpage")[​](#browser-context-event-background-page "Direct link to on(\"backgroundpage\")") browserContext.on("backgroundpage")

Deprecated

Background pages have been removed from Chromium together with Manifest V2 extensions.

This event is not emitted.

**Usage**

```
browser_context.on("backgroundpage", handler)
```

**Event data**

* [Page](Page.md)

---

### background_pages[​](#browser-context-background-pages "Direct link to background_pages") browserContext.background_pages

Deprecated

Background pages have been removed from Chromium together with Manifest V2 extensions.

Returns an empty list.

**Usage**

```
browser_context.background_pages
```

**Returns**

* List[[Page](Page.md)]
