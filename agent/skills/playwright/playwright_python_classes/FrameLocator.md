# FrameLocator

Source: https://playwright.dev/python/docs/api/class-framelocator

---

FrameLocator represents a view to the `iframe` on the page. It captures the logic sufficient to retrieve the `iframe` and locate elements in that iframe. FrameLocator can be created with either [locator.content_frame](Locator.md), [page.frame_locator()](Page.md) or [locator.frame_locator()](Locator.md) method.

* Sync* Async

```
locator = page.locator("my-frame").content_frame.get_by_text("Submit")  
locator.click()
```

```
locator = page.locator("#my-frame").content_frame.get_by_text("Submit")  
await locator.click()
```

**Strictness**

Frame locators are strict. This means that all operations on frame locators will throw if more than one element matches a given selector.

* Sync* Async

```
# Throws if there are several frames in DOM:  
page.locator('.result-frame').content_frame.get_by_role('button').click()  
  
# Works because we explicitly tell locator to pick the first frame:  
page.locator('.result-frame').first.content_frame.get_by_role('button').click()
```

```
# Throws if there are several frames in DOM:  
await page.locator('.result-frame').content_frame.get_by_role('button').click()  
  
# Works because we explicitly tell locator to pick the first frame:  
await page.locator('.result-frame').first.content_frame.get_by_role('button').click()
```

**Converting Locator to FrameLocator**

If you have a [Locator](Locator.md) object pointing to an `iframe` it can be converted to [FrameLocator](Framelocator.md) using [locator.content_frame](Locator.md).

**Converting FrameLocator to Locator**

If you have a [FrameLocator](Framelocator.md) object it can be converted to [Locator](Locator.md) pointing to the same `iframe` using [frame_locator.owner](Framelocator.md).

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### frame_locator[​](#frame-locator-frame-locator "Direct link to frame_locator") frameLocator.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements in that iframe.

**Usage**

```
frame_locator.frame_locator(selector)
```

**Arguments**

* `selector` str

  A selector to use when resolving DOM element.

**Returns**

* [FrameLocator](Framelocator.md)

---

### get_by_alt_text[​](#frame-locator-get-by-alt-text "Direct link to get_by_alt_text") frameLocator.get_by_alt_text

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

### get_by_label[​](#frame-locator-get-by-label "Direct link to get_by_label") frameLocator.get_by_label

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

### get_by_placeholder[​](#frame-locator-get-by-placeholder "Direct link to get_by_placeholder") frameLocator.get_by_placeholder

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

### get_by_role[​](#frame-locator-get-by-role "Direct link to get_by_role") frameLocator.get_by_role

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

  Whether [name](Framelocator.md) is matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when [name](Framelocator.md) is a regular expression. Note that exact match still trims whitespace.
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

  Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use [exact](Framelocator.md) to control this behavior.

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

### get_by_test_id[​](#frame-locator-get-by-test-id "Direct link to get_by_test_id") frameLocator.get_by_test_id

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

### get_by_text[​](#frame-locator-get-by-text "Direct link to get_by_text") frameLocator.get_by_text

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

### get_by_title[​](#frame-locator-get-by-title "Direct link to get_by_title") frameLocator.get_by_title

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

### locator[​](#frame-locator-locator "Direct link to locator") frameLocator.locator

The method finds an element matching the specified selector in the locator's subtree. It also accepts filter options, similar to [locator.filter()](Locator.md) method.

[Learn more about locators](/python/docs/locators).

**Usage**

```
frame_locator.locator(selector_or_locator)  
frame_locator.locator(selector_or_locator, **kwargs)
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

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### owner[​](#frame-locator-owner "Direct link to owner") frameLocator.owner

Returns a [Locator](Locator.md) object pointing to the same `iframe` as this frame locator.

Useful when you have a [FrameLocator](Framelocator.md) object obtained somewhere, and later on would like to interact with the `iframe` element.

For a reverse operation, use [locator.content_frame](Locator.md).

**Usage**

* Sync* Async

```
frame_locator = page.locator("iframe[name=\"embedded\"]").content_frame  
# ...  
locator = frame_locator.owner  
expect(locator).to_be_visible()
```

```
frame_locator = page.locator("iframe[name=\"embedded\"]").content_frame  
# ...  
locator = frame_locator.owner  
await expect(locator).to_be_visible()
```

**Returns**

* [Locator](Locator.md)

---

Deprecated[​](#deprecated "Direct link to Deprecated")
------------------------------------------------------

### first[​](#frame-locator-first "Direct link to first") frameLocator.first

Deprecated

Use [locator.first](Locator.md) followed by [locator.content_frame](Locator.md) instead.

Returns locator to the first matching frame.

**Usage**

```
frame_locator.first
```

**Returns**

* [FrameLocator](Framelocator.md)

---

### last[​](#frame-locator-last "Direct link to last") frameLocator.last

Deprecated

Use [locator.last](Locator.md) followed by [locator.content_frame](Locator.md) instead.

Returns locator to the last matching frame.

**Usage**

```
frame_locator.last
```

**Returns**

* [FrameLocator](Framelocator.md)

---

### nth[​](#frame-locator-nth "Direct link to nth") frameLocator.nth

Deprecated

Use [locator.nth()](Locator.md) followed by [locator.content_frame](Locator.md) instead.

Returns locator to the n-th matching frame. It's zero based, `nth(0)` selects the first frame.

**Usage**

```
frame_locator.nth(index)
```

**Arguments**

* `index` int

**Returns**

* [FrameLocator](Framelocator.md)
