# FileChooser

Source: https://playwright.dev/python/docs/api/class-filechooser

---

[FileChooser](Filechooser.md) objects are dispatched by the page in the [page.on("filechooser")](Page.md) event.

* Sync* Async

```
with page.expect_file_chooser() as fc_info:  
    page.get_by_text("Upload file").click()  
file_chooser = fc_info.value  
file_chooser.set_files("myfile.pdf")
```

```
async with page.expect_file_chooser() as fc_info:  
    await page.get_by_text("Upload file").click()  
file_chooser = await fc_info.value  
await file_chooser.set_files("myfile.pdf")
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### set_files[​](#file-chooser-set-files "Direct link to set_files")

Added before v1.9
fileChooser.set_files

Sets the value of the file input this chooser is associated with. If some of the `filePaths` are relative paths, then they are resolved relative to the current working directory. For empty array, clears the selected files.

**Usage**

```
file_chooser.set_files(files)  
file_chooser.set_files(files, **kwargs)
```

**Arguments**

* `files` Union[str, pathlib.Path] | List[Union[str, pathlib.Path]] | Dict | List[Dict]

  + `name` str

    File name
  + `mimeType` str

    File type
  + `buffer` bytes

    File content
* `no_wait_after` bool *(optional)*

  Deprecated

  This option has no effect.

  This option has no effect.
* `timeout` float *(optional)*

  Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the [browser_context.set_default_timeout()](Browsercontext.md) or [page.set_default_timeout()](Page.md) methods.

**Returns**

* NoneType

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### element[​](#file-chooser-element "Direct link to element")

Added before v1.9
fileChooser.element

Returns input element associated with this file chooser.

**Usage**

```
file_chooser.element
```

**Returns**

* [ElementHandle](Elementhandle.md)

---

### is_multiple[​](#file-chooser-is-multiple "Direct link to is_multiple")

Added before v1.9
fileChooser.is_multiple

Returns whether this file chooser accepts multiple files.

**Usage**

```
file_chooser.is_multiple()
```

**Returns**

* bool

---

### page[​](#file-chooser-page "Direct link to page")

Added before v1.9
fileChooser.page

Returns page this file chooser belongs to.

**Usage**

```
file_chooser.page
```

**Returns**

* [Page](Page.md)
