# Touchscreen

Source: https://playwright.dev/python/docs/api/class-touchscreen

---

The Touchscreen class operates in main-frame CSS pixels relative to the top-left corner of the viewport. Methods on the touchscreen can only be used in browser contexts that have been initialized with `hasTouch` set to true.

This class is limited to emulating tap gestures. For examples of other gestures simulated by manually dispatching touch events, see the [emulating legacy touch events](/python/docs/touch-events) page.

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### tap[​](#touchscreen-tap "Direct link to tap")

Added before v1.9
touchscreen.tap

Dispatches a `touchstart` and `touchend` event with a single touch at the position ([x](Touchscreen.md),[y](Touchscreen.md)).

note

[page.tap()](Page.md) the method will throw if [has_touch](Browser.md) option of the browser context is false.

**Usage**

```
touchscreen.tap(x, y)
```

**Arguments**

* `x` float

  X coordinate relative to the main frame's viewport in CSS pixels.
* `y` float

  Y coordinate relative to the main frame's viewport in CSS pixels.

**Returns**

* NoneType
