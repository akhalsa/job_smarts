# Locator

Source: https://playwright.dev/python/docs/api/class-locator

---

Locators are the central piece of Playwright's auto-waiting and retry-ability. In a nutshell, locators represent a way to find element(s) on the page at any moment. A locator can be created with the [page.locator()](Page.md) method.

[Learn more about locators](/python/docs/locators).

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### all[​](#locator-all "Direct link to all") locator.all

When the locator points to a list of elements, this returns an array of locators, pointing to their respective elements.

note

[locator.all()](Locator.md) does not wait for elements to match the locator, and instead immediately returns whatever is present in the page.

When the list of elements changes dynamically, [locator.all()](Locator.md) will produce unpredictable and flaky results.

When the list of elements is stable, but loaded dynamically, wait for the full list to finish loading before calling [locator.all()](Locator.md).

**Usage**

* Sync* Async

```
for li in page.get_by_role('listitem').all():  
  li.click();
```

```
for li in await page.get_by_role('listitem').all():  
  await li.click();
```

**Returns**

* List[[Locator](Locator.md)]

---

### all_inner_texts[​](#locator-all-inner-texts "Direct link to all_inner_texts") locator.all_inner_texts

Returns an array of `node.innerText` values for all matching nodes.

Asserting text

If you need to assert text on the page, prefer [expect(locator).to_have_text()](Locatorassertions.md) with [use_inner_text](Locatorassertions.md) option to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
texts = page.get_by_role("link").all_inner_texts()
```

```
texts = await page.get_by_role("link").all_inner_texts()
```

**Returns**

* List[str]

---

### all_text_contents[​](#locator-all-text-contents "Direct link to all_text_contents") locator.all_text_contents

Returns an array of `node.textContent` values for all matching nodes.

Asserting text

If you need to assert text on the page, prefer [expect(locator).to_have_text()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
texts = page.get_by_role("link").all_text_contents()
```

```
texts = await page.get_by_role("link").all_text_contents()
```

**Returns**

* List[str]

---

### and_[​](#locator-and "Direct link to and_") locator.and_

Creates a locator that matches both this locator and the argument locator.

**Usage**

The following example finds a button with a specific title.

* Sync* Async

```
button = page.get_by_role("button").and_(page.get_by_title("Subscribe"))
```

```
button = page.get_by_role("button").and_(page.get_by_title("Subscribe"))
```

**Arguments**

* `locator` [Locator](Locator.md)

  Additional locator to match.

**Returns**

* [Locator](Locator.md)

---

### aria_snapshot[​](#locator-aria-snapshot "Direct link to aria_snapshot") locator.aria_snapshot

Captures the aria snapshot of the given element. Read more about [aria snapshots](/python/docs/aria-snapshots) and [expect(locator).to_match_aria_snapshot()](Locatorassertions.md) for the corresponding assertion.

**Usage**

* Sync* Async

```
page.get_by_role("link").aria_snapshot()
```

```
await page.get_by_role("link").aria_snapshot()
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

**Details**

This method captures the aria snapshot of the given element. The snapshot is a string that represents the state of the element and its children. The snapshot can be used to assert the state of the element in the test, or to compare it to state in the future.

The ARIA snapshot is represented using [YAML](https://yaml.org/spec/1.2.2/) markup language:

* The keys of the objects are the roles and optional accessible names of the elements.
* The values are either text content or an array of child elements.
* Generic static text can be represented with the `text` key.

Below is the HTML markup and the respective ARIA snapshot:

```
<ul aria-label="Links">  
  <li><a href="/">Home</a></li>  
  <li><a href="/about">About</a></li>  
<ul>
```

```
- list "Links":  
  - listitem:  
    - link "Home"  
  - listitem:  
    - link "About"
