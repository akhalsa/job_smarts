# ElementHandle

Source: https://playwright.dev/python/docs/api/class-elementhandle

---

* extends: [JSHandle](Jshandle.md)

ElementHandle represents an in-page DOM element. ElementHandles can be created with the [page.query_selector()](Page.md) method.

Discouraged

The use of ElementHandle is discouraged, use [Locator](Locator.md) objects and web-first assertions instead.

* Sync* Async

```
href_element = page.query_selector("a")  
href_element.click()
```

```
href_element = await page.query_selector("a")  
await href_element.click()
```

ElementHandle prevents DOM element from garbage collection unless the handle is disposed with [js_handle.dispose()](Jshandle.md). ElementHandles are auto-disposed when their origin frame gets navigated.

ElementHandle instances can be used as an argument in [page.eval_on_selector()](Page.md) and [page.evaluate()](Page.md) methods.

The difference between the [Locator](Locator.md) and ElementHandle is that the ElementHandle points to a particular element, while [Locator](Locator.md) captures the logic of how to retrieve an element.

In the example below, handle points to a particular DOM element on page. If that element changes text or is used by React to render an entirely different component, handle is still pointing to that very DOM element. This can lead to unexpected behaviors.

* Sync* Async

```
handle = page.query_selector("text=Submit")  
handle.hover()  
handle.click()
```

```
handle = await page.query_selector("text=Submit")  
await handle.hover()  
await handle.click()
```

With the locator, every time the `element` is used, up-to-date DOM element is located in the page using the selector. So in the snippet below, underlying DOM element is going to be located twice.

* Sync* Async

```
locator = page.get_by_text("Submit")  
locator.hover()  
locator.click()
```

```
locator = page.get_by_text("Submit")  
await locator.hover()  
await locator.click()
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### bounding_box[​](#element-handle-bounding-box "Direct link to bounding_box")

Added before v1.9
elementHandle.bounding_box

This method returns the bounding box of the element, or `null` if the element is not visible. The bounding box is calculated relative to the main frame viewport - which is usually the same as the browser window.

Scrolling affects the returned bounding box, similarly to [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). That means `x` and/or `y` may be negative.

Elements from child frames return the bounding box relative to the main frame, unlike the [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the following snippet should click the center of the element.

**Usage**

* Sync* Async

```
box = element_handle.bounding_box()  
page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

```
box = await element_handle.bounding_box()  
await page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

**Returns**

* NoneType | Dict
  + `x` float

    the x coordinate of the element in pixels.
  + `y` float

    the y coordinate of the element in pixels.
  + `width` float

    the width of the element in pixels.
  + `height` float

    the height of the element in pixels.

---

### content_frame[​](#element-handle-content-frame "Direct link to content_frame")

Added before v1.9
elementHandle.content_frame

Returns the content frame for element handles referencing iframe nodes, or `null` otherwise

**Usage**

```
element_handle.content_frame()
```

**Returns**

* NoneType | [Frame](Frame.md)

---

### owner_frame[​](#element-handle-owner-frame "Direct link to owner_frame")

Added before v1.9
elementHandle.owner_frame

Returns the frame containing the given element.

**Usage**

```
element_handle.owner_frame()
```

**Returns**

* NoneType | [Frame](Frame.md)

---

### wait_for_element_state[​](#element-handle-wait-for-element-state "Direct link to wait_for_element_state")

Added before v1.9
elementHandle.wait_for_element_state

Returns when the element satisfies the [state](Elementhandle.md).

Depending on the [state](Elementhandle.md) parameter, this method waits for one of the [actionability](/python/docs/actionability) checks to pass. This method throws when the element is detached while waiting, unless waiting for the `"hidden"` state.

* `"visible"` Wait until the element is [visible](/python/docs/actionability#visible).
* `"hidden"` Wait until the element is [not visible](/python/docs/actionability#visible) or not attached. Note that waiting for hidden does not throw when the element detaches.
* `"stable"` Wait until the element is both [visible](/python/docs/actionability#visible) and [stable](/python/docs/actionability#stable).
* `"enabled"` Wait until the element is [enabled](/python/docs/actionability#enabled).
* `"disabled"` Wait until the element is [not enabled](/python/docs/actionability#enabled).
* `"editable"` Wait until the element is [editable](/python/docs/actionability#editable).

If the element does not satisfy the condition for the [timeout](Elementhandle.md) milliseconds, this method will throw.

**Usage**

```
element_handle.wait_for_element_state(state)  
element_handle.wait_for_element_state(state, **kwargs)
```

**Arguments**

* `state` "visible" | "hidden" | "stable" | "enabled" | "disabled" | "editable"

  A state to wait for, see below for more details.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

Deprecated[​](#deprecated "Direct link to Deprecated")
------------------------------------------------------

### check[​](#element-handle-check "Direct link to check")

Added before v1.9
elementHandle.check

Discouraged

Use locator-based [locator.check()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method checks the element by performing the following steps:

1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already checked, this method returns immediately.
2. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Elementhandle.md) option is set.
3. Scroll the element into view if needed.
4. Use [page.mouse](Page.md) to click in the center of the element.
5. Ensure that the element is now checked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Elementhandle.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
element_handle.check()  
element_handle.check(**kwargs)
```

