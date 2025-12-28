# WebSocket

Source: https://playwright.dev/python/docs/api/class-websocket

---

The [WebSocket](Websocket.md) class represents WebSocket connections within a page. It provides the ability to inspect and manipulate the data being transmitted and received.

If you want to intercept or modify WebSocket frames, consider using [WebSocketRoute](Websocketroute.md).

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### expect_event[​](#web-socket-wait-for-event "Direct link to expect_event")

Added before v1.9
webSocket.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy value. Will throw an error if the webSocket is closed before the event is fired. Returns the event data value.

**Usage**

```
web_socket.expect_event(event)  
web_socket.expect_event(event, **kwargs)
```

**Arguments**

* `event` str

  Event name, same one would pass into `webSocket.on(event)`.
* `predicate` Callable *(optional)*

  Receives the event data and resolves to truthy value when the waiting should resolve.
* `timeout` float *(optional)*

  Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md).

**Returns**

* EventContextManager

---

### wait_for_event[​](#web-socket-wait-for-event-2 "Direct link to wait_for_event")

Added before v1.9
webSocket.wait_for_event

note

In most cases, you should use [web_socket.expect_event()](Websocket.md).

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function and waits for `predicate(event)` to return a truthy value. Will throw an error if the socket is closed before the `event` is fired.

**Usage**

```
web_socket.wait_for_event(event)  
web_socket.wait_for_event(event, **kwargs)
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

### is_closed[​](#web-socket-is-closed "Direct link to is_closed")

Added before v1.9
webSocket.is_closed

Indicates that the web socket has been closed.

**Usage**

```
web_socket.is_closed()
```

**Returns**

* bool

---

### url[​](#web-socket-url "Direct link to url")

Added before v1.9
webSocket.url

Contains the URL of the WebSocket.

**Usage**

```
web_socket.url
```

**Returns**

* str

---

Events[​](#events "Direct link to Events")
------------------------------------------

### on("close")[​](#web-socket-event-close "Direct link to on(\"close\")")

Added before v1.9
webSocket.on("close")

Fired when the websocket closes.

**Usage**

```
web_socket.on("close", handler)
```

**Event data**

* [WebSocket](Websocket.md)

---

### on("framereceived")[​](#web-socket-event-frame-received "Direct link to on(\"framereceived\")") webSocket.on("framereceived")

Fired when the websocket receives a frame.

**Usage**

```
web_socket.on("framereceived", handler)
```

**Event data**

* str | bytes

---

### on("framesent")[​](#web-socket-event-frame-sent "Direct link to on(\"framesent\")") webSocket.on("framesent")

Fired when the websocket sends a frame.

**Usage**

```
web_socket.on("framesent", handler)
```

**Event data**

* str | bytes

---

### on("socketerror")[​](#web-socket-event-socket-error "Direct link to on(\"socketerror\")") webSocket.on("socketerror")

Fired when the websocket has an error.

**Usage**

```
web_socket.on("socketerror", handler)
```

**Event data**

* str
