# PageAssertions

Source: https://playwright.dev/python/docs/api/class-pageassertions

---

The [PageAssertions](Pageassertions.md) class provides assertion methods that can be used to make assertions about the [Page](Page.md) state in the tests.

* Sync* Async

```
import re  
from playwright.sync_api import Page, expect  
  
def test_navigates_to_login_page(page: Page) -> None:  
    # ..  
    page.get_by_text("Sign in").click()  
    expect(page).to_have_url(re.compile(r".*/login"))
```

```
import re  
from playwright.async_api import Page, expect  
  
async def test_navigates_to_login_page(page: Page) -> None:  
    # ..  
    await page.get_by_text("Sign in").click()  
    await expect(page).to_have_url(re.compile(r".*/login"))
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### not_to_have_title[​](#page-assertions-not-to-have-title "Direct link to not_to_have_title") pageAssertions.not_to_have_title

The opposite of [expect(page).to_have_title()](Pageassertions.md).

**Usage**

```
expect(page).not_to_have_title(title_or_reg_exp)  
expect(page).not_to_have_title(title_or_reg_exp, **kwargs)
```

**Arguments**

* `title_or_reg_exp` str | Pattern 

  Expected title or RegExp.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### not_to_have_url[​](#page-assertions-not-to-have-url "Direct link to not_to_have_url") pageAssertions.not_to_have_url

The opposite of [expect(page).to_have_url()](Pageassertions.md).

**Usage**

```
expect(page).not_to_have_url(url_or_reg_exp)  
expect(page).not_to_have_url(url_or_reg_exp, **kwargs)
```

**Arguments**

* `url_or_reg_exp` str | Pattern 

  Expected URL string or RegExp.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Pageassertions.md) option takes precedence over the corresponding regular expression flag if specified.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_title[​](#page-assertions-to-have-title "Direct link to to_have_title") pageAssertions.to_have_title

Ensures the page has the given title.

**Usage**

* Sync* Async

```
import re  
from playwright.sync_api import expect  
  
# ...  
expect(page).to_have_title(re.compile(r".*checkout"))
```

```
import re  
from playwright.async_api import expect  
  
# ...  
await expect(page).to_have_title(re.compile(r".*checkout"))
```

**Arguments**

* `title_or_reg_exp` str | Pattern 

  Expected title or RegExp.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType

---

### to_have_url[​](#page-assertions-to-have-url "Direct link to to_have_url") pageAssertions.to_have_url

Ensures the page is navigated to the given URL.

**Usage**

* Sync* Async

```
import re  
from playwright.sync_api import expect  
  
# ...  
expect(page).to_have_url(re.compile(".*checkout"))
```

```
import re  
from playwright.async_api import expect  
  
# ...  
await expect(page).to_have_url(re.compile(".*checkout"))
```

**Arguments**

* `url_or_reg_exp` str | Pattern 

  Expected URL string or RegExp.
* `ignore_case` bool *(optional)* 

  Whether to perform case-insensitive match. [ignore_case](Pageassertions.md) option takes precedence over the corresponding regular expression parameter if specified. A provided predicate ignores this flag.
* `timeout` float *(optional)* 

  Time to retry the assertion for in milliseconds. Defaults to `5000`.

**Returns**

* NoneType
