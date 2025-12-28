# Video

Source: https://playwright.dev/python/docs/api/class-video

---

When browser context is created with the `recordVideo` option, each page has a video object associated with it.

* Sync* Async

```
print(page.video.path())
```

```
print(await page.video.path())
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### delete[​](#video-delete "Direct link to delete") video.delete

Deletes the video file. Will wait for the video to finish if necessary.

**Usage**

```
video.delete()
```

**Returns**

* NoneType

---

### path[​](#video-path "Direct link to path")

Added before v1.9
video.path

Returns the file system path this video will be recorded to. The video is guaranteed to be written to the filesystem upon closing the browser context. This method throws when connected remotely.

**Usage**

```
video.path()
```

**Returns**

* pathlib.Path

---

### save_as[​](#video-save-as "Direct link to save_as") video.save_as

Saves the video to a user-specified path. It is safe to call this method while the video is still in progress, or after the page has closed. This method waits until the page is closed and the video is fully saved.

**Usage**

```
video.save_as(path)
```

**Arguments**

* `path` Union[str, pathlib.Path]

  Path where the video should be saved.

**Returns**

* NoneType
