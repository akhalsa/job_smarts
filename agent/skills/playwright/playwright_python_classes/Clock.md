# Clock

Source: https://playwright.dev/python/docs/api/class-clock

---

Accurately simulating time-dependent behavior is essential for verifying the correctness of applications. Learn more about [clock emulation](/python/docs/clock).

Note that clock is installed for the entire [BrowserContext](Browsercontext.md), so the time in all the pages and iframes is controlled by the same clock.

---

Methods[​](#methods "Direct link to Methods")
---------------------------------------------

### fast_forward[​](#clock-fast-forward "Direct link to fast_forward") clock.fast_forward

Advance the clock by jumping forward in time. Only fires due timers at most once. This is equivalent to user closing the laptop lid for a while and reopening it later, after given time.

**Usage**

* Sync* Async

```
page.clock.fast_forward(1000)  
page.clock.fast_forward("30:00")
```

```
await page.clock.fast_forward(1000)  
await page.clock.fast_forward("30:00")
```

**Arguments**

* `ticks` int | str

  Time may be the number of milliseconds to advance the clock by or a human-readable string. Valid string formats are "08" for eight seconds, "01:00" for one minute and "02:34:10" for two hours, 34 minutes and ten seconds.

**Returns**

* NoneType

---

### install[​](#clock-install "Direct link to install") clock.install

Install fake implementations for the following time-related functions:

* `Date`
* `setTimeout`
* `clearTimeout`
* `setInterval`
* `clearInterval`
* `requestAnimationFrame`
* `cancelAnimationFrame`
* `requestIdleCallback`
* `cancelIdleCallback`
* `performance`

Fake timers are used to manually control the flow of time in tests. They allow you to advance time, fire timers, and control the behavior of time-dependent functions. See [clock.run_for()](Clock.md) and [clock.fast_forward()](Clock.md) for more information.

**Usage**

```
clock.install()  
clock.install(**kwargs)
```

**Arguments**

* `time` float | str | datetime *(optional)*

  Time to initialize with, current system time by default.

**Returns**

* NoneType

---

### pause_at[​](#clock-pause-at "Direct link to pause_at") clock.pause_at

Advance the clock by jumping forward in time and pause the time. Once this method is called, no timers are fired unless [clock.run_for()](Clock.md), [clock.fast_forward()](Clock.md), [clock.pause_at()](Clock.md) or [clock.resume()](Clock.md) is called.

Only fires due timers at most once. This is equivalent to user closing the laptop lid for a while and reopening it at the specified time and pausing.

**Usage**

* Sync* Async

```
page.clock.pause_at(datetime.datetime(2020, 2, 2))  
page.clock.pause_at("2020-02-02")
```

```
await page.clock.pause_at(datetime.datetime(2020, 2, 2))  
await page.clock.pause_at("2020-02-02")
```

For best results, install the clock before navigating the page and set it to a time slightly before the intended test time. This ensures that all timers run normally during page loading, preventing the page from getting stuck. Once the page has fully loaded, you can safely use [clock.pause_at()](Clock.md) to pause the clock.

* Sync* Async

```
# Initialize clock with some time before the test time and let the page load  
# naturally. `Date.now` will progress as the timers fire.  
page.clock.install(time=datetime.datetime(2024, 12, 10, 8, 0, 0))  
page.goto("http://localhost:3333")  
page.clock.pause_at(datetime.datetime(2024, 12, 10, 10, 0, 0))
```

```
# Initialize clock with some time before the test time and let the page load  
# naturally. `Date.now` will progress as the timers fire.  
await page.clock.install(time=datetime.datetime(2024, 12, 10, 8, 0, 0))  
await page.goto("http://localhost:3333")  
await page.clock.pause_at(datetime.datetime(2024, 12, 10, 10, 0, 0))
```

**Arguments**

* `time` float | str | datetime

  Time to pause at.

**Returns**

* NoneType

---

### resume[​](#clock-resume "Direct link to resume") clock.resume

Resumes timers. Once this method is called, time resumes flowing, timers are fired as usual.

**Usage**

```
clock.resume()
```

**Returns**

* NoneType

---

### run_for[​](#clock-run-for "Direct link to run_for") clock.run_for

Advance the clock, firing all the time-related callbacks.

**Usage**

* Sync* Async

```
page.clock.run_for(1000);  
page.clock.run_for("30:00")
```

```
await page.clock.run_for(1000);  
await page.clock.run_for("30:00")
```

**Arguments**

* `ticks` int | str

  Time may be the number of milliseconds to advance the clock by or a human-readable string. Valid string formats are "08" for eight seconds, "01:00" for one minute and "02:34:10" for two hours, 34 minutes and ten seconds.

**Returns**

* NoneType

---

### set_fixed_time[​](#clock-set-fixed-time "Direct link to set_fixed_time") clock.set_fixed_time

Makes `Date.now` and `new Date()` return fixed fake time at all times, keeps all the timers running.

Use this method for simple scenarios where you only need to test with a predefined time. For more advanced scenarios, use [clock.install()](Clock.md) instead. Read docs on [clock emulation](/python/docs/clock) to learn more.

**Usage**

* Sync* Async

```
page.clock.set_fixed_time(datetime.datetime.now())  
page.clock.set_fixed_time(datetime.datetime(2020, 2, 2))  
page.clock.set_fixed_time("2020-02-02")
```

```
await page.clock.set_fixed_time(datetime.datetime.now())  
await page.clock.set_fixed_time(datetime.datetime(2020, 2, 2))  
await page.clock.set_fixed_time("2020-02-02")
```

**Arguments**

* `time` float | str | datetime

  Time to be set.

**Returns**

* NoneType

---

### set_system_time[​](#clock-set-system-time "Direct link to set_system_time") clock.set_system_time

Sets system time, but does not trigger any timers. Use this to test how the web page reacts to a time shift, for example switching from summer to winter time, or changing time zones.

**Usage**

* Sync* Async

```
page.clock.set_system_time(datetime.datetime.now())  
page.clock.set_system_time(datetime.datetime(2020, 2, 2))  
page.clock.set_system_time("2020-02-02")
```

```
await page.clock.set_system_time(datetime.datetime.now())  
await page.clock.set_system_time(datetime.datetime(2020, 2, 2))  
await page.clock.set_system_time("2020-02-02")
```

**Arguments**

* `time` float | str | datetime

  Time to be set.

**Returns**

* NoneType
