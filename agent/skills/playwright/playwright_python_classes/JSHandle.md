# JSHandle

Source: https://playwright.dev/python/docs/api/class-jshandle

---

JSHandle represents an in-page JavaScript object. JSHandles can be created with the [page.evaluate_handle()](Page.md) method.

* Sync* Async

```
window_handle = page.evaluate_handle("window")  
# ...
```

```
window_handle = await page.evaluate_handle("window")  
# ...
```

JSHandle prevents the referenced JavaScript object being garbage collected unless the handle is exposed with [js_handle.dispose()](Jshandle.md). JSHandles are auto-disposed when their origin frame gets navigated or the parent context gets destroyed.

JSHandle instances can be used as an argument in [page.eval_on_selector()](Page.md), [page.evaluate()](Page.md) and [page.evaluate_handle()](Page.md) methods.

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### dispose[​](#js-handle-dispose "Direct link to dispose")

Added before v1.9
jsHandle.dispose

The `jsHandle.dispose` method stops referencing the element handle.

**Usage**

```
js_handle.dispose()
```

**Returns**

* NoneType

---

### evaluate[​](#js-handle-evaluate "Direct link to evaluate")

Added before v1.9
jsHandle.evaluate

Returns the return value of [expression](Jshandle.md).

This method passes this handle as the first argument to [expression](Jshandle.md).

If [expression](Jshandle.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then `handle.evaluate` would wait for the promise to resolve and return its value.

**Usage**

* Sync* Async

```
tweet_handle = page.query_selector(".tweet .retweets")  
assert tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

```
tweet_handle = await page.query_selector(".tweet .retweets")  
assert await tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Jshandle.md).

**Returns**

* Dict

---

### evaluate_handle[​](#js-handle-evaluate-handle "Direct link to evaluate_handle")

Added before v1.9
jsHandle.evaluate_handle

Returns the return value of [expression](Jshandle.md) as a [JSHandle](Jshandle.md).

This method passes this handle as the first argument to [expression](Jshandle.md).

The only difference between `jsHandle.evaluate` and `jsHandle.evaluateHandle` is that `jsHandle.evaluateHandle` returns [JSHandle](Jshandle.md).

If the function passed to the `jsHandle.evaluateHandle` returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then `jsHandle.evaluateHandle` would wait for the promise to resolve and return its value.

See [page.evaluate_handle()](Page.md) for more details.

**Usage**

```
js_handle.evaluate_handle(expression)  
js_handle.evaluate_handle(expression, **kwargs)
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Jshandle.md).

**Returns**

* [JSHandle](Jshandle.md)

---

### get_properties[​](#js-handle-get-properties "Direct link to get_properties")

Added before v1.9
jsHandle.get_properties

The method returns a map with **own property names** as keys and JSHandle instances for the property values.

**Usage**

* Sync* Async

```
handle = page.evaluate_handle("({ window, document })")  
properties = handle.get_properties()  
window_handle = properties.get("window")  
document_handle = properties.get("document")  
handle.dispose()
```

```
handle = await page.evaluate_handle("({ window, document })")  
properties = await handle.get_properties()  
window_handle = properties.get("window")  
document_handle = properties.get("document")  
await handle.dispose()
```

**Returns**

* [Map][str, [JSHandle](Jshandle.md)]

---

### get_property[​](#js-handle-get-property "Direct link to get_property")

Added before v1.9
jsHandle.get_property

Fetches a single property from the referenced object.

**Usage**

```
js_handle.get_property(property_name)
```

**Arguments**

* `property_name` str

  property to get

**Returns**

* [JSHandle](Jshandle.md)

---

### json_value[​](#js-handle-json-value "Direct link to json_value")

Added before v1.9
jsHandle.json_value

Returns a JSON representation of the object. If the object has a `toJSON` function, it **will not be called**.

note

The method will return an empty JSON object if the referenced object is not stringifiable. It will throw an error if the object has circular references.

**Usage**

```
js_handle.json_value()
```

**Returns**

* Dict

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### as_element[​](#js-handle-as-element "Direct link to as_element")

Added before v1.9
jsHandle.as_element

Returns either `null` or the object handle itself, if the object handle is an instance of [ElementHandle](Elementhandle.md).

**Usage**

```
js_handle.as_element()
```

**Returns**

* NoneType | [ElementHandle](Elementhandle.md)
