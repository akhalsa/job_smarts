# WebSocketRoute

Source: https://playwright.dev/python/docs/api/class-websocketroute

---

Whenever a [`WebSocket`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) route is set up with [page.route_web_socket()](Page.md) or [browser_context.route_web_socket()](Browsercontext.md), the `WebSocketRoute` object allows to handle the WebSocket, like an actual server would do.

**Mocking**

By default, the routed WebSocket will not connect to the server. This way, you can mock entire communication over the WebSocket. Here is an example that responds to a `"request"` with a `"response"`.

* Sync* Async

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message == "request":  
    ws.send("response")  
  
page.route_web_socket("wss://example.com/ws", lambda ws: ws.on_message(  
    lambda message: message_handler(ws, message)  
))
```

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message == "request":  
    ws.send("response")  
  
await page.route_web_socket("wss://example.com/ws", lambda ws: ws.on_message(  
    lambda message: message_handler(ws, message)  
))
```

Since we do not call [web_socket_route.connect_to_server](Websocketroute.md) inside the WebSocket route handler, Playwright assumes that WebSocket will be mocked, and opens the WebSocket inside the page automatically.

Here is another example that handles JSON messages:

* Sync* Async

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  json_message = json.loads(message)  
  if json_message["request"] == "question":  
    ws.send(json.dumps({ "response": "answer" }))  
  
page.route_web_socket("wss://example.com/ws", lambda ws: ws.on_message(  
    lambda message: message_handler(ws, message)  
))
```

```
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  json_message = json.loads(message)  
  if json_message["request"] == "question":  
    ws.send(json.dumps({ "response": "answer" }))  
  
await page.route_web_socket("wss://example.com/ws", lambda ws: ws.on_message(  
    lambda message: message_handler(ws, message)  
))
```

**Intercepting**

Alternatively, you may want to connect to the actual server, but intercept messages in-between and modify or block them. Calling [web_socket_route.connect_to_server](Websocketroute.md) returns a server-side `WebSocketRoute` instance that you can send messages to, or handle incoming messages.

Below is an example that modifies some messages sent by the page to the server. Messages sent from the server to the page are left intact, relying on the default forwarding.

* Sync* Async

```
def message_handler(server: WebSocketRoute, message: Union[str, bytes]):  
  if message == "request":  
    server.send("request2")  
  else:  
    server.send(message)  
  
def handler(ws: WebSocketRoute):  
  server = ws.connect_to_server()  
  ws.on_message(lambda message: message_handler(server, message))  
  
page.route_web_socket("/ws", handler)
```

```
def message_handler(server: WebSocketRoute, message: Union[str, bytes]):  
  if message == "request":  
    server.send("request2")  
  else:  
    server.send(message)  
  
def handler(ws: WebSocketRoute):  
  server = ws.connect_to_server()  
  ws.on_message(lambda message: message_handler(server, message))  
  
await page.route_web_socket("/ws", handler)
```

After connecting to the server, all **messages are forwarded** between the page and the server by default.

However, if you call [web_socket_route.on_message()](Websocketroute.md) on the original route, messages from the page to the server **will not be forwarded** anymore, but should instead be handled by the [handler](Websocketroute.md).

Similarly, calling [web_socket_route.on_message()](Websocketroute.md) on the server-side WebSocket will **stop forwarding messages** from the server to the page, and [handler](Websocketroute.md) should take care of them.

The following example blocks some messages in both directions. Since it calls [web_socket_route.on_message()](Websocketroute.md) in both directions, there is no automatic forwarding at all.

* Sync* Async

```
def ws_message_handler(server: WebSocketRoute, message: Union[str, bytes]):  
  if message != "blocked-from-the-page":  
    server.send(message)  
  
def server_message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message != "blocked-from-the-server":  
    ws.send(message)  
  
def handler(ws: WebSocketRoute):  
  server = ws.connect_to_server()  
  ws.on_message(lambda message: ws_message_handler(server, message))  
  server.on_message(lambda message: server_message_handler(ws, message))  
  
