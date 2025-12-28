# Response

Source: https://playwright.dev/python/docs/api/class-response

---

[Response](Response.md) class represents responses which are received by page.

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### all_headers[​](#response-all-headers "Direct link to all_headers") response.all_headers

An object with all the response HTTP headers associated with this response.

**Usage**

```
response.all_headers()
```

**Returns**

* Dict[str, str]

---

### body[​](#response-body "Direct link to body")

Added before v1.9
response.body

Returns the buffer with response body.

**Usage**

```
response.body()
```

**Returns**

* bytes

---

### finished[​](#response-finished "Direct link to finished")

Added before v1.9
response.finished

Waits for this response to finish, returns always `null`.

**Usage**

```
response.finished()
```

**Returns**

* NoneType | str

---

### header_value[​](#response-header-value "Direct link to header_value") response.header_value

Returns the value of the header matching the name. The name is case-insensitive. If multiple headers have the same name (except `set-cookie`), they are returned as a list separated by `,` . For `set-cookie`, the `\n` separator is used. If no headers are found, `null` is returned.

**Usage**

```
response.header_value(name)
```

**Arguments**

* `name` str

  Name of the header.

**Returns**

* NoneType | str

---

### header_values[​](#response-header-values "Direct link to header_values") response.header_values

Returns all values of the headers matching the name, for example `set-cookie`. The name is case-insensitive.

**Usage**

```
response.header_values(name)
```

**Arguments**

* `name` str

  Name of the header.

**Returns**

* List[str]

---

### headers_array[​](#response-headers-array "Direct link to headers_array") response.headers_array

An array with all the request HTTP headers associated with this response. Unlike [response.all_headers()](Response.md), header names are NOT lower-cased. Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.

**Usage**

```
response.headers_array()
```

**Returns**

* List[Dict]
  + `name` str

    Name of the header.
  + `value` str

    Value of the header.

---

### json[​](#response-json "Direct link to json")

Added before v1.9
response.json

Returns the JSON representation of response body.

This method will throw if the response body is not parsable via `JSON.parse`.

**Usage**

```
response.json()
```

**Returns**

* Dict

---

### security_details[​](#response-security-details "Direct link to security_details") response.security_details

Returns SSL and other security information.

**Usage**

```
response.security_details()
```

**Returns**

* NoneType | Dict
  + `issuer` str *(optional)*

    Common Name component of the Issuer field. from the certificate. This should only be used for informational purposes. Optional.
  + `protocol` str *(optional)*

    The specific TLS protocol used. (e.g. `TLS 1.3`). Optional.
  + `subjectName` str *(optional)*

    Common Name component of the Subject field from the certificate. This should only be used for informational purposes. Optional.
  + `validFrom` float *(optional)*

    Unix timestamp (in seconds) specifying when this cert becomes valid. Optional.
  + `validTo` float *(optional)*

    Unix timestamp (in seconds) specifying when this cert becomes invalid. Optional.

---

### server_addr[​](#response-server-addr "Direct link to server_addr") response.server_addr

Returns the IP address and port of the server.

**Usage**

```
response.server_addr()
```

**Returns**

* NoneType | Dict
  + `ipAddress` str

    IPv4 or IPV6 address of the server.
  + `port` int

---

### text[​](#response-text "Direct link to text")

Added before v1.9
response.text

Returns the text representation of response body.

**Usage**

```
response.text()
```

**Returns**

* str

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### frame[​](#response-frame "Direct link to frame")

Added before v1.9
response.frame

Returns the [Frame](Frame.md) that initiated this response.

**Usage**

```
response.frame
```

**Returns**

* [Frame](Frame.md)

---

### from_service_worker[​](#response-from-service-worker "Direct link to from_service_worker") response.from_service_worker

Indicates whether this Response was fulfilled by a Service Worker's Fetch Handler (i.e. via [FetchEvent.respondWith](https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent/respondWith)).

**Usage**

```
response.from_service_worker
```

**Returns**

* bool

---

### headers[​](#response-headers "Direct link to headers")

Added before v1.9
response.headers

An object with the response HTTP headers. The header names are lower-cased. Note that this method does not return security-related headers, including cookie-related ones. You can use [response.all_headers()](Response.md) for complete list of headers that include `cookie` information.

**Usage**

```
response.headers
```

**Returns**

* Dict[str, str]

---

### ok[​](#response-ok "Direct link to ok")

Added before v1.9
response.ok

Contains a boolean stating whether the response was successful (status in the range 200-299) or not.

**Usage**

```
response.ok
```

**Returns**

* bool

---

### request[​](#response-request "Direct link to request")

Added before v1.9
response.request

Returns the matching [Request](Request.md) object.

**Usage**

```
response.request
```

**Returns**

* [Request](Request.md)

---

### status[​](#response-status "Direct link to status")

Added before v1.9
response.status

Contains the status code of the response (e.g., 200 for a success).

**Usage**

```
response.status
```

**Returns**

* int

---

### status_text[​](#response-status-text "Direct link to status_text")

Added before v1.9
response.status_text

Contains the status text of the response (e.g. usually an "OK" for a success).

**Usage**

```
response.status_text
```

**Returns**

* str

---

### url[​](#response-url "Direct link to url")

Added before v1.9
response.url

Contains the URL of the response.

**Usage**

```
response.url
```

**Returns**

* str
