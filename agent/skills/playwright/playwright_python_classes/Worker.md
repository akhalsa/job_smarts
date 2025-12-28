# Worker

Source: https://playwright.dev/python/docs/api/class-worker

---

The Worker class represents a [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API). `worker` event is emitted on the page object to signal a worker creation. `close` event is emitted on the worker object when the worker is gone.

```
def handle_worker(worker):  
    print("worker created: " + worker.url)  
    worker.on("close", lambda: print("worker destroyed: " + worker.url))  
  
page.on('worker', handle_worker)  
  
print("current workers:")  
for worker in page.workers:  
    print("    " + worker.url)
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### evaluate[​](#worker-evaluate "Direct link to evaluate")

Added before v1.9
worker.evaluate

Returns the return value of [expression](Worker.md).

If the function passed to the [worker.evaluate()](Worker.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [worker.evaluate()](Worker.md) would wait for the promise to resolve and return its value.

If the function passed to the [worker.evaluate()](Worker.md) returns a non-[Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") value, then [worker.evaluate()](Worker.md) returns `undefined`. Playwright also supports transferring some additional values that are not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

```
worker.evaluate(expression)  
worker.evaluate(expression, **kwargs)
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Worker.md).

**Returns**

* Dict

---

### evaluate_handle[​](#worker-evaluate-handle "Direct link to evaluate_handle")

Added before v1.9
worker.evaluate_handle

Returns the return value of [expression](Worker.md) as a [JSHandle](Jshandle.md).

The only difference between [worker.evaluate()](Worker.md) and [worker.evaluate_handle()](Worker.md) is that [worker.evaluate_handle()](Worker.md) returns [JSHandle](Jshandle.md).

If the function passed to the [worker.evaluate_handle()](Worker.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [worker.evaluate_handle()](Worker.md) would wait for the promise to resolve and return its value.

**Usage**

```
worker.evaluate_handle(expression)  
worker.evaluate_handle(expression, **kwargs)
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Worker.md).

**Returns**

* [JSHandle](Jshandle.md)

---

### expect_event[​](#worker-wait-for-event "Direct link to expect_event") worker.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

**Usage**

* Sync* Async

```
with worker.expect_event("console") as event_info:  
    worker.evaluate("console.log(42)")  
message = event_info.value
```

```
async with worker.expect_event("console") as event_info:  
    await worker.evaluate("console.log(42)")  
message = await event_info.value
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

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### url[​](#worker-url "Direct link to url")

Added before v1.9
worker.url

**Usage**

```
worker.url
```

**Returns**

* str

---

Events[​](#events "Direct link to Events")
------------------------------------------

### on("close")[​](#worker-event-close "Direct link to on(\"close\")")

Added before v1.9
worker.on("close")

Emitted when this dedicated [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) is terminated.

**Usage**

```
worker.on("close", handler)
```

**Event data**

* [Worker](Worker.md)

---

### on("console")[​](#worker-event-console "Direct link to on(\"console\")") worker.on("console")

Emitted when JavaScript within the worker calls one of console API methods, e.g. `console.log` or `console.dir`.

**Usage**

```
worker.on("console", handler)
```

**Event data**

* [ConsoleMessage](Consolemessage.md)