**Arguments**

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
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### click[​](#element-handle-click "Direct link to click")

Added before v1.9
elementHandle.click

Discouraged

Use locator-based [locator.click()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method clicks the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Elementhandle.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.mouse](Page.md) to click in the center of the element, or the specified [position](Elementhandle.md).
4. Wait for initiated navigations to either succeed or fail, unless [no_wait_after](Elementhandle.md) option is set.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Elementhandle.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
element_handle.click()  
element_handle.click(**kwargs)
```

**Arguments**

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
* `steps` int *(optional)* 

  Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### dblclick[​](#element-handle-dblclick "Direct link to dblclick")

Added before v1.9
elementHandle.dblclick

Discouraged

Use locator-based [locator.dblclick()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method double clicks the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Elementhandle.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.mouse](Page.md) to double click in the center of the element, or the specified [position](Elementhandle.md).

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Elementhandle.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

note

`elementHandle.dblclick()` dispatches two `click` events and a single `dblclick` event.

**Usage**

```
element_handle.dblclick()  
element_handle.dblclick(**kwargs)
```

**Arguments**

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
* `steps` int *(optional)* 

  Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### dispatch_event[​](#element-handle-dispatch-event "Direct link to dispatch_event")

Added before v1.9
elementHandle.dispatch_event

Discouraged

Use locator-based [locator.dispatch_event()](Locator.md) instead. Read more about [locators](/python/docs/locators).

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element, `click` is dispatched. This is equivalent to calling [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

* Sync* Async

```
element_handle.dispatch_event("click")
```

```
await element_handle.dispatch_event("click")
```

Under the hood, it creates an instance of an event based on the given [type](Elementhandle.md), initializes it with [event_init](Elementhandle.md) properties and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

Since [event_init](Elementhandle.md) is event-specific, please refer to the events documentation for the lists of initial properties:

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
element_handle.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

```
# note you can only create data_transfer in chromium and firefox  
data_transfer = await page.evaluate_handle("new DataTransfer()")  
await element_handle.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

**Arguments**

* `type` str

  DOM event type: `"click"`, `"dragstart"`, etc.
* `event_init` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional event-specific initialization properties.

**Returns**

* NoneType

---

### eval_on_selector[​](#element-handle-eval-on-selector "Direct link to eval_on_selector") elementHandle.eval_on_selector

Discouraged

This method does not wait for the element to pass actionability checks and therefore can lead to the flaky tests. Use [locator.evaluate()](Locator.md), other [Locator](Locator.md) helper methods or web-first assertions instead.

Returns the return value of [expression](Elementhandle.md).

The method finds an element matching the specified selector in the `ElementHandle`s subtree and passes it as a first argument to [expression](Elementhandle.md). If no elements match the selector, the method throws an error.

If [expression](Elementhandle.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [element_handle.eval_on_selector()](Elementhandle.md) would wait for the promise to resolve and return its value.

**Usage**

* Sync* Async

```
tweet_handle = page.query_selector(".tweet")  
assert tweet_handle.eval_on_selector(".like", "node => node.innerText") == "100"  
assert tweet_handle.eval_on_selector(".retweets", "node => node.innerText") == "10"
```

```
tweet_handle = await page.query_selector(".tweet")  
assert await tweet_handle.eval_on_selector(".like", "node => node.innerText") == "100"  
assert await tweet_handle.eval_on_selector(".retweets", "node => node.innerText") == "10"
```

**Arguments**

* `selector` str

  A selector to query for.
* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Elementhandle.md).

