# LocatorAssertions

Source: https://playwright.dev/python/docs/api/class-locatorassertions

---

The [LocatorAssertions](Locatorassertions.md) class provides assertion methods that can be used to make assertions about the [Locator](Locator.md) state in the tests.

* Sync* Async

```
from playwright.sync_api import Page, expect  
  
def test_status_becomes_submitted(page: Page) -> None:  
    # ..  
    page.get_by_role("button").click()  
    expect(page.locator(".status")).to_have_text("Submitted")
```

```
from playwright.async_api import Page, expect  
  
async def test_status_becomes_submitted(page: Page) -> None:  
    # ..  
    await page.get_by_role("button").click()  
    await expect(page.locator(".status")).to_have_text("Submitted")
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### not_to_be_attached[​](#locator-assertions-not-to-be-attached "Direct link to not_to_be_attached") locatorAssertions.not_to_be_attached

The opposite of [expect(locator).to_be_attached()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_attached()  
expect(locator).not_to_be_attached(**kwargs)
```

**Arguments**

* `attached` bool *(optional)*
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_checked[​](#locator-assertions-not-to-be-checked "Direct link to not_to_be_checked") locatorAssertions.not_to_be_checked

The opposite of [expect(locator).to_be_checked()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_checked()  
expect(locator).not_to_be_checked(**kwargs)
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_disabled[​](#locator-assertions-not-to-be-disabled "Direct link to not_to_be_disabled") locatorAssertions.not_to_be_disabled

The opposite of [expect(locator).to_be_disabled()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_disabled()  
expect(locator).not_to_be_disabled(**kwargs)
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_editable[​](#locator-assertions-not-to-be-editable "Direct link to not_to_be_editable") locatorAssertions.not_to_be_editable

The opposite of [expect(locator).to_be_editable()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_editable()  
expect(locator).not_to_be_editable(**kwargs)
```

**Arguments**

* `editable` bool *(optional)* 
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_empty[​](#locator-assertions-not-to-be-empty "Direct link to not_to_be_empty") locatorAssertions.not_to_be_empty

The opposite of [expect(locator).to_be_empty()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_empty()  
expect(locator).not_to_be_empty(**kwargs)
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_enabled[​](#locator-assertions-not-to-be-enabled "Direct link to not_to_be_enabled") locatorAssertions.not_to_be_enabled

The opposite of [expect(locator).to_be_enabled()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_enabled()  
expect(locator).not_to_be_enabled(**kwargs)
```

**Arguments**

* `enabled` bool *(optional)* 
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_focused[​](#locator-assertions-not-to-be-focused "Direct link to not_to_be_focused") locatorAssertions.not_to_be_focused

The opposite of [expect(locator).to_be_focused()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_focused()  
expect(locator).not_to_be_focused(**kwargs)
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_hidden[​](#locator-assertions-not-to-be-hidden "Direct link to not_to_be_hidden") locatorAssertions.not_to_be_hidden

The opposite of [expect(locator).to_be_hidden()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_hidden()  
expect(locator).not_to_be_hidden(**kwargs)
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_in_viewport[​](#locator-assertions-not-to-be-in-viewport "Direct link to not_to_be_in_viewport") locatorAssertions.not_to_be_in_viewport

The opposite of [expect(locator).to_be_in_viewport()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_in_viewport()  
expect(locator).not_to_be_in_viewport(**kwargs)
```

**Arguments**

* `ratio` float *(optional)*
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_be_visible[​](#locator-assertions-not-to-be-visible "Direct link to not_to_be_visible") locatorAssertions.not_to_be_visible

The opposite of [expect(locator).to_be_visible()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_be_visible()  
expect(locator).not_to_be_visible(**kwargs)
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.
* `visible` bool *(optional)* 

**Returns**

* NoneType

---

### not_to_contain_class[​](#locator-assertions-not-to-contain-class "Direct link to not_to_contain_class") locatorAssertions.not_to_contain_class

The opposite of [expect(locator).to_contain_class()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_contain_class(expected)  
expect(locator).not_to_contain_class(expected, **kwargs)
```

**Arguments**

* `expected` str | List[str]

  Expected class or RegExp or a list of those.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_contain_text[​](#locator-assertions-not-to-contain-text "Direct link to not_to_contain_text") locatorAssertions.not_to_contain_text

The opposite of [expect(locator).to_contain_text()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_contain_text(expected)  
expect(locator).not_to_contain_text(expected, **kwargs)
```

**Arguments**

* `expected` str | Pattern | List[str] | List[Pattern] | List[str | Pattern] 

  Expected substring or RegExp or a list of those.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.
* `use_inner_text` bool *(optional)* 

  Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text.

**Returns**

* NoneType

---

### not_to_have_accessible_description[​](#locator-assertions-not-to-have-accessible-description "Direct link to not_to_have_accessible_description") locatorAssertions.not_to_have_accessible_description

The opposite of [expect(locator).to_have_accessible_description()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_accessible_description(name)  
expect(locator).not_to_have_accessible_description(name, **kwargs)
```

**Arguments**

* `description` str | Pattern

  Expected accessible description.
* `ignore_case` bool *(optional)*

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_accessible_error_message[​](#locator-assertions-not-to-have-accessible-error-message "Direct link to not_to_have_accessible_error_message") locatorAssertions.not_to_have_accessible_error_message

The opposite of [expect(locator).to_have_accessible_error_message()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_accessible_error_message(error_message)  
expect(locator).not_to_have_accessible_error_message(error_message, **kwargs)
```

**Arguments**

* `error_message` str | Pattern

  Expected accessible error message.
* `ignore_case` bool *(optional)*

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_accessible_name[​](#locator-assertions-not-to-have-accessible-name "Direct link to not_to_have_accessible_name") locatorAssertions.not_to_have_accessible_name

The opposite of [expect(locator).to_have_accessible_name()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_accessible_name(name)  
expect(locator).not_to_have_accessible_name(name, **kwargs)
```

**Arguments**

* `name` str | Pattern

  Expected accessible name.
* `ignore_case` bool *(optional)*

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_attribute[​](#locator-assertions-not-to-have-attribute "Direct link to not_to_have_attribute") locatorAssertions.not_to_have_attribute

The opposite of [expect(locator).to_have_attribute()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_attribute(name, value)  
expect(locator).not_to_have_attribute(name, value, **kwargs)
```

**Arguments**

* `name` str 

  Attribute name.
* `value` str | Pattern 

  Expected attribute value.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_class[​](#locator-assertions-not-to-have-class "Direct link to not_to_have_class") locatorAssertions.not_to_have_class

The opposite of [expect(locator).to_have_class()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_class(expected)  
expect(locator).not_to_have_class(expected, **kwargs)
```

**Arguments**

* `expected` str | Pattern | List[str] | List[Pattern] | List[str | Pattern] 

  Expected class or RegExp or a list of those.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_count[​](#locator-assertions-not-to-have-count "Direct link to not_to_have_count") locatorAssertions.not_to_have_count

The opposite of [expect(locator).to_have_count()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_count(count)  
expect(locator).not_to_have_count(count, **kwargs)
```

**Arguments**

* `count` int 

  Expected count.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_css[​](#locator-assertions-not-to-have-css "Direct link to not_to_have_css") locatorAssertions.not_to_have_css

The opposite of [expect(locator).to_have_css()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_css(name, value)  
expect(locator).not_to_have_css(name, value, **kwargs)
```

**Arguments**

* `name` str 

  CSS property name.
* `value` str | Pattern 

  CSS property value.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_id[​](#locator-assertions-not-to-have-id "Direct link to not_to_have_id") locatorAssertions.not_to_have_id

The opposite of [expect(locator).to_have_id()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_id(id)  
expect(locator).not_to_have_id(id, **kwargs)
```

**Arguments**

* `id` str | Pattern 

  Element id.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_js_property[​](#locator-assertions-not-to-have-js-property "Direct link to not_to_have_js_property") locatorAssertions.not_to_have_js_property

The opposite of [expect(locator).to_have_js_property()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_js_property(name, value)  
expect(locator).not_to_have_js_property(name, value, **kwargs)
```

**Arguments**

* `name` str 

  Property name.
* `value` Any 

  Property value.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_role[​](#locator-assertions-not-to-have-role "Direct link to not_to_have_role") locatorAssertions.not_to_have_role

The opposite of [expect(locator).to_have_role()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_role(role)  
expect(locator).not_to_have_role(role, **kwargs)
```

**Arguments**

* `role` "alert" | "alertdialog" | "application" | "article" | "banner" | "blockquote" | "button" | "caption" | "cell" | "checkbox" | "code" | "columnheader" | "combobox" | "complementary" | "contentinfo" | "definition" | "deletion" | "dialog" | "directory" | "document" | "emphasis" | "feed" | "figure" | "form" | "generic" | "grid" | "gridcell" | "group" | "heading" | "img" | "insertion" | "link" | "list" | "listbox" | "listitem" | "log" | "main" | "marquee" | "math" | "meter" | "menu" | "menubar" | "menuitem" | "menuitemcheckbox" | "menuitemradio" | "navigation" | "none" | "note" | "option" | "paragraph" | "presentation" | "progressbar" | "radio" | "radiogroup" | "region" | "row" | "rowgroup" | "rowheader" | "scrollbar" | "search" | "searchbox" | "separator" | "slider" | "spinbutton" | "status" | "strong" | "subscript" | "superscript" | "switch" | "tab" | "table" | "tablist" | "tabpanel" | "term" | "textbox" | "time" | "timer" | "toolbar" | "tooltip" | "tree" | "treegrid" | "treeitem"

  Required aria role.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_text[​](#locator-assertions-not-to-have-text "Direct link to not_to_have_text") locatorAssertions.not_to_have_text

The opposite of [expect(locator).to_have_text()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_text(expected)  
expect(locator).not_to_have_text(expected, **kwargs)
```

**Arguments**

* `expected` str | Pattern | List[str] | List[Pattern] | List[str | Pattern] 

  Expected string or RegExp or a list of those.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.
* `use_inner_text` bool *(optional)* 

  Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text.

**Returns**

* NoneType

---

### not_to_have_value[​](#locator-assertions-not-to-have-value "Direct link to not_to_have_value") locatorAssertions.not_to_have_value

The opposite of [expect(locator).to_have_value()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_value(value)  
expect(locator).not_to_have_value(value, **kwargs)
```

**Arguments**

* `value` str | Pattern 

  Expected value.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_values[​](#locator-assertions-not-to-have-values "Direct link to not_to_have_values") locatorAssertions.not_to_have_values

The opposite of [expect(locator).to_have_values()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_have_values(values)  
expect(locator).not_to_have_values(values, **kwargs)
```

**Arguments**

* `values` List[str] | List[Pattern] | List[str | Pattern]

  Expected options currently selected.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_match_aria_snapshot[​](#locator-assertions-not-to-match-aria-snapshot "Direct link to not_to_match_aria_snapshot") locatorAssertions.not_to_match_aria_snapshot

The opposite of [expect(locator).to_match_aria_snapshot()](Locatorassertions.md).

**Usage**

```
expect(locator).not_to_match_aria_snapshot(expected)  
expect(locator).not_to_match_aria_snapshot(expected, **kwargs)
```

**Arguments**

* `expected` str
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_attached[​](#locator-assertions-to-be-attached "Direct link to to_be_attached") locatorAssertions.to_be_attached

Ensures that [Locator](Locator.md) points to an element that is [connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

**Usage**

* Sync* Async

```
expect(page.get_by_text("Hidden text")).to_be_attached()
```

```
await expect(page.get_by_text("Hidden text")).to_be_attached()
```

**Arguments**

* `attached` bool *(optional)*
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_checked[​](#locator-assertions-to-be-checked "Direct link to to_be_checked") locatorAssertions.to_be_checked

Ensures the [Locator](Locator.md) points to a checked input.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.get_by_label("Subscribe to newsletter")  
expect(locator).to_be_checked()
```

```
from playwright.async_api import expect  
  
locator = page.get_by_label("Subscribe to newsletter")  
await expect(locator).to_be_checked()
```

**Arguments**

* `checked` bool *(optional)* 

  Provides state to assert for. Asserts for input to be checked by default. This option can't be used when [indeterminate](Locatorassertions.md) is set to true.
* `indeterminate` bool *(optional)* 

  Asserts that the element is in the indeterminate (mixed) state. Only supported for checkboxes and radio buttons. This option can't be true when [checked](Locatorassertions.md) is provided.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_disabled[​](#locator-assertions-to-be-disabled "Direct link to to_be_disabled") locatorAssertions.to_be_disabled

Ensures the [Locator](Locator.md) points to a disabled element. Element is disabled if it has "disabled" attribute or is disabled via ['aria-disabled'](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-disabled). Note that only native control elements such as HTML `button`, `input`, `select`, `textarea`, `option`, `optgroup` can be disabled by setting "disabled" attribute. "disabled" attribute on other elements is ignored by the browser.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator("button.submit")  
expect(locator).to_be_disabled()
```

```
from playwright.async_api import expect  
  
locator = page.locator("button.submit")  
await expect(locator).to_be_disabled()
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_editable[​](#locator-assertions-to-be-editable "Direct link to to_be_editable") locatorAssertions.to_be_editable

Ensures the [Locator](Locator.md) points to an editable element.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.get_by_role("textbox")  
expect(locator).to_be_editable()
```

```
from playwright.async_api import expect  
  
locator = page.get_by_role("textbox")  
await expect(locator).to_be_editable()
```

**Arguments**

* `editable` bool *(optional)* 
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_empty[​](#locator-assertions-to-be-empty "Direct link to to_be_empty") locatorAssertions.to_be_empty

Ensures the [Locator](Locator.md) points to an empty editable element or to a DOM node that has no text.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator("div.warning")  
expect(locator).to_be_empty()
```

```
from playwright.async_api import expect  
  
locator = page.locator("div.warning")  
await expect(locator).to_be_empty()
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_enabled[​](#locator-assertions-to-be-enabled "Direct link to to_be_enabled") locatorAssertions.to_be_enabled

Ensures the [Locator](Locator.md) points to an enabled element.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator("button.submit")  
expect(locator).to_be_enabled()
```

```
from playwright.async_api import expect  
  
locator = page.locator("button.submit")  
await expect(locator).to_be_enabled()
```

**Arguments**

* `enabled` bool *(optional)* 
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_focused[​](#locator-assertions-to-be-focused "Direct link to to_be_focused") locatorAssertions.to_be_focused

Ensures the [Locator](Locator.md) points to a focused DOM node.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.get_by_role("textbox")  
expect(locator).to_be_focused()
```

```
from playwright.async_api import expect  
  
locator = page.get_by_role("textbox")  
await expect(locator).to_be_focused()
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_hidden[​](#locator-assertions-to-be-hidden "Direct link to to_be_hidden") locatorAssertions.to_be_hidden

Ensures that [Locator](Locator.md) either does not resolve to any DOM node, or resolves to a [non-visible](/python/docs/actionability#visible) one.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator('.my-element')  
expect(locator).to_be_hidden()
```

```
from playwright.async_api import expect  
  
locator = page.locator('.my-element')  
await expect(locator).to_be_hidden()
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_in_viewport[​](#locator-assertions-to-be-in-viewport "Direct link to to_be_in_viewport") locatorAssertions.to_be_in_viewport

Ensures the [Locator](Locator.md) points to an element that intersects viewport, according to the [intersection observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.get_by_role("button")  
# Make sure at least some part of element intersects viewport.  
expect(locator).to_be_in_viewport()  
# Make sure element is fully outside of viewport.  
expect(locator).not_to_be_in_viewport()  
# Make sure that at least half of the element intersects viewport.  
expect(locator).to_be_in_viewport(ratio=0.5)
```

```
from playwright.async_api import expect  
  
locator = page.get_by_role("button")  
# Make sure at least some part of element intersects viewport.  
await expect(locator).to_be_in_viewport()  
# Make sure element is fully outside of viewport.  
await expect(locator).not_to_be_in_viewport()  
# Make sure that at least half of the element intersects viewport.  
await expect(locator).to_be_in_viewport(ratio=0.5)
```

**Arguments**

* `ratio` float *(optional)*

  The minimal ratio of the element to intersect viewport. If equals to `0`, then element should intersect viewport at any positive ratio. Defaults to `0`.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_be_visible[​](#locator-assertions-to-be-visible "Direct link to to_be_visible") locatorAssertions.to_be_visible

Ensures that [Locator](Locator.md) points to an attached and [visible](/python/docs/actionability#visible) DOM node.

To check that at least one element from the list is visible, use [locator.first](Locator.md).

**Usage**

* Sync* Async

```
# A specific element is visible.  
expect(page.get_by_text("Welcome")).to_be_visible()  
  
# At least one item in the list is visible.  
expect(page.get_by_test_id("todo-item").first).to_be_visible()  
  
# At least one of the two elements is visible, possibly both.  
expect(  
    page.get_by_role("button", name="Sign in")  
    .or_(page.get_by_role("button", name="Sign up"))  
    .first  
).to_be_visible()
```

```
# A specific element is visible.  
await expect(page.get_by_text("Welcome")).to_be_visible()  
  
# At least one item in the list is visible.  
await expect(page.get_by_test_id("todo-item").first).to_be_visible()  
  
# At least one of the two elements is visible, possibly both.  
await expect(  
    page.get_by_role("button", name="Sign in")  
    .or_(page.get_by_role("button", name="Sign up"))  
    .first  
).to_be_visible()
```

**Arguments**

* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.
* `visible` bool *(optional)* 

**Returns**

* NoneType

---

### to_contain_class[​](#locator-assertions-to-contain-class "Direct link to to_contain_class") locatorAssertions.to_contain_class

Ensures the [Locator](Locator.md) points to an element with given CSS classes. All classes from the asserted value, separated by spaces, must be present in the [Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) in any order.

**Usage**

```
<div class='middle selected row' id='component'></div>
```

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator("#component")  
expect(locator).to_contain_class("middle selected row")  
expect(locator).to_contain_class("selected")  
expect(locator).to_contain_class("row middle")
```

```
from playwright.async_api import expect  
  
locator = page.locator("#component")  
await expect(locator).to_contain_class("middle selected row")  
await expect(locator).to_contain_class("selected")  
await expect(locator).to_contain_class("row middle")
```

When an array is passed, the method asserts that the list of elements located matches the corresponding list of expected class lists. Each element's class attribute is matched against the corresponding class in the array:

```
<div class='list'>  
  <div class='component inactive'></div>  
  <div class='component active'></div>  
  <div class='component inactive'></div>  
</div>
```

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator(".list > .component")  
await expect(locator).to_contain_class(["inactive", "active", "inactive"])
```

```
from playwright.async_api import expect  
  
locator = page.locator(".list > .component")  
await expect(locator).to_contain_class(["inactive", "active", "inactive"])
```

**Arguments**

* `expected` str | List[str]

  A string containing expected class names, separated by spaces, or a list of such strings to assert multiple elements.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_contain_text[​](#locator-assertions-to-contain-text "Direct link to to_contain_text") locatorAssertions.to_contain_text

Ensures the [Locator](Locator.md) points to an element that contains the given text. All nested elements will be considered when computing the text content of the element. You can use regular expressions for the value as well.

**Usage**

* Sync* Async

```
import re  
from playwright.sync_api import expect  
  
locator = page.locator('.title')  
expect(locator).to_contain_text("substring")  
expect(locator).to_contain_text(re.compile(r"\d messages"))
```

```
import re  
from playwright.async_api import expect  
  
locator = page.locator('.title')  
await expect(locator).to_contain_text("substring")  
await expect(locator).to_contain_text(re.compile(r"\d messages"))
```

If you pass an array as an expected value, the expectations are:

1. Locator resolves to a list of elements.
2. Elements from a **subset** of this list contain text from the expected array, respectively.
3. The matching subset of elements has the same order as the expected array.
4. Each text value from the expected array is matched by some element from the list.

For example, consider the following list:

```
<ul>  
  <li>Item Text 1</li>  
  <li>Item Text 2</li>  
  <li>Item Text 3</li>  
</ul>
```

Let's see how we can use the assertion:

* Sync* Async

```
from playwright.sync_api import expect  
  
# ✓ Contains the right items in the right order  
expect(page.locator("ul > li")).to_contain_text(["Text 1", "Text 3", "Text 4"])  
  
# ✖ Wrong order  
expect(page.locator("ul > li")).to_contain_text(["Text 3", "Text 2"])  
  
# ✖ No item contains this text  
expect(page.locator("ul > li")).to_contain_text(["Some 33"])  
  
# ✖ Locator points to the outer list element, not to the list items  
expect(page.locator("ul")).to_contain_text(["Text 3"])
```

```
from playwright.async_api import expect  
  
# ✓ Contains the right items in the right order  
await expect(page.locator("ul > li")).to_contain_text(["Text 1", "Text 3", "Text 4"])  
  
# ✖ Wrong order  
await expect(page.locator("ul > li")).to_contain_text(["Text 3", "Text 2"])  
  
# ✖ No item contains this text  
await expect(page.locator("ul > li")).to_contain_text(["Some 33"])  
  
# ✖ Locator points to the outer list element, not to the list items  
await expect(page.locator("ul")).to_contain_text(["Text 3"])
```

**Arguments**

* `expected` str | Pattern | List[str] | List[Pattern] | List[str | Pattern] 

  Expected substring or RegExp or a list of those.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.
* `use_inner_text` bool *(optional)* 

  Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text.

**Returns**

* NoneType

**Details**

When `expected` parameter is a string, Playwright will normalize whitespaces and line breaks both in the actual text and in the expected string before matching. When regular expression is used, the actual text is matched as is.

---

### to_have_accessible_description[​](#locator-assertions-to-have-accessible-description "Direct link to to_have_accessible_description") locatorAssertions.to_have_accessible_description

Ensures the [Locator](Locator.md) points to an element with a given [accessible description](https://w3c.github.io/accname/#dfn-accessible-description).

**Usage**

* Sync* Async

```
locator = page.get_by_test_id("save-button")  
expect(locator).to_have_accessible_description("Save results to disk")
```

```
locator = page.get_by_test_id("save-button")  
await expect(locator).to_have_accessible_description("Save results to disk")
```

**Arguments**

* `description` str | Pattern

  Expected accessible description.
* `ignore_case` bool *(optional)*

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_accessible_error_message[​](#locator-assertions-to-have-accessible-error-message "Direct link to to_have_accessible_error_message") locatorAssertions.to_have_accessible_error_message

Ensures the [Locator](Locator.md) points to an element with a given [aria errormessage](https://w3c.github.io/aria/#aria-errormessage).

**Usage**

* Sync* Async

```
locator = page.get_by_test_id("username-input")  
expect(locator).to_have_accessible_error_message("Username is required.")
```

```
locator = page.get_by_test_id("username-input")  
await expect(locator).to_have_accessible_error_message("Username is required.")
```

**Arguments**

* `error_message` str | Pattern

  Expected accessible error message.
* `ignore_case` bool *(optional)*

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_accessible_name[​](#locator-assertions-to-have-accessible-name "Direct link to to_have_accessible_name") locatorAssertions.to_have_accessible_name

Ensures the [Locator](Locator.md) points to an element with a given [accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

* Sync* Async

```
locator = page.get_by_test_id("save-button")  
expect(locator).to_have_accessible_name("Save to disk")
```

```
locator = page.get_by_test_id("save-button")  
await expect(locator).to_have_accessible_name("Save to disk")
```

**Arguments**

* `name` str | Pattern

  Expected accessible name.
* `ignore_case` bool *(optional)*

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_attribute[​](#locator-assertions-to-have-attribute "Direct link to to_have_attribute") locatorAssertions.to_have_attribute

Ensures the [Locator](Locator.md) points to an element with given attribute.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator("input")  
expect(locator).to_have_attribute("type", "text")
```

```
from playwright.async_api import expect  
  
locator = page.locator("input")  
await expect(locator).to_have_attribute("type", "text")
```

**Arguments**

* `name` str 

  Attribute name.
* `value` str | Pattern 

  Expected attribute value.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_class[​](#locator-assertions-to-have-class "Direct link to to_have_class") locatorAssertions.to_have_class

Ensures the [Locator](Locator.md) points to an element with given CSS classes. When a string is provided, it must fully match the element's `class` attribute. To match individual classes use [expect(locator).to_contain_class()](Locatorassertions.md).

**Usage**

```
<div class='middle selected row' id='component'></div>
```

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator("#component")  
expect(locator).to_have_class("middle selected row")  
expect(locator).to_have_class(re.compile(r"(^|\\s)selected(\\s|$)"))
```

```
from playwright.async_api import expect  
  
locator = page.locator("#component")  
await expect(locator).to_have_class("middle selected row")  
await expect(locator).to_have_class(re.compile(r"(^|\\s)selected(\\s|$)"))
```

When an array is passed, the method asserts that the list of elements located matches the corresponding list of expected class values. Each element's class attribute is matched against the corresponding string or regular expression in the array:

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator(".list > .component")  
expect(locator).to_have_class(["component", "component selected", "component"])
```

```
from playwright.async_api import expect  
  
locator = page.locator(".list > .component")  
await expect(locator).to_have_class(["component", "component selected", "component"])
```

**Arguments**

* `expected` str | Pattern | List[str] | List[Pattern] | List[str | Pattern] 

  Expected class or RegExp or a list of those.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_count[​](#locator-assertions-to-have-count "Direct link to to_have_count") locatorAssertions.to_have_count

Ensures the [Locator](Locator.md) resolves to an exact number of DOM nodes.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator("list > .component")  
expect(locator).to_have_count(3)
```

```
from playwright.async_api import expect  
  
locator = page.locator("list > .component")  
await expect(locator).to_have_count(3)
```

**Arguments**

* `count` int 

  Expected count.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_css[​](#locator-assertions-to-have-css "Direct link to to_have_css") locatorAssertions.to_have_css

Ensures the [Locator](Locator.md) resolves to an element with the given computed CSS style.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.get_by_role("button")  
expect(locator).to_have_css("display", "flex")
```

```
from playwright.async_api import expect  
  
locator = page.get_by_role("button")  
await expect(locator).to_have_css("display", "flex")
```

**Arguments**

* `name` str 

  CSS property name.
* `value` str | Pattern 

  CSS property value.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_id[​](#locator-assertions-to-have-id "Direct link to to_have_id") locatorAssertions.to_have_id

Ensures the [Locator](Locator.md) points to an element with the given DOM Node ID.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.get_by_role("textbox")  
expect(locator).to_have_id("lastname")
```

```
from playwright.async_api import expect  
  
locator = page.get_by_role("textbox")  
await expect(locator).to_have_id("lastname")
```

**Arguments**

* `id` str | Pattern 

  Element id.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_js_property[​](#locator-assertions-to-have-js-property "Direct link to to_have_js_property") locatorAssertions.to_have_js_property

Ensures the [Locator](Locator.md) points to an element with given JavaScript property. Note that this property can be of a primitive type as well as a plain serializable JavaScript object.

**Usage**

* Sync* Async

```
from playwright.sync_api import expect  
  
locator = page.locator(".component")  
expect(locator).to_have_js_property("loaded", True)
```

```
from playwright.async_api import expect  
  
locator = page.locator(".component")  
await expect(locator).to_have_js_property("loaded", True)
```

**Arguments**

* `name` str 

  Property name.
* `value` Any 

  Property value.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_role[​](#locator-assertions-to-have-role "Direct link to to_have_role") locatorAssertions.to_have_role

Ensures the [Locator](Locator.md) points to an element with a given [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles).

Note that role is matched as a string, disregarding the ARIA role hierarchy. For example, asserting a superclass role `"checkbox"` on an element with a subclass role `"switch"` will fail.

**Usage**

* Sync* Async

```
locator = page.get_by_test_id("save-button")  
expect(locator).to_have_role("button")
```

```
locator = page.get_by_test_id("save-button")  
await expect(locator).to_have_role("button")
```

**Arguments**

* `role` "alert" | "alertdialog" | "application" | "article" | "banner" | "blockquote" | "button" | "caption" | "cell" | "checkbox" | "code" | "columnheader" | "combobox" | "complementary" | "contentinfo" | "definition" | "deletion" | "dialog" | "directory" | "document" | "emphasis" | "feed" | "figure" | "form" | "generic" | "grid" | "gridcell" | "group" | "heading" | "img" | "insertion" | "link" | "list" | "listbox" | "listitem" | "log" | "main" | "marquee" | "math" | "meter" | "menu" | "menubar" | "menuitem" | "menuitemcheckbox" | "menuitemradio" | "navigation" | "none" | "note" | "option" | "paragraph" | "presentation" | "progressbar" | "radio" | "radiogroup" | "region" | "row" | "rowgroup" | "rowheader" | "scrollbar" | "search" | "searchbox" | "separator" | "slider" | "spinbutton" | "status" | "strong" | "subscript" | "superscript" | "switch" | "tab" | "table" | "tablist" | "tabpanel" | "term" | "textbox" | "time" | "timer" | "toolbar" | "tooltip" | "tree" | "treegrid" | "treeitem"

  Required aria role.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_text[​](#locator-assertions-to-have-text "Direct link to to_have_text") locatorAssertions.to_have_text

Ensures the [Locator](Locator.md) points to an element with the given text. All nested elements will be considered when computing the text content of the element. You can use regular expressions for the value as well.

**Usage**

* Sync* Async

```
import re  
from playwright.sync_api import expect  
  
locator = page.locator(".title")  
expect(locator).to_have_text(re.compile(r"Welcome, Test User"))  
expect(locator).to_have_text(re.compile(r"Welcome, .*"))
```

```
import re  
from playwright.async_api import expect  
  
locator = page.locator(".title")  
await expect(locator).to_have_text(re.compile(r"Welcome, Test User"))  
await expect(locator).to_have_text(re.compile(r"Welcome, .*"))
```

If you pass an array as an expected value, the expectations are:

1. Locator resolves to a list of elements.
2. The number of elements equals the number of expected values in the array.
3. Elements from the list have text matching expected array values, one by one, in order.

For example, consider the following list:

```
<ul>  
  <li>Text 1</li>  
  <li>Text 2</li>  
  <li>Text 3</li>  
</ul>
```

Let's see how we can use the assertion:

* Sync* Async

```
from playwright.sync_api import expect  
  
# ✓ Has the right items in the right order  
expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text 3"])  
  
# ✖ Wrong order  
expect(page.locator("ul > li")).to_have_text(["Text 3", "Text 2", "Text 1"])  
  
# ✖ Last item does not match  
expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text"])  
  
# ✖ Locator points to the outer list element, not to the list items  
expect(page.locator("ul")).to_have_text(["Text 1", "Text 2", "Text 3"])
```

```
from playwright.async_api import expect  
  
# ✓ Has the right items in the right order  
await expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text 3"])  
  
# ✖ Wrong order  
await expect(page.locator("ul > li")).to_have_text(["Text 3", "Text 2", "Text 1"])  
  
# ✖ Last item does not match  
await expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text"])  
  
# ✖ Locator points to the outer list element, not to the list items  
await expect(page.locator("ul")).to_have_text(["Text 1", "Text 2", "Text 3"])
```

**Arguments**

* `expected` str | Pattern | List[str] | List[Pattern] | List[str | Pattern] 

  Expected string or RegExp or a list of those.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Locatorassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.
* `use_inner_text` bool *(optional)* 

  Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text.

**Returns**

* NoneType

**Details**

When `expected` parameter is a string, Playwright will normalize whitespaces and line breaks both in the actual text and in the expected string before matching. When regular expression is used, the actual text is matched as is.

---

### to_have_value[​](#locator-assertions-to-have-value "Direct link to to_have_value") locatorAssertions.to_have_value

Ensures the [Locator](Locator.md) points to an element with the given input value. You can use regular expressions for the value as well.

**Usage**

* Sync* Async

```
import re  
from playwright.sync_api import expect  
  
locator = page.locator("input[type=number]")  
expect(locator).to_have_value(re.compile(r"[0-9]"))
```

```
import re  
from playwright.async_api import expect  
  
locator = page.locator("input[type=number]")  
await expect(locator).to_have_value(re.compile(r"[0-9]"))
```

**Arguments**

* `value` str | Pattern 

  Expected value.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_values[​](#locator-assertions-to-have-values "Direct link to to_have_values") locatorAssertions.to_have_values

Ensures the [Locator](Locator.md) points to multi-select/combobox (i.e. a `select` with the `multiple` attribute) and the specified values are selected.

**Usage**

For example, given the following element:

```
<select id="favorite-colors" multiple>  
  <option value="R">Red</option>  
  <option value="G">Green</option>  
  <option value="B">Blue</option>  
</select>
```

* Sync* Async

```
import re  
from playwright.sync_api import expect  
  
locator = page.locator("id=favorite-colors")  
locator.select_option(["R", "G"])  
expect(locator).to_have_values([re.compile(r"R"), re.compile(r"G")])
```

```
import re  
from playwright.async_api import expect  
  
locator = page.locator("id=favorite-colors")  
await locator.select_option(["R", "G"])  
await expect(locator).to_have_values([re.compile(r"R"), re.compile(r"G")])
```

**Arguments**

* `values` List[str] | List[Pattern] | List[str | Pattern]

  Expected options currently selected.
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_match_aria_snapshot[​](#locator-assertions-to-match-aria-snapshot "Direct link to to_match_aria_snapshot") locatorAssertions.to_match_aria_snapshot

Asserts that the target element matches the given [accessibility snapshot](/python/docs/aria-snapshots).

**Usage**

* Sync* Async

```
page.goto("https://demo.playwright.dev/todomvc/")  
expect(page.locator('body')).to_match_aria_snapshot('''  
  - heading "todos"  
  - textbox "What needs to be done?"  
''')
```

```
await page.goto("https://demo.playwright.dev/todomvc/")  
await expect(page.locator('body')).to_match_aria_snapshot('''  
  - heading "todos"  
  - textbox "What needs to be done?"  
''')
```

**Arguments**

* `expected` str
* `timeout` float *(optional)*

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType
