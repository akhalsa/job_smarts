# Mouse

Source: https://playwright.dev/python/docs/api/class-mouse

---

The Mouse class operates in main-frame CSS pixels relative to the top-left corner of the viewport.

tip

If you want to debug where the mouse moved, you can use the [Trace viewer](/python/docs/trace-viewer-intro) or [Playwright Inspector](/python/docs/running-tests). A red dot showing the location of the mouse will be shown for every mouse action.

Every `page` object has its own Mouse, accessible with [page.mouse](Page.md).

* Sync* Async

```
# using ‘page.mouse’ to trace a 100x100 square.  
page.mouse.move(0, 0)  
page.mouse.down()  
page.mouse.move(0, 100)  
page.mouse.move(100, 100)  
page.mouse.move(100, 0)  
page.mouse.move(0, 0)  
page.mouse.up()
```

```
# using ‘page.mouse’ to trace a 100x100 square.  
await page.mouse.move(0, 0)  
await page.mouse.down()  
await page.mouse.move(0, 100)  
await page.mouse.move(100, 100)  
await page.mouse.move(100, 0)  
await page.mouse.move(0, 0)  
await page.mouse.up()
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### click[​](#mouse-click "Direct link to click")

Added before v1.9
mouse.click

Shortcut for [mouse.move()](Mouse.md), [mouse.down()](Mouse.md), [mouse.up()](Mouse.md).

**Usage**

```
mouse.click(x, y)  
mouse.click(x, y, **kwargs)
```

**Arguments**

* `x` float

  X coordinate relative to the main frame's viewport in CSS pixels.
* `y` float

  Y coordinate relative to the main frame's viewport in CSS pixels.
* `button` "left" | "right" | "middle" *(optional)*

  Defaults to `left`.
* `click_count` int *(optional)*

  defaults to 1. See [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail").
* `delay` float *(optional)*

  Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.

**Returns**

* NoneType

---

### dblclick[​](#mouse-dblclick "Direct link to dblclick")

Added before v1.9
mouse.dblclick

Shortcut for [mouse.move()](Mouse.md), [mouse.down()](Mouse.md), [mouse.up()](Mouse.md), [mouse.down()](Mouse.md) and [mouse.up()](Mouse.md).

**Usage**

```
mouse.dblclick(x, y)  
mouse.dblclick(x, y, **kwargs)
```

**Arguments**

* `x` float

  X coordinate relative to the main frame's viewport in CSS pixels.
* `y` float

  Y coordinate relative to the main frame's viewport in CSS pixels.
* `button` "left" | "right" | "middle" *(optional)*

  Defaults to `left`.
* `delay` float *(optional)*

  Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.

**Returns**

* NoneType

---

### down[​](#mouse-down "Direct link to down")

Added before v1.9
mouse.down

Dispatches a `mousedown` event.

**Usage**

```
mouse.down()  
mouse.down(**kwargs)
```

**Arguments**

* `button` "left" | "right" | "middle" *(optional)*

  Defaults to `left`.
* `click_count` int *(optional)*

  defaults to 1. See [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail").

**Returns**

* NoneType

---

### move[​](#mouse-move "Direct link to move")

Added before v1.9
mouse.move

Dispatches a `mousemove` event.

**Usage**

```
mouse.move(x, y)  
mouse.move(x, y, **kwargs)
```

**Arguments**

* `x` float

  X coordinate relative to the main frame's viewport in CSS pixels.
* `y` float

  Y coordinate relative to the main frame's viewport in CSS pixels.
* `steps` int *(optional)*

  Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location.

**Returns**

* NoneType

---

### up[​](#mouse-up "Direct link to up")

Added before v1.9
mouse.up

Dispatches a `mouseup` event.

**Usage**

```
mouse.up()  
mouse.up(**kwargs)
```

**Arguments**

* `button` "left" | "right" | "middle" *(optional)*

  Defaults to `left`.
* `click_count` int *(optional)*

  defaults to 1. See [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail").

**Returns**

* NoneType

---

### wheel[​](#mouse-wheel "Direct link to wheel") mouse.wheel

Dispatches a `wheel` event. This method is usually used to manually scroll the page. See [scrolling](/python/docs/input#scrolling) for alternative ways to scroll.

note

Wheel events may cause scrolling if they are not handled, and this method does not wait for the scrolling to finish before returning.

**Usage**

```
mouse.wheel(delta_x, delta_y)
```

**Arguments**

* `delta_x` float

  Pixels to scroll horizontally.
* `delta_y` float

  Pixels to scroll vertically.

**Returns**

* NoneType
