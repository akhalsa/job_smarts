# CDPSession

Source: https://playwright.dev/python/docs/api/class-cdpsession

---

The `CDPSession` instances are used to talk raw Chrome Devtools Protocol:

* protocol methods can be called with `session.send` method.
* protocol events can be subscribed to with `session.on` method.

Useful links:

* Documentation on DevTools Protocol can be found here: [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/).
* Getting Started with DevTools Protocol: <https://github.com/aslushnikov/getting-started-with-cdp/blob/master/README.md>

* Sync* Async

```
client = page.context.new_cdp_session(page)  
client.send("Animation.enable")  
client.on("Animation.animationCreated", lambda: print("animation created!"))  
response = client.send("Animation.getPlaybackRate")  
print("playback rate is " + str(response["playbackRate"]))  
client.send("Animation.setPlaybackRate", {  
    "playbackRate": response["playbackRate"] / 2  
})
```

```
client = await page.context.new_cdp_session(page)  
await client.send("Animation.enable")  
client.on("Animation.animationCreated", lambda: print("animation created!"))  
response = await client.send("Animation.getPlaybackRate")  
print("playback rate is " + str(response["playbackRate"]))  
await client.send("Animation.setPlaybackRate", {  
    "playbackRate": response["playbackRate"] / 2  
})
```

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### detach[​](#cdp-session-detach "Direct link to detach")

Added before v1.9
cdpSession.detach

Detaches the CDPSession from the target. Once detached, the CDPSession object won't emit any events and can't be used to send messages.

**Usage**

```
cdp_session.detach()
```

**Returns**

* NoneType

---

### send[​](#cdp-session-send "Direct link to send")

Added before v1.9
cdpSession.send

**Usage**

```
cdp_session.send(method)  
cdp_session.send(method, **kwargs)
```

**Arguments**

* `method` str

  Protocol method name.
* `params` Dict *(optional)*

  Optional method parameters.

**Returns**

* Dict
