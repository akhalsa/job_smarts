# Tracing

Source: https://playwright.dev/python/docs/api/class-tracing

---

API for collecting and saving Playwright traces. Playwright traces can be opened in [Trace Viewer](/python/docs/trace-viewer) after Playwright script runs.

note

You probably want to [enable tracing in your config file](https://playwright.dev/docs/api/class-testoptions#test-options-trace) instead of using `context.tracing`.

The `context.tracing` API captures browser operations and network activity, but it doesn't record test assertions (like `expect` calls). We recommend [enabling tracing through Playwright Test configuration](https://playwright.dev/docs/api/class-testoptions#test-options-trace), which includes those assertions and provides a more complete trace for debugging test failures.

Start recording a trace before performing actions. At the end, stop tracing and save it to a file.

* Sync* Async

```
browser = chromium.launch()  
context = browser.new_context()  
context.tracing.start(screenshots=True, snapshots=True)  
page = context.new_page()  
page.goto("https://playwright.dev")  
context.tracing.stop(path = "trace.zip")
```

```
browser = await chromium.launch()  
context = await browser.new_context()  
await context.tracing.start(screenshots=True, snapshots=True)  
page = await context.new_page()  
await page.goto("https://playwright.dev")  
await context.tracing.stop(path = "trace.zip")
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### group[​](#tracing-group "Direct link to group") tracing.group

caution

Use `test.step` instead when available.

Creates a new group within the trace, assigning any subsequent API calls to this group, until [tracing.group_end()](Tracing.md) is called. Groups can be nested and will be visible in the trace viewer.

**Usage**

* Sync* Async

```
# All actions between group and group_end  
# will be shown in the trace viewer as a group.  
page.context.tracing.group("Open Playwright.dev > API")  
page.goto("https://playwright.dev/")  
page.get_by_role("link", name="API").click()  
page.context.tracing.group_end()
```

```
# All actions between group and group_end  
# will be shown in the trace viewer as a group.  
await page.context.tracing.group("Open Playwright.dev > API")  
await page.goto("https://playwright.dev/")  
await page.get_by_role("link", name="API").click()  
await page.context.tracing.group_end()
```

**Arguments**

* `name` str

  Group name shown in the trace viewer.
* `location` Dict *(optional)*

  + `file` str
  + `line` int *(optional)*
  + `column` int *(optional)*

  Specifies a custom location for the group to be shown in the trace viewer. Defaults to the location of the [tracing.group()](Tracing.md) call.

**Returns**

* NoneType

---

### group_end[​](#tracing-group-end "Direct link to group_end") tracing.group_end

Closes the last group created by [tracing.group()](Tracing.md).

**Usage**

```
tracing.group_end()
```

**Returns**

* NoneType

---

### start[​](#tracing-start "Direct link to start") tracing.start

Start tracing.

note

You probably want to [enable tracing in your config file](https://playwright.dev/docs/api/class-testoptions#test-options-trace) instead of using `Tracing.start`.

The `context.tracing` API captures browser operations and network activity, but it doesn't record test assertions (like `expect` calls). We recommend [enabling tracing through Playwright Test configuration](https://playwright.dev/docs/api/class-testoptions#test-options-trace), which includes those assertions and provides a more complete trace for debugging test failures.

**Usage**

* Sync* Async

```
context.tracing.start(screenshots=True, snapshots=True)  
page = context.new_page()  
page.goto("https://playwright.dev")  
context.tracing.stop(path = "trace.zip")
```

```
await context.tracing.start(screenshots=True, snapshots=True)  
page = await context.new_page()  
await page.goto("https://playwright.dev")  
await context.tracing.stop(path = "trace.zip")
```

**Arguments**

* `name` str *(optional)*

  If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the [traces_dir](Browsertype.md) directory specified in [browser_type.launch()](Browsertype.md). To specify the final trace zip file name, you need to pass `path` option to [tracing.stop()](Tracing.md) instead.
* `screenshots` bool *(optional)*

  Whether to capture screenshots during tracing. Screenshots are used to build a timeline preview.
* `snapshots` bool *(optional)*

  If this option is true tracing will

  + capture DOM snapshot on every action
  + record network activity
* `sources` bool *(optional)* 

  Whether to include source files for trace actions.
* `title` str *(optional)* 

  Trace name to be shown in the Trace Viewer.

**Returns**

* NoneType

---

### start_chunk[​](#tracing-start-chunk "Direct link to start_chunk") tracing.start_chunk

Start a new trace chunk. If you'd like to record multiple traces on the same [BrowserContext](Browsercontext.md), use [tracing.start()](Tracing.md) once, and then create multiple trace chunks with [tracing.start_chunk()](Tracing.md) and [tracing.stop_chunk()](Tracing.md).

**Usage**

* Sync* Async

```
context.tracing.start(screenshots=True, snapshots=True)  
page = context.new_page()  
page.goto("https://playwright.dev")  
  
context.tracing.start_chunk()  
page.get_by_text("Get Started").click()  
# Everything between start_chunk and stop_chunk will be recorded in the trace.  
context.tracing.stop_chunk(path = "trace1.zip")  
  
context.tracing.start_chunk()  
page.goto("http://example.com")  
# Save a second trace file with different actions.  
context.tracing.stop_chunk(path = "trace2.zip")
```

```
await context.tracing.start(screenshots=True, snapshots=True)  
page = await context.new_page()  
await page.goto("https://playwright.dev")  
  
await context.tracing.start_chunk()  
await page.get_by_text("Get Started").click()  
# Everything between start_chunk and stop_chunk will be recorded in the trace.  
await context.tracing.stop_chunk(path = "trace1.zip")  
  
await context.tracing.start_chunk()  
await page.goto("http://example.com")  
# Save a second trace file with different actions.  
await context.tracing.stop_chunk(path = "trace2.zip")
```

**Arguments**

* `name` str *(optional)* 

  If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the [traces_dir](Browsertype.md) directory specified in [browser_type.launch()](Browsertype.md). To specify the final trace zip file name, you need to pass `path` option to [tracing.stop_chunk()](Tracing.md) instead.
* `title` str *(optional)* 

  Trace name to be shown in the Trace Viewer.

**Returns**

* NoneType

---

### stop[​](#tracing-stop "Direct link to stop") tracing.stop

Stop tracing.

**Usage**

```
tracing.stop()  
tracing.stop(**kwargs)
```

**Arguments**

* `path` Union[str, pathlib.Path] *(optional)*

  Export trace into the file with the given path.

**Returns**

* NoneType

---

### stop_chunk[​](#tracing-stop-chunk "Direct link to stop_chunk") tracing.stop_chunk

Stop the trace chunk. See [tracing.start_chunk()](Tracing.md) for more details about multiple trace chunks.

**Usage**

```
tracing.stop_chunk()  
tracing.stop_chunk(**kwargs)
```

**Arguments**

* `path` Union[str, pathlib.Path] *(optional)*

  Export trace collected since the last [tracing.start_chunk()](Tracing.md) call into the file with the given path.

**Returns**

* NoneType