page.route_web_socket("/ws", handler)
```

```
def ws_message_handler(server: WebSocketRoute, message: Union[str, bytes]):  
  if message != "blocked-from-the-page":  
    server.send(message)  
  
def server_message_handler(ws: WebSocketRoute, message: Union[str, bytes]):  
  if message != "blocked-from-the-server":  
    ws.send(message)  
  
def handler(ws: WebSocketRoute):  
  server = ws.connect_to_server()  
  ws.on_message(lambda message: ws_message_handler(server, message))  
  server.on_message(lambda message: server_message_handler(ws, message))  
  
await page.route_web_socket("/ws", handler)
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### close[​](#web-socket-route-close "Direct link to close") webSocketRoute.close

Closes one side of the WebSocket connection.

**Usage**

```
web_socket_route.close()  
web_socket_route.close(**kwargs)
```

**Arguments**

* `code` int *(optional)*

  Optional [close code](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#code).
* `reason` str *(optional)*

  Optional [close reason](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#reason).

**Returns**

* NoneType

---

### on_close[​](#web-socket-route-on-close "Direct link to on_close") webSocketRoute.on_close

Allows to handle [`WebSocket.close`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close).

By default, closing one side of the connection, either in the page or on the server, will close the other side. However, when [web_socket_route.on_close()](Websocketroute.md) handler is set up, the default forwarding of closure is disabled, and handler should take care of it.

**Usage**

```
web_socket_route.on_close(handler)
```

**Arguments**

* `handler` Callable[int | [undefined]]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any] | Any

  Function that will handle WebSocket closure. Received an optional [close code](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#code) and an optional [close reason](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#reason).

---

### on_message[​](#web-socket-route-on-message "Direct link to on_message") webSocketRoute.on_message

This method allows to handle messages that are sent by the WebSocket, either from the page or from the server.

When called on the original WebSocket route, this method handles messages sent from the page. You can handle this messages by responding to them with [web_socket_route.send()](Websocketroute.md), forwarding them to the server-side connection returned by [web_socket_route.connect_to_server](Websocketroute.md) or do something else.

Once this method is called, messages are not automatically forwarded to the server or to the page - you should do that manually by calling [web_socket_route.send()](Websocketroute.md). See examples at the top for more details.

Calling this method again will override the handler with a new one.

**Usage**

```
web_socket_route.on_message(handler)
```

**Arguments**

* `handler` Callable[str]:[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")[Any] | Any

  Function that will handle messages.

---

### send[​](#web-socket-route-send "Direct link to send") webSocketRoute.send

Sends a message to the WebSocket. When called on the original WebSocket, sends the message to the page. When called on the result of [web_socket_route.connect_to_server](Websocketroute.md), sends the message to the server. See examples at the top for more details.

**Usage**

```
web_socket_route.send(message)
```

**Arguments**

* `message` str | bytes

  Message to send.

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### connect_to_server[​](#web-socket-route-connect-to-server "Direct link to connect_to_server") webSocketRoute.connect_to_server

By default, routed WebSocket does not connect to the server, so you can mock entire WebSocket communication. This method connects to the actual WebSocket server, and returns the server-side [WebSocketRoute](Websocketroute.md) instance, giving the ability to send and receive messages from the server.

Once connected to the server:

* Messages received from the server will be **automatically forwarded** to the WebSocket in the page, unless [web_socket_route.on_message()](Websocketroute.md) is called on the server-side `WebSocketRoute`.
* Messages sent by the [`WebSocket.send()`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/send) call in the page will be **automatically forwarded** to the server, unless [web_socket_route.on_message()](Websocketroute.md) is called on the original `WebSocketRoute`.

See examples at the top for more details.

**Usage**

```
web_socket_route.connect_to_server
```

**Returns**

* [WebSocketRoute](Websocketroute.md)

---

### url[​](#web-socket-route-url "Direct link to url") webSocketRoute.url

URL of the WebSocket created in the page.

**Usage**

```
web_socket_route.url
```

**Returns**

* str
