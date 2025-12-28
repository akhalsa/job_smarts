# ConsoleMessage

Source: https://playwright.dev/python/docs/api/class-consolemessage

---

[ConsoleMessage](Consolemessage.md) objects are dispatched by page via the [page.on("console")](Page.md) event. For each console message logged in the page there will be corresponding event in the Playwright context.

* Sync* Async

```
# Listen for all console logs  
page.on("console", lambda msg: print(msg.text))  
  
# Listen for all console events and handle errors  
page.on("console", lambda msg: print(f"error: {msg.text}") if msg.type == "error" else None)  
  
# Get the next console log  
with page.expect_console_message() as msg_info:  
    # Issue console.log inside the page  
    page.evaluate("console.log('hello', 42, { foo: 'bar' })")  
msg = msg_info.value  
  
# Deconstruct print arguments  
msg.args[0].json_value() # hello  
msg.args[1].json_value() # 42
```

```
# Listen for all console logs  
page.on("console", lambda msg: print(msg.text))  
  
# Listen for all console events and handle errors  
page.on("console", lambda msg: print(f"error: {msg.text}") if msg.type == "error" else None)  
  
# Get the next console log  
async with page.expect_console_message() as msg_info:  
    # Issue console.log inside the page  
    await page.evaluate("console.log('hello', 42, { foo: 'bar' })")  
msg = await msg_info.value  
  
# Deconstruct print arguments  
await msg.args[0].json_value() # hello  
await msg.args[1].json_value() # 42
```

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### args[​](#console-message-args "Direct link to args")

Added before v1.9
consoleMessage.args

List of arguments passed to a `console` function call. See also [page.on("console")](Page.md).

**Usage**

```
console_message.args
```

**Returns**

* List[[JSHandle](Jshandle.md)]

---

### location[​](#console-message-location "Direct link to location")

Added before v1.9
consoleMessage.location

**Usage**

```
console_message.location
```

**Returns**

* Dict
  + `url` str

    URL of the resource.
  + `lineNumber` int

    0-based line number in the resource.
  + `columnNumber` int

    0-based column number in the resource.

---

### page[​](#console-message-page "Direct link to page") consoleMessage.page

The page that produced this console message, if any.

**Usage**

```
console_message.page
```

**Returns**

* NoneType | [Page](Page.md)

---

### text[​](#console-message-text "Direct link to text")

Added before v1.9
consoleMessage.text

The text of the console message.

**Usage**

```
console_message.text
```

**Returns**

* str

---

### type[​](#console-message-type "Direct link to type")

Added before v1.9
consoleMessage.type

**Usage**

```
console_message.type
```

**Returns**

* "log" | "debug" | "info" | "error" | "warning" | "dir" | "dirxml" | "table" | "trace" | "clear" | "startGroup" | "startGroupCollapsed" | "endGroup" | "assert" | "profile" | "profileEnd" | "count" | "timeEnd"

---

### worker[​](#console-message-worker "Direct link to worker") consoleMessage.worker

The web worker or service worker that produced this console message, if any. Note that console messages from web workers also have non-null [console_message.page](Consolemessage.md).

**Usage**

```
console_message.worker
```

**Returns**

* NoneType | [Worker](Worker.md)

* [Properties](#properties)
  + [args](#console-message-args)+ [location](#console-message-location)+ [page](#console-message-page)+ [text](#console-message-text)+ [type](#console-message-type)+ [worker](#console-message-worker)
