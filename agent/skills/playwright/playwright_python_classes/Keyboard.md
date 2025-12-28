# Keyboard

Source: https://playwright.dev/python/docs/api/class-keyboard

---

Keyboard provides an api for managing a virtual keyboard. The high level api is [keyboard.type()](Keyboard.md), which takes raw characters and generates proper `keydown`, `keypress`/`input`, and `keyup` events on your page.

For finer control, you can use [keyboard.down()](Keyboard.md), [keyboard.up()](Keyboard.md), and [keyboard.insert_text()](Keyboard.md) to manually fire events as if they were generated from a real keyboard.

An example of holding down `Shift` in order to select and delete some text:

* Sync* Async

```
page.keyboard.type("Hello World!")  
page.keyboard.press("ArrowLeft")  
page.keyboard.down("Shift")  
for i in range(6):  
    page.keyboard.press("ArrowLeft")  
page.keyboard.up("Shift")  
page.keyboard.press("Backspace")  
# result text will end up saying "Hello!"
```

```
await page.keyboard.type("Hello World!")  
await page.keyboard.press("ArrowLeft")  
await page.keyboard.down("Shift")  
for i in range(6):  
    await page.keyboard.press("ArrowLeft")  
await page.keyboard.up("Shift")  
await page.keyboard.press("Backspace")  
# result text will end up saying "Hello!"
```

An example of pressing uppercase `A`

* Sync* Async

```
page.keyboard.press("Shift+KeyA")  
# or  
page.keyboard.press("Shift+A")
```

```
await page.keyboard.press("Shift+KeyA")  
# or  
await page.keyboard.press("Shift+A")
```

An example to trigger select-all with the keyboard

* Sync* Async

```
page.keyboard.press("ControlOrMeta+A")
```

```
await page.keyboard.press("ControlOrMeta+A")
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### down[​](#keyboard-down "Direct link to down")

Added before v1.9
keyboard.down

Dispatches a `keydown` event.

[key](Keyboard.md) can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character to generate the text for. A superset of the [key](Keyboard.md) values can be found [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the [key](Keyboard.md) in the upper case.

If [key](Keyboard.md) is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective texts.

If [key](Keyboard.md) is a modifier key, `Shift`, `Meta`, `Control`, or `Alt`, subsequent key presses will be sent with that modifier active. To release the modifier key, use [keyboard.up()](Keyboard.md).

After the key is pressed once, subsequent calls to [keyboard.down()](Keyboard.md) will have [repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat) set to true. To release the key, use [keyboard.up()](Keyboard.md).

note

Modifier keys DO influence `keyboard.down`. Holding down `Shift` will type the text in upper case.

**Usage**

```
keyboard.down(key)
```

**Arguments**

* `key` str

  Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.

**Returns**

* NoneType

---

### insert_text[​](#keyboard-insert-text "Direct link to insert_text")

Added before v1.9
keyboard.insert_text

Dispatches only `input` event, does not emit the `keydown`, `keyup` or `keypress` events.

**Usage**

* Sync* Async

```
page.keyboard.insert_text("嗨")
```

```
await page.keyboard.insert_text("嗨")
```

note

Modifier keys DO NOT effect `keyboard.insertText`. Holding down `Shift` will not type the text in upper case.

**Arguments**

* `text` str

  Sets input to the specified text value.

**Returns**

* NoneType

---

### press[​](#keyboard-press "Direct link to press")

Added before v1.9
keyboard.press

tip

In most cases, you should use [locator.press()](Locator.md) instead.

[key](Keyboard.md) can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character to generate the text for. A superset of the [key](Keyboard.md) values can be found [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the [key](Keyboard.md) in the upper case.

If [key](Keyboard.md) is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

**Usage**

* Sync* Async

```
page = browser.new_page()  
page.goto("https://keycode.info")  
page.keyboard.press("a")  
page.screenshot(path="a.png")  
page.keyboard.press("ArrowLeft")  
page.screenshot(path="arrow_left.png")  
page.keyboard.press("Shift+O")  
page.screenshot(path="o.png")  
browser.close()
```

```
page = await browser.new_page()  
await page.goto("https://keycode.info")  
await page.keyboard.press("a")  
await page.screenshot(path="a.png")  
await page.keyboard.press("ArrowLeft")  
await page.screenshot(path="arrow_left.png")  
await page.keyboard.press("Shift+O")  
await page.screenshot(path="o.png")  
await browser.close()
```

Shortcut for [keyboard.down()](Keyboard.md) and [keyboard.up()](Keyboard.md).

**Arguments**

* `key` str

  Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.
* `delay` float *(optional)*

  Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.

**Returns**

* NoneType

---

### type[​](#keyboard-type "Direct link to type")

Added before v1.9
keyboard.type

caution

In most cases, you should use [locator.fill()](Locator.md) instead. You only need to press keys one by one if there is special keyboard handling on the page - in this case use [locator.press_sequentially()](Locator.md).

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

To press a special key, like `Control` or `ArrowDown`, use [keyboard.press()](Keyboard.md).

**Usage**

* Sync* Async

```
page.keyboard.type("Hello") # types instantly  
page.keyboard.type("World", delay=100) # types slower, like a user
```

```
await page.keyboard.type("Hello") # types instantly  
await page.keyboard.type("World", delay=100) # types slower, like a user
```

note

Modifier keys DO NOT effect `keyboard.type`. Holding down `Shift` will not type the text in upper case.

note

For characters that are not on a US keyboard, only an `input` event will be sent.

**Arguments**

* `text` str

  A text to type into a focused element.
* `delay` float *(optional)*

  Time to wait between key presses in milliseconds. Defaults to 0.

**Returns**

* NoneType

---

### up[​](#keyboard-up "Direct link to up")

Added before v1.9
keyboard.up

Dispatches a `keyup` event.

**Usage**

```
keyboard.up(key)
```

**Arguments**

* `key` str

  Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.

**Returns**

* NoneType