```

---

### blur[​](#locator-blur "Direct link to blur") locator.blur

Calls [blur](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/blur) on the element.

**Usage**

```
locator.blur()  
locator.blur(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### bounding_box[​](#locator-bounding-box "Direct link to bounding_box") locator.bounding_box

This method returns the bounding box of the element matching the locator, or `null` if the element is not visible. The bounding box is calculated relative to the main frame viewport - which is usually the same as the browser window.

**Usage**

* Sync* Async

```
box = page.get_by_role("button").bounding_box()  
page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

```
box = await page.get_by_role("button").bounding_box()  
await page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

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

**Details**

Scrolling affects the returned bounding box, similarly to [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). That means `x` and/or `y` may be negative.

Elements from child frames return the bounding box relative to the main frame, unlike the [Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the following snippet should click the center of the element.

---

### check[​](#locator-check "Direct link to check") locator.check

Ensure that checkbox or radio element is checked.

**Usage**

* Sync* Async

```
page.get_by_role("checkbox").check()
```

```
await page.get_by_role("checkbox").check()
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

**Details**

Performs the following steps:

1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already checked, this method returns immediately.
2. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Locator.md) option is set.
3. Scroll the element into view if needed.
4. Use [page.mouse](Page.md) to click in the center of the element.
5. Ensure that the element is now checked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Locator.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

---

### clear[​](#locator-clear "Direct link to clear") locator.clear

Clear the input field.

**Usage**

* Sync* Async

```
page.get_by_role("textbox").clear()
```

```
await page.get_by_role("textbox").clear()
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

**Returns**

* NoneType

**Details**

This method waits for [actionability](/python/docs/actionability) checks, focuses the element, clears it and triggers an `input` event after clearing.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be cleared instead.

---

### click[​](#locator-click "Direct link to click") locator.click

Click an element.

**Usage**

Click a button:

* Sync* Async

```
page.get_by_role("button").click()
```

```
await page.get_by_role("button").click()
```

Shift-right-click at a specific position on a canvas:

* Sync* Async

```
page.locator("canvas").click(  
    button="right", modifiers=["Shift"], position={"x": 23, "y": 32}  
)
```

```
await page.locator("canvas").click(  
    button="right", modifiers=["Shift"], position={"x": 23, "y": 32}  
)
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

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

**Details**

This method clicks the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Locator.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.mouse](Page.md) to click in the center of the element, or the specified [position](Locator.md).
4. Wait for initiated navigations to either succeed or fail, unless [no_wait_after](Locator.md) option is set.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Locator.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

---

### count[​](#locator-count "Direct link to count") locator.count

Returns the number of elements matching the locator.

Asserting count

If you need to assert the number of elements on the page, prefer [expect(locator).to_have_count()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
count = page.get_by_role("listitem").count()
```

```
count = await page.get_by_role("listitem").count()
```

**Returns**

* int

---

### dblclick[​](#locator-dblclick "Direct link to dblclick") locator.dblclick

Double-click an element.

**Usage**

```
locator.dblclick()  
locator.dblclick(**kwargs)
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

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

**Details**

This method double clicks the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Locator.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.mouse](Page.md) to double click in the center of the element, or the specified [position](Locator.md).

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Locator.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

note

`element.dblclick()` dispatches two `click` events and a single `dblclick` event.

---

### describe[​](#locator-describe "Direct link to describe") locator.describe

Describes the locator, description is used in the trace viewer and reports. Returns the locator pointing to the same element.

**Usage**

* Sync* Async

```
button = page.get_by_test_id("btn-sub").describe("Subscribe button")  
button.click()
```

```
button = page.get_by_test_id("btn-sub").describe("Subscribe button")  
await button.click()
```

**Arguments**

* `description` str

  Locator description.

**Returns**

* [Locator](Locator.md)

---

### dispatch_event[​](#locator-dispatch-event "Direct link to dispatch_event") locator.dispatch_event

Programmatically dispatch an event on the matching element.

**Usage**

* Sync* Async

```
locator.dispatch_event("click")
```

```
await locator.dispatch_event("click")
```

**Arguments**

* `type` str

  DOM event type: `"click"`, `"dragstart"`, etc.
* `event_init` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional event-specific initialization properties.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

**Details**

The snippet above dispatches the `click` event on the element. Regardless of the visibility state of the element, `click` is dispatched. This is equivalent to calling [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

Under the hood, it creates an instance of an event based on the given [type](Locator.md), initializes it with [event_init](Locator.md) properties and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

Since [event_init](Locator.md) is event-specific, please refer to the events documentation for the lists of initial properties:

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

You can also specify [JSHandle](Jshandle.md) as the property value if you want live objects to be passed into the event:

* Sync* Async

```
data_transfer = page.evaluate_handle("new DataTransfer()")  
locator.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

```
data_transfer = await page.evaluate_handle("new DataTransfer()")  
await locator.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

---

### drag_to[​](#locator-drag-to "Direct link to drag_to") locator.drag_to

Drag the source element towards the target element and drop it.

**Usage**

* Sync* Async

```
source = page.locator("#source")  
target = page.locator("#target")  
  
source.drag_to(target)  
# or specify exact positions relative to the top-left corners of the elements:  
source.drag_to(  
  target,  
  source_position={"x": 34, "y": 7},  
  target_position={"x": 10, "y": 20}  
)
```

```
source = page.locator("#source")  
target = page.locator("#target")  
  
await source.drag_to(target)  
# or specify exact positions relative to the top-left corners of the elements:  
await source.drag_to(  
  target,  
  source_position={"x": 34, "y": 7},  
  target_position={"x": 10, "y": 20}  
)
```

**Arguments**

* `target` [Locator](Locator.md)

  Locator of the element to drag to.
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

**Details**

This method drags the locator to another target locator or target position. It will first move to the source element, perform a `mousedown`, then move to the target element or position and perform a `mouseup`.

---

### evaluate[​](#locator-evaluate "Direct link to evaluate") locator.evaluate

Execute JavaScript code in the page, taking the matching element as an argument.

**Usage**

Passing argument to [expression](Locator.md):

* Sync* Async

```
result = page.get_by_testid("myId").evaluate("(element, [x, y]) => element.textContent + ' ' + x * y", [7, 8])  
print(result) # prints "myId text 56"
```

```
result = await page.get_by_testid("myId").evaluate("(element, [x, y]) => element.textContent + ' ' + x * y", [7, 8])  
print(result) # prints "myId text 56"
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Locator.md).
* `timeout` float *(optional)*

  Maximum time in milliseconds to wait for the locator before evaluating. Note that after locator is resolved, evaluation itself is not limited by the timeout. Defaults to `30000` (30 seconds). Pass `0` to disable timeout.

**Returns**

* Dict

**Details**

Returns the return value of [expression](Locator.md), called with the matching element as a first argument, and [arg](Locator.md) as a second argument.

If [expression](Locator.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), this method will wait for the promise to resolve and return its value.

If [expression](Locator.md) throws or rejects, this method throws.

---

### evaluate_all[​](#locator-evaluate-all "Direct link to evaluate_all") locator.evaluate_all

Execute JavaScript code in the page, taking all matching elements as an argument.

**Usage**

* Sync* Async

```
locator = page.locator("div")  
more_than_ten = locator.evaluate_all("(divs, min) => divs.length > min", 10)
```

```
locator = page.locator("div")  
more_than_ten = await locator.evaluate_all("(divs, min) => divs.length > min", 10)
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Locator.md).

**Returns**

* Dict

**Details**

Returns the return value of [expression](Locator.md), called with an array of all matching elements as a first argument, and [arg](Locator.md) as a second argument.

If [expression](Locator.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), this method will wait for the promise to resolve and return its value.

If [expression](Locator.md) throws or rejects, this method throws.

---

### evaluate_handle[​](#locator-evaluate-handle "Direct link to evaluate_handle") locator.evaluate_handle

Execute JavaScript code in the page, taking the matching element as an argument, and return a [JSHandle](Jshandle.md) with the result.

**Usage**

```
locator.evaluate_handle(expression)  
locator.evaluate_handle(expression, **kwargs)
```

**Arguments**

* `expression` str

  JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked.
* `arg` [EvaluationArgument](/python/docs/evaluating#evaluation-argument "EvaluationArgument") *(optional)*

  Optional argument to pass to [expression](Locator.md).
* `timeout` float *(optional)*

  Maximum time in milliseconds to wait for the locator before evaluating. Note that after locator is resolved, evaluation itself is not limited by the timeout. Defaults to `30000` (30 seconds). Pass `0` to disable timeout.

**Returns**

* [JSHandle](Jshandle.md)

**Details**

Returns the return value of [expression](Locator.md) as a[JSHandle](Jshandle.md), called with the matching element as a first argument, and [arg](Locator.md) as a second argument.

The only difference between [locator.evaluate()](Locator.md) and [locator.evaluate_handle()](Locator.md) is that [locator.evaluate_handle()](Locator.md) returns [JSHandle](Jshandle.md).

If [expression](Locator.md) returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise"), this method will wait for the promise to resolve and return its value.

If [expression](Locator.md) throws or rejects, this method throws.

See [page.evaluate_handle()](Page.md) for more details.

---

### fill[​](#locator-fill "Direct link to fill") locator.fill

Set a value to the input field.

**Usage**

* Sync* Async

```
page.get_by_role("textbox").fill("example value")
```

```
await page.get_by_role("textbox").fill("example value")
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

**Details**

This method waits for [actionability](/python/docs/actionability) checks, focuses the element, fills it and triggers an `input` event after filling. Note that you can pass an empty string to clear the input field.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled instead.

To send fine-grained keyboard events, use [locator.press_sequentially()](Locator.md).

---

### filter[​](#locator-filter "Direct link to filter") locator.filter

This method narrows existing locator according to the options, for example filters by text. It can be chained to filter multiple times.

**Usage**

* Sync* Async

```
row_locator = page.locator("tr")  
# ...  
row_locator.filter(has_text="text in column 1").filter(  
    has=page.get_by_role("button", name="column 2 button")  
).screenshot()
```

```
row_locator = page.locator("tr")  
# ...  
await row_locator.filter(has_text="text in column 1").filter(  
    has=page.get_by_role("button", name="column 2 button")  
).screenshot()
```

**Arguments**

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
* `visible` bool *(optional)* 

  Only matches visible or invisible elements.

**Returns**

* [Locator](Locator.md)

---

### focus[​](#locator-focus "Direct link to focus") locator.focus

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the matching element.

**Usage**

```
locator.focus()  
locator.focus(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### frame_locator[​](#locator-frame-locator "Direct link to frame_locator") locator.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow locating elements in that iframe:

**Usage**

* Sync* Async

```
locator = page.frame_locator("iframe").get_by_text("Submit")  
locator.click()
```

```
locator = page.frame_locator("iframe").get_by_text("Submit")  
await locator.click()
```

**Arguments**

* `selector` str

  A selector to use when resolving DOM element.

**Returns**

* [FrameLocator](Framelocator.md)

---

### get_attribute[​](#locator-get-attribute "Direct link to get_attribute") locator.get_attribute

Returns the matching element's attribute value.

Asserting attributes

If you need to assert an element's attribute, prefer [expect(locator).to_have_attribute()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

```
locator.get_attribute(name)  
locator.get_attribute(name, **kwargs)
```

**Arguments**

* `name` str

  Attribute name to get the value for.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType | str

---

### get_by_alt_text[​](#locator-get-by-alt-text "Direct link to get_by_alt_text") locator.get_by_alt_text

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

### get_by_label[​](#locator-get-by-label "Direct link to get_by_label") locator.get_by_label

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

### get_by_placeholder[​](#locator-get-by-placeholder "Direct link to get_by_placeholder") locator.get_by_placeholder

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

### get_by_role[​](#locator-get-by-role "Direct link to get_by_role") locator.get_by_role

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

  Whether [name](Locator.md) is matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when [name](Locator.md) is a regular expression. Note that exact match still trims whitespace.
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

  Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use [exact](Locator.md) to control this behavior.

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

### get_by_test_id[​](#locator-get-by-test-id "Direct link to get_by_test_id") locator.get_by_test_id

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

### get_by_text[​](#locator-get-by-text "Direct link to get_by_text") locator.get_by_text

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

### get_by_title[​](#locator-get-by-title "Direct link to get_by_title") locator.get_by_title

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

### highlight[​](#locator-highlight "Direct link to highlight") locator.highlight

Highlight the corresponding element(s) on the screen. Useful for debugging, don't commit the code that uses [locator.highlight()](Locator.md).

**Usage**

```
locator.highlight()
```

**Returns**

* NoneType

---

### hover[​](#locator-hover "Direct link to hover") locator.hover

Hover over the matching element.

**Usage**

* Sync* Async

```
page.get_by_role("link").hover()
```

```
await page.get_by_role("link").hover()
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

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

**Details**

This method hovers over the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Locator.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.mouse](Page.md) to hover over the center of the element, or the specified [position](Locator.md).

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Locator.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

