# Error

Source: https://playwright.dev/python/docs/api/class-error

---

* extends: Exception

Error is raised whenever certain operations are terminated abnormally, e.g. browser closes while [page.evaluate()](Page.md) is running. All Playwright exceptions inherit from this class.

---

Properties[​](#properties "Direct link to Properties")
------------------------------------------------------

### message[​](#error-message "Direct link to message") error.message

Message of the error.

**Usage**

```
error.message
```

**Type**

* str

---

### name[​](#error-name "Direct link to name") error.name

Name of the error which got thrown inside the browser. Optional.

**Usage**

```
error.name
```

**Type**

* str

---

### stack[​](#error-stack "Direct link to stack") error.stack

Stack of the error which got thrown inside the browser. Optional.

**Usage**

```
error.stack
```

**Type**

* str

* [Properties](#properties)
  + [message](#error-message)+ [name](#error-name)+ [stack](#error-stack)
