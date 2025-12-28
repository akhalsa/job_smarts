# Download

Source: https://playwright.dev/python/docs/api/class-download

---

[Download](Download.md) objects are dispatched by page via the [page.on("download")](Page.md) event.

All the downloaded files belonging to the browser context are deleted when the browser context is closed.

Download event is emitted once the download starts. Download path becomes available once download completes.

* Sync* Async

```
# Start waiting for the download  
with page.expect_download() as download_info:  
    # Perform the action that initiates download  
    page.get_by_text("Download file").click()  
download = download_info.value  
  
# Wait for the download process to complete and save the downloaded file somewhere  
download.save_as("/path/to/save/at/" + download.suggested_filename)
```

```
# Start waiting for the download  
async with page.expect_download() as download_info:  
    # Perform the action that initiates download  
    await page.get_by_text("Download file").click()  
download = await download_info.value  
  
# Wait for the download process to complete and save the downloaded file somewhere  
await download.save_as("/path/to/save/at/" + download.suggested_filename)
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### cancel[​](#download-cancel "Direct link to cancel") download.cancel

Cancels a download. Will not fail if the download is already finished or canceled. Upon successful cancellations, `download.failure()` would resolve to `'canceled'`.

**Usage**

```
download.cancel()
```

**Returns**

* NoneType

---

### delete[​](#download-delete "Direct link to delete")

Added before v1.9
download.delete

Deletes the downloaded file. Will wait for the download to finish if necessary.

**Usage**

```
download.delete()
```

**Returns**

* NoneType

---

### failure[​](#download-failure "Direct link to failure")

Added before v1.9
download.failure

Returns download error if any. Will wait for the download to finish if necessary.

**Usage**

```
download.failure()
```

**Returns**

* NoneType | str

---

### path[​](#download-path "Direct link to path")

Added before v1.9
download.path

Returns path to the downloaded file for a successful download, or throws for a failed/canceled download. The method will wait for the download to finish if necessary. The method throws when connected remotely.

Note that the download's file name is a random GUID, use [download.suggested_filename](Download.md) to get suggested file name.

**Usage**

```
download.path()
```

**Returns**

* pathlib.Path

---

### save_as[​](#download-save-as "Direct link to save_as")

Added before v1.9
download.save_as

Copy the download to a user-specified path. It is safe to call this method while the download is still in progress. Will wait for the download to finish if necessary.

**Usage**

* Sync* Async

```
download.save_as("/path/to/save/at/" + download.suggested_filename)
```

```
await download.save_as("/path/to/save/at/" + download.suggested_filename)
```

**Arguments**

* `path` Union[str, pathlib.Path]

  Path where the download should be copied.

**Returns**

* NoneType

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### page[​](#download-page "Direct link to page") download.page

Get the page that the download belongs to.

**Usage**

```
download.page
```

**Returns**

* [Page](Page.md)

---

### suggested_filename[​](#download-suggested-filename "Direct link to suggested_filename")

Added before v1.9
download.suggested_filename

Returns suggested filename for this download. It is typically computed by the browser from the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) response header or the `download` attribute. See the spec on [whatwg](https://html.spec.whatwg.org/#downloading-resources). Different browsers can use different logic for computing it.

**Usage**

```
download.suggested_filename
```

**Returns**

* str

---

### url[​](#download-url "Direct link to url")

Added before v1.9
download.url

Returns downloaded url.

**Usage**

```
download.url
```

**Returns**

* str
