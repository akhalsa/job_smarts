# APIResponse

Source: https://playwright.dev/python/docs/api/class-apiresponse

---

[APIResponse](Apiresponse.md) class represents responses returned by [api_request_context.get()](Apirequestcontext.md) and similar methods.

* Sync* Async

```
from playwright.sync_api import sync_playwright  
  
with sync_playwright() as p:  
    context = playwright.request.new_context()  
    response = context.get("https://example.com/user/repos")  
    assert response.ok  
    assert response.status == 200  
    assert response.headers["content-type"] == "application/json; charset=utf-8"  
    assert response.json()["name"] == "foobar"  
    assert response.body() == '{"status": "ok"}'
```

```
import asyncio  
from playwright.async_api import async_playwright, Playwright  
  
async def run(playwright: Playwright):  
    context = await playwright.request.new_context()  
    response = await context.get("https://example.com/user/repos")  
    assert response.ok  
    assert response.status == 200  
    assert response.headers["content-type"] == "application/json; charset=utf-8"  
    json_data = await response.json()  
    assert json_data["name"] == "foobar"  
    assert await response.body() == '{"status": "ok"}'  
  
  
async def main():  
    async with async_playwright() as playwright:  
        await run(playwright)  
  
asyncio.run(main())
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### body[​](#api-response-body "Direct link to body") apiResponse.body

Returns the buffer with response body.

**Usage**

```
api_response.body()
```

**Returns**

* bytes

---

### dispose[​](#api-response-dispose "Direct link to dispose") apiResponse.dispose

Disposes the body of this response. If not called then the body will stay in memory until the context closes.

**Usage**

```
api_response.dispose()
```

**Returns**

* NoneType

---

### json[​](#api-response-json "Direct link to json") apiResponse.json

Returns the JSON representation of response body.

This method will throw if the response body is not parsable via `JSON.parse`.

**Usage**

```
api_response.json()
```

**Returns**

* Dict

---

### text[​](#api-response-text "Direct link to text") apiResponse.text

Returns the text representation of response body.

**Usage**

```
api_response.text()
```

**Returns**

* str

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### headers[​](#api-response-headers "Direct link to headers") apiResponse.headers

An object with all the response HTTP headers associated with this response.

**Usage**

```
api_response.headers
```

**Returns**

* Dict[str, str]

---

### headers_array[​](#api-response-headers-array "Direct link to headers_array") apiResponse.headers_array

An array with all the response HTTP headers associated with this response. Header names are not lower-cased. Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.

**Usage**

```
api_response.headers_array
```

**Returns**

* List[Dict]
  + `name` str

    Name of the header.
  + `value` str

    Value of the header.

---

### ok[​](#api-response-ok "Direct link to ok") apiResponse.ok

Contains a boolean stating whether the response was successful (status in the range 200-299) or not.

**Usage**

```
api_response.ok
```

**Returns**

* bool

---

### status[​](#api-response-status "Direct link to status") apiResponse.status

Contains the status code of the response (e.g., 200 for a success).

**Usage**

```
api_response.status
```

**Returns**

* int

---

### status_text[​](#api-response-status-text "Direct link to status_text") apiResponse.status_text

Contains the status text of the response (e.g. usually an "OK" for a success).

**Usage**

```
api_response.status_text
```

**Returns**

* str

---

### url[​](#api-response-url "Direct link to url") apiResponse.url

Contains the URL of the response.

**Usage**

```
api_response.url
```

**Returns**

* str