---

### inner_html[​](#locator-inner-html "Direct link to inner_html") locator.inner_html

Returns the [`element.innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML).

**Usage**

```
locator.inner_html()  
locator.inner_html(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

---

### inner_text[​](#locator-inner-text "Direct link to inner_text") locator.inner_text

Returns the [`element.innerText`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText).

Asserting text

If you need to assert text on the page, prefer [expect(locator).to_have_text()](Locatorassertions.md) with [use_inner_text](Locatorassertions.md) option to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

```
locator.inner_text()  
locator.inner_text(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

---

### input_value[​](#locator-input-value "Direct link to input_value") locator.input_value

Returns the value for the matching `<input>` or `<textarea>` or `<select>` element.

Asserting value

If you need to assert input value, prefer [expect(locator).to_have_value()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
value = page.get_by_role("textbox").input_value()
```

```
value = await page.get_by_role("textbox").input_value()
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* str

**Details**

Throws elements that are not an input, textarea or a select. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the control.

---

### is_checked[​](#locator-is-checked "Direct link to is_checked") locator.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

Asserting checked state

If you need to assert that checkbox is checked, prefer [expect(locator).to_be_checked()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
checked = page.get_by_role("checkbox").is_checked()
```

```
checked = await page.get_by_role("checkbox").is_checked()
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_disabled[​](#locator-is-disabled "Direct link to is_disabled") locator.is_disabled

Returns whether the element is disabled, the opposite of [enabled](/python/docs/actionability#enabled).

Asserting disabled state

If you need to assert that an element is disabled, prefer [expect(locator).to_be_disabled()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
disabled = page.get_by_role("button").is_disabled()
```

```
disabled = await page.get_by_role("button").is_disabled()
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_editable[​](#locator-is-editable "Direct link to is_editable") locator.is_editable

Returns whether the element is [editable](/python/docs/actionability#editable). If the target element is not an `<input>`, `<textarea>`, `<select>`, `[contenteditable]` and does not have a role allowing `[aria-readonly]`, this method throws an error.

Asserting editable state

If you need to assert that an element is editable, prefer [expect(locator).to_be_editable()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
editable = page.get_by_role("textbox").is_editable()
```

```
editable = await page.get_by_role("textbox").is_editable()
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_enabled[​](#locator-is-enabled "Direct link to is_enabled") locator.is_enabled

Returns whether the element is [enabled](/python/docs/actionability#enabled).

Asserting enabled state

If you need to assert that an element is enabled, prefer [expect(locator).to_be_enabled()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
enabled = page.get_by_role("button").is_enabled()
```

```
enabled = await page.get_by_role("button").is_enabled()
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* bool

---

### is_hidden[​](#locator-is-hidden "Direct link to is_hidden") locator.is_hidden

Returns whether the element is hidden, the opposite of [visible](/python/docs/actionability#visible).

Asserting visibility

If you need to assert that element is hidden, prefer [expect(locator).to_be_hidden()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
hidden = page.get_by_role("button").is_hidden()
```

```
hidden = await page.get_by_role("button").is_hidden()
```

**Arguments**

* `timeout` float *(optional)*

  Deprecated

  This option is ignored. [locator.is_hidden()](Locator.md) does not wait for the element to become hidden and returns immediately.

**Returns**

* bool

---

### is_visible[​](#locator-is-visible "Direct link to is_visible") locator.is_visible

Returns whether the element is [visible](/python/docs/actionability#visible).

Asserting visibility

If you need to assert that element is visible, prefer [expect(locator).to_be_visible()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

* Sync* Async

```
visible = page.get_by_role("button").is_visible()
```

```
visible = await page.get_by_role("button").is_visible()
```

**Arguments**

* `timeout` float *(optional)*

  Deprecated

  This option is ignored. [locator.is_visible()](Locator.md) does not wait for the element to become visible and returns immediately.

**Returns**

* bool

---

### locator[​](#locator-locator "Direct link to locator") locator.locator

The method finds an element matching the specified selector in the locator's subtree. It also accepts filter options, similar to [locator.filter()](Locator.md) method.

[Learn more about locators](/python/docs/locators).

**Usage**

```
locator.locator(selector_or_locator)  
locator.locator(selector_or_locator, **kwargs)
```

**Arguments**

* `selector_or_locator` str | [Locator](Locator.md)

  A selector or locator to use when resolving DOM element.
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

### nth[​](#locator-nth "Direct link to nth") locator.nth

Returns locator to the n-th matching element. It's zero based, `nth(0)` selects the first element.

**Usage**

* Sync* Async

```
banana = page.get_by_role("listitem").nth(2)
```

```
banana = await page.get_by_role("listitem").nth(2)
```

**Arguments**

* `index` int

**Returns**

* [Locator](Locator.md)

---

### or_[​](#locator-or "Direct link to or_") locator.or_

Creates a locator matching all elements that match one or both of the two locators.

Note that when both locators match something, the resulting locator will have multiple matches, potentially causing a [locator strictness](/python/docs/locators#strictness) violation.

**Usage**

Consider a scenario where you'd like to click on a "New email" button, but sometimes a security settings dialog shows up instead. In this case, you can wait for either a "New email" button, or a dialog and act accordingly.

note

If both "New email" button and security dialog appear on screen, the "or" locator will match both of them, possibly throwing the ["strict mode violation" error](/python/docs/locators#strictness). In this case, you can use [locator.first](Locator.md) to only match one of them.

* Sync* Async

```
new_email = page.get_by_role("button", name="New")  
dialog = page.get_by_text("Confirm security settings")  
expect(new_email.or_(dialog).first).to_be_visible()  
if (dialog.is_visible()):  
  page.get_by_role("button", name="Dismiss").click()  
new_email.click()
```

```
new_email = page.get_by_role("button", name="New")  
dialog = page.get_by_text("Confirm security settings")  
await expect(new_email.or_(dialog).first).to_be_visible()  
if (await dialog.is_visible()):  
  await page.get_by_role("button", name="Dismiss").click()  
await new_email.click()
```

**Arguments**

* `locator` [Locator](Locator.md)

  Alternative locator to match.

**Returns**

* [Locator](Locator.md)

---

### press[​](#locator-press "Direct link to press") locator.press

Focuses the matching element and presses a combination of the keys.

**Usage**

* Sync* Async

```
page.get_by_role("textbox").press("Backspace")
```

```
await page.get_by_role("textbox").press("Backspace")
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

**Details**

Focuses the element, and then uses [keyboard.down()](Keyboard.md) and [keyboard.up()](Keyboard.md).

[key](Locator.md) can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character to generate the text for. A superset of the [key](Locator.md) values can be found [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the [key](Locator.md) in the upper case.

If [key](Locator.md) is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

---

### press_sequentially[​](#locator-press-sequentially "Direct link to press_sequentially") locator.press_sequentially

tip

In most cases, you should use [locator.fill()](Locator.md) instead. You only need to press keys one by one if there is special keyboard handling on the page.

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

To press a special key, like `Control` or `ArrowDown`, use [locator.press()](Locator.md).

**Usage**

* Sync* Async

```
locator.press_sequentially("hello") # types instantly  
locator.press_sequentially("world", delay=100) # types slower, like a user
```

```
await locator.press_sequentially("hello") # types instantly  
await locator.press_sequentially("world", delay=100) # types slower, like a user
```

An example of typing into a text field and then submitting the form:

* Sync* Async

```
locator = page.get_by_label("Password")  
locator.press_sequentially("my password")  
locator.press("Enter")
```

```
locator = page.get_by_label("Password")  
await locator.press_sequentially("my password")  
await locator.press("Enter")
```

**Arguments**

* `text` str

  String of characters to sequentially press into a focused element.
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

### screenshot[​](#locator-screenshot "Direct link to screenshot") locator.screenshot

Take a screenshot of the element matching the locator.

**Usage**

* Sync* Async

```
page.get_by_role("link").screenshot()
```

```
await page.get_by_role("link").screenshot()
```

Disable animations and save screenshot to a file:

* Sync* Async

```
page.get_by_role("link").screenshot(animations="disabled", path="link.png")
```

```
await page.get_by_role("link").screenshot(animations="disabled", path="link.png")
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

  Specify locators that should be masked when the screenshot is taken. Masked elements will be overlaid with a pink box `#FF00FF` (customized by [mask_color](Locator.md)) that completely covers its bounding box. The mask is also applied to invisible elements, see [Matching only visible elements](/python/docs/locators#matching-only-visible-elements) to disable that.
* `mask_color` str *(optional)* 

  Specify the color of the overlay box for masked elements, in [CSS color format](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value). Default color is pink `#FF00FF`.
* `omit_background` bool *(optional)*

  Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images. Defaults to `false`.
* `path` Union[str, pathlib.Path] *(optional)*

  The file path to save the image to. The screenshot type will be inferred from file extension. If [path](Locator.md) is a relative path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to the disk.
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

**Details**

This method captures a screenshot of the page, clipped to the size and position of a particular element matching the locator. If the element is covered by other elements, it will not be actually visible on the screenshot. If the element is a scrollable container, only the currently scrolled content will be visible on the screenshot.

This method waits for the [actionability](/python/docs/actionability) checks, then scrolls element into view before taking a screenshot. If the element is detached from DOM, the method throws an error.

Returns the buffer with the captured screenshot.

---

### scroll_into_view_if_needed[​](#locator-scroll-into-view-if-needed "Direct link to scroll_into_view_if_needed") locator.scroll_into_view_if_needed

This method waits for [actionability](/python/docs/actionability) checks, then tries to scroll element into view, unless it is completely visible as defined by [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s `ratio`.

See [scrolling](/python/docs/input#scrolling) for alternative ways to scroll.

**Usage**

```
locator.scroll_into_view_if_needed()  
locator.scroll_into_view_if_needed(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### select_option[​](#locator-select-option "Direct link to select_option") locator.select_option

Selects option or options in `<select>`.

**Usage**

```
<select multiple>  
  <option value="red">Red</option>  
  <option value="green">Green</option>  
  <option value="blue">Blue</option>  
</select>
```

* Sync* Async

```
# single selection matching the value or label  
element.select_option("blue")  
# single selection matching the label  
element.select_option(label="blue")  
# multiple selection for blue, red and second option  
element.select_option(value=["red", "green", "blue"])
```

```
# single selection matching the value or label  
await element.select_option("blue")  
# single selection matching the label  
await element.select_option(label="blue")  
# multiple selection for blue, red and second option  
await element.select_option(value=["red", "green", "blue"])
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

**Details**

This method waits for [actionability](/python/docs/actionability) checks, waits until all specified options are present in the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

---

### select_text[​](#locator-select-text "Direct link to select_text") locator.select_text

This method waits for [actionability](/python/docs/actionability) checks, then focuses the element and selects all its text content.

If the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), focuses and selects text in the control instead.

**Usage**

```
locator.select_text()  
locator.select_text(**kwargs)
```

**Arguments**

* `force` bool *(optional)*

  Whether to bypass the [actionability](/python/docs/actionability) checks. Defaults to `false`.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

### set_checked[​](#locator-set-checked "Direct link to set_checked") locator.set_checked

Set the state of a checkbox or a radio element.

**Usage**

* Sync* Async

```
page.get_by_role("checkbox").set_checked(True)
```

```
await page.get_by_role("checkbox").set_checked(True)
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

**Details**

This method checks or unchecks an element by performing the following steps:

1. Ensure that matched element is a checkbox or a radio input. If not, this method throws.
2. If the element already has the right checked state, this method returns immediately.
3. Wait for [actionability](/python/docs/actionability) checks on the matched element, unless [force](Locator.md) option is set. If the element is detached during the checks, the whole action is retried.
4. Scroll the element into view if needed.
5. Use [page.mouse](Page.md) to click in the center of the element.
6. Ensure that the element is now checked or unchecked. If not, this method throws.

When all steps combined have not finished during the specified [timeout](Locator.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

---

### set_input_files[​](#locator-set-input-files "Direct link to set_input_files") locator.set_input_files

Upload file or multiple files into `<input type=file>`. For inputs with a `[webkitdirectory]` attribute, only a single directory path is supported.

**Usage**

* Sync* Async

```
# Select one file  
page.get_by_label("Upload file").set_input_files('myfile.pdf')  
  
# Select multiple files  
page.get_by_label("Upload files").set_input_files(['file1.txt', 'file2.txt'])  
  
# Select a directory  
page.get_by_label("Upload directory").set_input_files('mydir')  
  
# Remove all the selected files  
page.get_by_label("Upload file").set_input_files([])  
  
# Upload buffer from memory  
page.get_by_label("Upload file").set_input_files(  
    files=[  
        {"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}  
    ],  
)
```

```
# Select one file  
await page.get_by_label("Upload file").set_input_files('myfile.pdf')  
  
# Select multiple files  
await page.get_by_label("Upload files").set_input_files(['file1.txt', 'file2.txt'])  
  
# Select a directory  
await page.get_by_label("Upload directory").set_input_files('mydir')  
  
# Remove all the selected files  
await page.get_by_label("Upload file").set_input_files([])  
  
# Upload buffer from memory  
await page.get_by_label("Upload file").set_input_files(  
    files=[  
        {"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}  
    ],  
)
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

**Details**

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they are resolved relative to the current working directory. For empty array, clears the selected files.

This method expects [Locator](Locator.md) to point to an [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

---

### tap[​](#locator-tap "Direct link to tap") locator.tap

Perform a tap gesture on the element matching the locator. For examples of emulating other gestures by manually dispatching touch events, see the [emulating legacy touch events](/python/docs/touch-events) page.

**Usage**

```
locator.tap()  
locator.tap(**kwargs)
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

  When set, this method only performs the [actionability](/python/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

**Returns**

* NoneType

**Details**

This method taps the element by performing the following steps:

1. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Locator.md) option is set.
2. Scroll the element into view if needed.
3. Use [page.touchscreen](Page.md) to tap the center of the element, or the specified [position](Locator.md).

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Locator.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

note

`element.tap()` requires that the `hasTouch` option of the browser context be set to true.

---

### text_content[​](#locator-text-content "Direct link to text_content") locator.text_content

Returns the [`node.textContent`](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent).

Asserting text

If you need to assert text on the page, prefer [expect(locator).to_have_text()](Locatorassertions.md) to avoid flakiness. See [assertions guide](/python/docs/test-assertions) for more details.

**Usage**

```
locator.text_content()  
locator.text_content(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType | str

---

### uncheck[​](#locator-uncheck "Direct link to uncheck") locator.uncheck

Ensure that checkbox or radio element is unchecked.

**Usage**

* Sync* Async

```
page.get_by_role("checkbox").uncheck()
```

```
await page.get_by_role("checkbox").uncheck()
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

**Details**

This method unchecks the element by performing the following steps:

1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already unchecked, this method returns immediately.
2. Wait for [actionability](/python/docs/actionability) checks on the element, unless [force](Locator.md) option is set.
3. Scroll the element into view if needed.
4. Use [page.mouse](Page.md) to click in the center of the element.
5. Ensure that the element is now unchecked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified [timeout](Locator.md), this method throws a [TimeoutError](Timeouterror.md). Passing zero timeout disables this.

---

### wait_for[​](#locator-wait-for "Direct link to wait_for") locator.wait_for

Returns when element specified by locator satisfies the [state](Locator.md) option.

If target element already satisfies the condition, the method returns immediately. Otherwise, waits for up to [timeout](Locator.md) milliseconds until the condition is met.

**Usage**

* Sync* Async

```
order_sent = page.locator("#order-sent")  
order_sent.wait_for()
```

```
order_sent = page.locator("#order-sent")  
await order_sent.wait_for()
```

**Arguments**

* `state` "attached" | "detached" | "visible" | "hidden" *(optional)*

  Defaults to `'visible'`. Can be either:

  + `'attached'` - wait for element to be present in DOM.
  + `'detached'` - wait for element to not be present in DOM.
  + `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without any content or with `display:none` has an empty bounding box and is not considered visible.
  + `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`. This is opposite to the `'visible'` option.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### content_frame[​](#locator-content-frame "Direct link to content_frame") locator.content_frame

Returns a [FrameLocator](Framelocator.md) object pointing to the same `iframe` as this locator.

Useful when you have a [Locator](Locator.md) object obtained somewhere, and later on would like to interact with the content inside the frame.

For a reverse operation, use [frame_locator.owner](Framelocator.md).

**Usage**

* Sync* Async

```
locator = page.locator("iframe[name=\"embedded\"]")  
# ...  
frame_locator = locator.content_frame  
frame_locator.get_by_role("button").click()
```

```
locator = page.locator("iframe[name=\"embedded\"]")  
# ...  
frame_locator = locator.content_frame  
await frame_locator.get_by_role("button").click()
```

**Returns**

* [FrameLocator](Framelocator.md)

---

### description[​](#locator-description "Direct link to description") locator.description

Returns locator description previously set with [locator.describe()](Locator.md). Returns `null` if no custom description has been set. Prefer `Locator.toString()` for a human-readable representation, as it uses the description when available.

**Usage**

* Sync* Async

```
button = page.get_by_role("button").describe("Subscribe button")  
print(button.description())  # "Subscribe button"  
  
input = page.get_by_role("textbox")  
print(input.description())  # None
```

```
button = page.get_by_role("button").describe("Subscribe button")  
print(button.description())  # "Subscribe button"  
  
input = page.get_by_role("textbox")  
print(input.description())  # None
```

**Returns**

* NoneType | str

---

### first[​](#locator-first "Direct link to first") locator.first

Returns locator to the first matching element.

**Usage**

```
locator.first
```

**Returns**

* [Locator](Locator.md)

---

### last[​](#locator-last "Direct link to last") locator.last

Returns locator to the last matching element.

**Usage**

* Sync* Async

```
banana = page.get_by_role("listitem").last
```

```
banana = await page.get_by_role("listitem").last
```

**Returns**

* [Locator](Locator.md)

---

### page[​](#locator-page "Direct link to page") locator.page

A page this locator belongs to.

**Usage**

```
locator.page
```

**Returns**

* [Page](Page.md)

---

Deprecated[​](#deprecated "Direct link to Deprecated")
------------------------------------------------------

### element_handle[​](#locator-element-handle "Direct link to element_handle") locator.element_handle

Discouraged

Always prefer using [Locator](Locator.md)s and web assertions over [ElementHandle](Elementhandle.md)s because latter are inherently racy.

Resolves given locator to the first matching DOM element. If there are no matching elements, waits for one. If multiple elements match the locator, throws.

**Usage**

```
locator.element_handle()  
locator.element_handle(**kwargs)
```

**Arguments**

* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* [ElementHandle](Elementhandle.md)

---

### element_handles[​](#locator-element-handles "Direct link to element_handles") locator.element_handles

Discouraged

Always prefer using [Locator](Locator.md)s and web assertions over [ElementHandle](Elementhandle.md)s because latter are inherently racy.

Resolves given locator to all matching DOM elements. If there are no matching elements, returns an empty list.

**Usage**

```
locator.element_handles()
```

**Returns**

* List[[ElementHandle](Elementhandle.md)]

---

### type[​](#locator-type "Direct link to type") locator.type

Deprecated

In most cases, you should use [locator.fill()](Locator.md) instead. You only need to press keys one by one if there is special keyboard handling on the page - in this case use [locator.press_sequentially()](Locator.md).

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

To press a special key, like `Control` or `ArrowDown`, use [locator.press()](Locator.md).

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
