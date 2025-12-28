# APIResponseAssertions

Source: https://playwright.dev/python/docs/api/class-apiresponseassertions

---

The [APIResponseAssertions](Apiresponseassertions.md) class provides assertion methods that can be used to make assertions about the [APIResponse](Apiresponse.md) in the tests.

* Sync* Async

```
from playwright.sync_api import Page, expect  
  
def test_navigates_to_login_page(page: Page) -> None:  
    # ..  
    response = page.request.get('https://playwright.dev')  
    expect(response).to_be_ok()
```

```
from playwright.async_api import Page, expect  
  
async def test_navigates_to_login_page(page: Page) -> None:  
    # ..  
    response = await page.request.get('https://playwright.dev')  
    await expect(response).to_be_ok()
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### not_to_be_ok[​](#api-response-assertions-not-to-be-ok "Direct link to not_to_be_ok") apiResponseAssertions.not_to_be_ok

The opposite of [expect(response).to_be_ok()](Apiresponseassertions.md).

**Usage**

```
expect(response).not_to_be_ok()
```

**Returns**

* NoneType

---

### to_be_ok[​](#api-response-assertions-to-be-ok "Direct link to to_be_ok") apiResponseAssertions.to_be_ok

Ensures the response status code is within `200..299` range.

**Usage**

* Sync* Async

```
import re  
from playwright.sync_api import expect  
  
# ...  
expect(response).to_be_ok()
```

```
from playwright.async_api import expect  
  
# ...  
await expect(response).to_be_ok()
```

**Returns**

* NoneType
