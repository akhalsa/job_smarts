# APIRequest

Source: https://playwright.dev/python/docs/api/class-apirequest

---

Exposes API that can be used for the Web API testing. This class is used for creating [APIRequestContext](APIRequestContext.md) instance which in turn can be used for sending web requests. An instance of this class can be obtained via `playwright.request` (see [Playwright](Playwright.md)). For more information see [APIRequestContext](APIRequestContext.md).

---

## Methods

### new_context

Creates new instances of [APIRequestContext](APIRequestContext.md).

**Usage**

```python
api_request.new_context()  
api_request.new_context(**kwargs)
```

**Arguments**

* `base_url` str *(optional)*

  Methods like `api_request_context.get()` take the base URL into consideration by using the [`URL()` constructor](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) for building the corresponding URL. Examples:

  + baseURL: `http://localhost:3000` and sending request to `/bar.html` results in `http://localhost:3000/bar.html`
  + baseURL: `http://localhost:3000/foo/` and sending request to `./bar.html` results in `http://localhost:3000/foo/bar.html`
  + baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html`

* `client_certificates` List[Dict] *(optional)*

  + `origin` str

    Exact origin that the certificate is valid for. Origin includes `https` protocol, a hostname and optionally a port.
  + `certPath` Union[str, pathlib.Path] *(optional)*

    Path to the file with the certificate in PEM format.
  + `cert` bytes *(optional)*

    Direct value of the certificate in PEM format.
  + `keyPath` Union[str, pathlib.Path] *(optional)*

    Path to the file with the private key in PEM format.
  + `key` bytes *(optional)*

    Direct value of the private key in PEM format.
  + `pfxPath` Union[str, pathlib.Path] *(optional)*

    Path to the PFX or PKCS12 encoded private key and certificate chain.
  + `pfx` bytes *(optional)*

    Direct value of the PFX or PKCS12 encoded private key and certificate chain.
  + `passphrase` str *(optional)*

    Passphrase for the private key (PEM or PFX).

  TLS Client Authentication allows the server to request a client certificate and verify it.

  **Details**

  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.

  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.

  **Note:** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`.

* `extra_http_headers` Dict[str, str] *(optional)*

  An object containing additional HTTP headers to be sent with every request. Defaults to none.

* `fail_on_status_code` bool *(optional)*

  Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes.

* `http_credentials` Dict *(optional)*

  + `username` str
  + `password` str
  + `origin` str *(optional)*

    Restrain sending http credentials on specific origin (scheme://host:port).
  + `send` "unauthorized" | "always" *(optional)*

    This option only applies to the requests sent from corresponding [APIRequestContext](APIRequestContext.md) and does not affect requests sent from the browser. `'always'` - `Authorization` header with basic authentication credentials will be sent with the each API request. `'unauthorized` - the credentials are only sent when 401 (Unauthorized) response with `WWW-Authenticate` header is received. Defaults to `'unauthorized'`.

  Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.

* `ignore_https_errors` bool *(optional)*

  Whether to ignore HTTPS errors when sending network requests. Defaults to `false`.

* `max_redirects` int *(optional)*

  Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. This can be overwritten for each request individually.

* `proxy` Dict *(optional)*

  + `server` str

    Proxy to be used for all requests. HTTP and SOCKS proxies are supported, for example `http://myproxy.com:3128` or `socks5://myproxy.com:3128`. Short form `myproxy.com:3128` is considered an HTTP proxy.
  + `bypass` str *(optional)*

    Optional comma-separated domains to bypass proxy, for example `".com, chromium.org, .domain.com"`.
  + `username` str *(optional)*

    Optional username to use if HTTP proxy requires authentication.
  + `password` str *(optional)*

    Optional password to use if HTTP proxy requires authentication.

  Network proxy settings.

* `storage_state` Union[str, pathlib.Path] | Dict *(optional)*

  + `cookies` List[Dict]

    - `name` str
    - `value` str
    - `domain` str
    - `path` str
    - `expires` float

      Unix time in seconds.
    - `httpOnly` bool
    - `secure` bool
    - `sameSite` "Strict" | "Lax" | "None"
  + `origins` List[Dict]

    - `origin` str
    - `localStorage` List[Dict]

      * `name` str
      * `value` str

  Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()` (see [BrowserContext](BrowserContext.md)) or `api_request_context.storage_state()` (see [APIRequestContext](APIRequestContext.md)). Either a path to the file with saved storage, or the value returned by one of these methods.

* `timeout` float *(optional)*

  Maximum time in milliseconds to wait for the response. Defaults to `30000` (30 seconds). Pass `0` to disable timeout.

* `user_agent` str *(optional)*

  Specific user agent to use in this context.

**Returns**

* [APIRequestContext](APIRequestContext.md)