**Returns**

* Dict

---

### eval_on_selector_all[​](#element-handle-eval-on-selector-all "Direct link to eval_on_selector_all") elementHandle.eval_on_selector_all

Discouraged

In most cases, [locator.evaluate_all()](Locator.md), other [Locator](Locator.md) helper methods and web-first assertions do a better job.

Returns the return value of [expression](Elementhandle.md).

The method finds all elements matching the specified selector in the `ElementHandle`'s subtree and passes an array of matched elements as a first argument to [expression](Elementhandle.md).

If [expression](Elementhandle.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), then [element_handle.eval_on_selector_all()](Elementhandle.md) would wait for the promise to resolve and return its value.

**Usage**

```
<div class="feed">  
  <div class="tweet">Hello!</div>  
  <div class="tweet">Hi!</div>  
</div>
```

* Sync* Async

```
feed_handle = page.query_selector(".feed")  
assert feed_handle.eval_on_selector_all(".tweet", "nodes => nodes.map(n => n.innerText)") == ["hello!", "hi!"]
```

```
feed_handle = await page.query_selector(".feed")  
assert await feed_handle.eval_on_selector_all(".tweet", "nodes => nodes.map(n => n.innerText)") == ["hello!", "hi!"]
```

**Arguments**

* `selector` str

  A selector to query for.
* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Elementhandle.md).

**Returns**

* Dict

---

### fill[​](#element-handle-fill "Direct link to fill")

Added before v1.9
elementHandle.fill

Discouraged

Use locator-based [locator.fill()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method waits for [actionability](/python/docs/actionability) checks, focuses the element, fills it and triggers an `input` event after filling. Note that you can pass an empty string to clear the input field.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled instead.

To send fine-grained keyboard events, use [locator.press_sequentially()](Locator.md).

**Usage**

```
element_handle.fill(value)  
element_handle.fill(value, **kwargs)
```

**Arguments**

* `value` str

  Value to set for the `<input>`, `<textarea>` or `[contenteditable]` element.
* `force` bool *(optional)* 

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### focus[​](#element-handle-focus "Direct link to focus")

Added before v1.9
elementHandle.focus

Discouraged

Use locator-based [locator.focus()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element.

**Usage**

```
element_handle.focus()
```

**Returns**

* NoneType

---

### get_attribute[​](#element-handle-get-attribute "Direct link to get_attribute")

Added before v1.9
elementHandle.get_attribute

Discouraged

Use locator-based [locator.get_attribute()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns element attribute value.

**Usage**

```
element_handle.get_attribute(name)
```

**Arguments**

* `name` str

  Attribute name to get the value for.

**Returns**

* NoneType | str

---

### hover[​](#element-handle-hover "Direct link to hover")

Added before v1.9
elementHandle.hover

Discouraged

Use locator-based [locator.hover()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method hovers over the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Elementhandle.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.mouse](Page.md) to hover over the center of the element, or the specified [position](Elementhandle.md).

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Elementhandle.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
element_handle.hover()  
element_handle.hover(**kwargs)
```

**Arguments**

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
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### inner_html[​](#element-handle-inner-html "Direct link to inner_html")

Added before v1.9
elementHandle.inner_html

Discouraged

Use locator-based [locator.inner_html()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns the `element.innerHTML`.

**Usage**

```
element_handle.inner_html()
```

**Returns**

* str

---

### inner_text[​](#element-handle-inner-text "Direct link to inner_text")

Added before v1.9
elementHandle.inner_text

Discouraged

Use locator-based [locator.inner_text()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns the `element.innerText`.

**Usage**

```
element_handle.inner_text()
```

**Returns**

* str

---

### input_value[​](#element-handle-input-value "Direct link to input_value") elementHandle.input_value

Discouraged

Use locator-based [locator.input_value()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns `input.value` for the selected `<input>` or `<textarea>` or `<select>` element.

Throws for non-input elements. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the control.

**Usage**

```
element_handle.input_value()  
element_handle.input_value(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

---

### is_checked[​](#element-handle-is-checked "Direct link to is_checked")

Added before v1.9
elementHandle.is_checked

Discouraged

Use locator-based [locator.is_checked()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

**Usage**

```
element_handle.is_checked()
```

**Returns**

* bool

---

### is_disabled[​](#element-handle-is-disabled "Direct link to is_disabled")

Added before v1.9
elementHandle.is_disabled

Discouraged

Use locator-based [locator.is_disabled()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is disabled, the opposite of [enabled](/python/docs/actionability#enabled).

**Usage**

```
element_handle.is_disabled()
```

**Returns**

* bool

---

### is_editable[​](#element-handle-is-editable "Direct link to is_editable")

Added before v1.9
elementHandle.is_editable

Discouraged

Use locator-based [locator.is_editable()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is [editable](/python/docs/actionability#editable).

**Usage**

```
element_handle.is_editable()
```

**Returns**

* bool

---

### is_enabled[​](#element-handle-is-enabled "Direct link to is_enabled")

Added before v1.9
elementHandle.is_enabled

Discouraged

Use locator-based [locator.is_enabled()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is [enabled](/python/docs/actionability#enabled).

**Usage**

```
element_handle.is_enabled()
```

**Returns**

* bool

---

### is_hidden[​](#element-handle-is-hidden "Direct link to is_hidden")

Added before v1.9
elementHandle.is_hidden

Discouraged

Use locator-based [locator.is_hidden()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is hidden, the opposite of [visible](/python/docs/actionability#visible).

**Usage**

```
element_handle.is_hidden()
```

**Returns**

* bool

---

### is_visible[​](#element-handle-is-visible "Direct link to is_visible")

Added before v1.9
elementHandle.is_visible

Discouraged

Use locator-based [locator.is_visible()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns whether the element is [visible](/python/docs/actionability#visible).

**Usage**

```
element_handle.is_visible()
```

**Returns**

* bool

---

### press[​](#element-handle-press "Direct link to press")

Added before v1.9
elementHandle.press

Discouraged

Use locator-based [locator.press()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Focuses the element, and then uses [keyboard.down()](Keyboard.md) and [keyboard.up()](Keyboard.md).

[key](Elementhandle.md) can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character to generate the text for. A superset of the [key](Elementhandle.md) values can be found [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`.

Holding down `Shift` will type the text that corresponds to the [key](Elementhandle.md) in the upper case.

If [key](Elementhandle.md) is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

**Usage**

```
element_handle.press(key)  
element_handle.press(key, **kwargs)
```

**Arguments**

* `key` str

  Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
* `delay` float *(optional)*

  Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option will default to `true` in the future.

  Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### query_selector[​](#element-handle-query-selector "Direct link to query_selector") elementHandle.query_selector

Discouraged

Use locator-based [page.locator()](Page.md) instead. Read more about [locators](/python/docs/locators).

The method finds an element matching the specified selector in the `ElementHandle`'s subtree. If no elements match the selector, returns `null`.

**Usage**

```
element_handle.query_selector(selector)
```

**Arguments**

* `selector` str

  A selector to query for.

**Returns**

* NoneType | [ElementHandle](Elementhandle.md)

---

### query_selector_all[​](#element-handle-query-selector-all "Direct link to query_selector_all") elementHandle.query_selector_all

Discouraged

Use locator-based [page.locator()](Page.md) instead. Read more about [locators](/python/docs/locators).

The method finds all elements matching the specified selector in the `ElementHandle`s subtree. If no elements match the selector, returns empty array.

**Usage**

```
element_handle.query_selector_all(selector)
```

**Arguments**

* `selector` str

  A selector to query for.

**Returns**

* List[[ElementHandle](Elementhandle.md)]

---

### screenshot[​](#element-handle-screenshot "Direct link to screenshot")

Added before v1.9
elementHandle.screenshot

Discouraged

Use locator-based [locator.screenshot()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method captures a screenshot of the page, clipped to the size and position of this particular element. If the element is covered by other elements, it will not be actually visible on the screenshot. If the element is a scrollable container, only the currently scrolled content will be visible on the screenshot.

This method waits for the [actionability](/python/docs/actionability) checks, then scrolls element into view before taking a screenshot. If the element is detached from DOM, the method throws an error.

Returns the buffer with the captured screenshot.

**Usage**

```
element_handle.screenshot()  
element_handle.screenshot(**kwargs)
```

**Arguments**

* `animations` "disabled" | "allow" *(optional)*

  When set to `"disabled"`, stops CSS animations, CSS transitions and Web Animations. Animations get different treatment depending on their duration:

  + finite animations are fast-forwarded to completion, so they'll fire `transitionend` event.
  + infinite animations are canceled to initial state, and then played over after the screenshot.

  Defaults to `"allow"` that leaves animations untouched.
* `caret` "hide" | "initial" *(optional)*

  When set to `"hide"`, screenshot will hide text caret. When set to `"initial"`, text caret behavior will not be changed. Defaults to `"hide"`.
* `mask` List[[Locator](Locator.md)] *(optional)*

  Specify locators that should be masked when the screenshot is taken. Masked elements will be overlaid with a pink box `#FF00FF` (customized by [mask_color](Elementhandle.md)) that completely covers its bounding box. The mask is also applied to invisible elements, see [Matching only visible elements](/python/docs/locators#matching-only-visible-elements) to disable that.
* `mask_color` str *(optional)* 

  Specify the color of the overlay box for masked elements, in [CSS color format](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value). Default color is pink `#FF00FF`.
* `omit_background` bool *(optional)*

  Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images. Defaults to `false`.
* `path` Union[str, pathlib.Path] *(optional)*

  The file path to save the image to. The screenshot type will be inferred from file extension. If [path](Elementhandle.md) is a relative path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to the disk.
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

### scroll_into_view_if_needed[​](#element-handle-scroll-into-view-if-needed "Direct link to scroll_into_view_if_needed")

Added before v1.9
elementHandle.scroll_into_view_if_needed

Discouraged

Use locator-based [locator.scroll_into_view_if_needed()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method waits for [actionability](/python/docs/actionability) checks, then tries to scroll element into view, unless it is completely visible as defined by [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s `ratio`.

Throws when `elementHandle` does not point to an element [connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

See [scrolling](/python/docs/input#scrolling) for alternative ways to scroll.

**Usage**

```
element_handle.scroll_into_view_if_needed()  
element_handle.scroll_into_view_if_needed(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### select_option[​](#element-handle-select-option "Direct link to select_option")

Added before v1.9
elementHandle.select_option

Discouraged

Use locator-based [locator.select_option()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method waits for [actionability](/python/docs/actionability) checks, waits until all specified options are present in the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

* Sync* Async

```
# Single selection matching the value or label  
handle.select_option("blue")  
# single selection matching both the label  
handle.select_option(label="blue")  
# multiple selection  
handle.select_option(value=["red", "green", "blue"])
```

```
# Single selection matching the value or label  
await handle.select_option("blue")  
# single selection matching the label  
await handle.select_option(label="blue")  
# multiple selection  
await handle.select_option(value=["red", "green", "blue"])
```

**Arguments**

* `force` bool *(optional)* 

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
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

### select_text[​](#element-handle-select-text "Direct link to select_text")

Added before v1.9
elementHandle.select_text

Discouraged

Use locator-based [locator.select_text()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method waits for [actionability](/python/docs/actionability) checks, then focuses the element and selects all its text content.

If the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), focuses and selects text in the control instead.

**Usage**

```
element_handle.select_text()  
element_handle.select_text(**kwargs)
```

**Arguments**

* `force` bool *(optional)* 

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### set_checked[​](#element-handle-set-checked "Direct link to set_checked") elementHandle.set_checked

Discouraged

Use locator-based [locator.set_checked()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method checks or unchecks an element by performing the following steps:

1. Ensure that element is a checkbox or a radio input. If not, this method throws.
2. If the element already has the right checked state, this method returns immediately.
3. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Elementhandle.md) option is set. If the element is detached during the checks, the whole action is retried.
4. Scroll the element into view if needed.
5. Use [page.mouse](Page.md) to click in the center of the element.
6. Ensure that the element is now checked or unchecked. If not, this method throws.

When all steps combined have not finished during the specified [timeout](Elementhandle.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
element_handle.set_checked(checked)  
element_handle.set_checked(checked, **kwargs)
```

**Arguments**

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
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)*

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### set_input_files[​](#element-handle-set-input-files "Direct link to set_input_files")

Added before v1.9
elementHandle.set_input_files

Discouraged

Use locator-based [locator.set_input_files()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they are resolved relative to the current working directory. For empty array, clears the selected files. For inputs with a `[webkitdirectory]` attribute, only a single directory path is supported.

This method expects [ElementHandle](Elementhandle.md) to point to an [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

**Usage**

```
element_handle.set_input_files(files)  
element_handle.set_input_files(files, **kwargs)
```

**Arguments**

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
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### tap[​](#element-handle-tap "Direct link to tap")

Added before v1.9
elementHandle.tap

Discouraged

Use locator-based [locator.tap()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method taps the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Elementhandle.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.touchscreen](Page.md) to tap the center of the element, or the specified [position](Elementhandle.md).

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Elementhandle.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

note

`elementHandle.tap()` requires that the `hasTouch` option of the browser context be set to true.

**Usage**

```
element_handle.tap()  
element_handle.tap(**kwargs)
```

**Arguments**

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
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### text_content[​](#element-handle-text-content "Direct link to text_content")

Added before v1.9
elementHandle.text_content

Discouraged

Use locator-based [locator.text_content()](Locator.md) instead. Read more about [locators](/python/docs/locators).

Returns the `node.textContent`.

**Usage**

```
element_handle.text_content()
```

**Returns**

* NoneType | str

---

### type[​](#element-handle-type "Direct link to type")

Added before v1.9
elementHandle.type

Deprecated

In most cases, you should use [locator.fill()](Locator.md) instead. You only need to press keys one by one if there is special keyboard handling on the page - in this case use [locator.press_sequentially()](Locator.md).

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

To press a special key, like `Control` or `ArrowDown`, use [element_handle.press()](Elementhandle.md).

**Usage**

**Arguments**

* `text` str

  A text to type into a focused element.
* `delay` float *(optional)*

  Time to wait between key presses in milliseconds. Defaults to 0.
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### uncheck[​](#element-handle-uncheck "Direct link to uncheck")

Added before v1.9
elementHandle.uncheck

Discouraged

Use locator-based [locator.uncheck()](Locator.md) instead. Read more about [locators](/python/docs/locators).

This method checks the element by performing the following steps:

1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already unchecked, this method returns immediately.
2. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Elementhandle.md) option is set.
3. Scroll the element into view if needed.
4. Use [page.mouse](Page.md) to click in the center of the element.
5. Ensure that the element is now unchecked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Elementhandle.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

**Usage**

```
element_handle.uncheck()  
element_handle.uncheck(**kwargs)
```

**Arguments**

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
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.
* `trial` bool *(optional)* 

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

**Returns**

* NoneType

---

### wait_for_selector[​](#element-handle-wait-for-selector "Direct link to wait_for_selector")

Added before v1.9
elementHandle.wait_for_selector

Discouraged

Use web assertions that assert visibility or a locator-based [locator.wait_for()](Locator.md) instead.

Returns element specified by selector when it satisfies [state](Elementhandle.md) option. Returns `null` if waiting for `hidden` or `detached`.

Wait for the [selector](Elementhandle.md) relative to the element handle to satisfy [state](Elementhandle.md) option (either appear/disappear from dom, or become visible/hidden). If at the moment of calling the method [selector](Elementhandle.md) already satisfies the condition, the method will return immediately. If the selector doesn't satisfy the condition for the [timeout](Elementhandle.md) milliseconds, the function will throw.

**Usage**

* Sync* Async

```
page.set_content("<div><span></span></div>")  
div = page.query_selector("div")  
# waiting for the "span" selector relative to the div.  
span = div.wait_for_selector("span", state="attached")
```

```
await page.set_content("<div><span></span></div>")  
div = await page.query_selector("div")  
# waiting for the "span" selector relative to the div.  
span = await div.wait_for_selector("span", state="attached")
```

note

This method does not work across navigations, use [page.wait_for_selector()](Page.md) instead.

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
