# labylib
### Cosmetics API for Labymod

Set and update Labymod cosmetics programmatically.

|![VicW](https://crafatar.com/renders/body/53c40674-f0a2-4f95-9ce1-479bdd1d8b67?scale=2) | Created by VicW | 
|--|--|

## Installation
1. Download and install [Python 3.x.x](https://www.python.org/downloads/) for your computer's architecture
2. Clone this repo to your machine, or [download a zip](/VictorWesterlund/labylib/archive/master.zip) if you don't speak git
```bash
$ git clone https://github.com/VictorWesterlund/labylib/
$ gh repo clone VictorWesterlund/labylib
```
3. Extract/copy the `labylib` folder into your project (or make it a dependancy)

## Quickstart
_**NOTE:**_ _labylib relies on a supplied `PHPSESSID`-cookie from 'labymod.net' to execute its requests. Follow this [this step-by-step guide](#find-your-phpsessid-cookie) to find your `PHPSESSID`_

**1. Start by importing a module from `labylib/<cosmetic>`. All [supported cosmetics](#supported-cosmetics) are self-contained modules.**
```python
from labylib import Cape
```
**2. Initialize the `Texture()` class.**

All modules take a required `PHPSESSID` as their first argument. The second argument varies depending on the cosmetic.

_Example with `Cape` where a file-path is expected:_
```python
texture = Cape.Texture("<String PHPSESSID>","<String PATH_TO_PNG>") # labylib = Cape.Texture("772nnas663jkc8ahbb2","/home/VicW/coolCape-2.png")
```

**3. Submit a cosmetic update**
```python
texture.update()
```
Normal Python "Built-in"-exceptions are rasied for missing texture files (`FileNotFoundError`) etc. If a request was sucuessfully sent to the Labymod endpoint, but it returned something falsey (not `OK`). A custom-defined `RequestError` exception will be raised. It contains the message received from the endpoint server.
```python
try:
  texture.update()
except RequestError as error:
  print("Caugh RequestError exception:" + error)
# "Caugh RequestError exception: Session expired"
```

## Advanced usage
### HTTP POST Headers
Request header and cookie dictionaries can be accessed and modified pre-submission by referencing `this.headers` and `this.cookies` respectivly.
```python
texture = Cape.Texture("<String PHPSESSID>","<String PATH_TO_PNG>")

texture.headers["Origin"] = "https://example.com/"
texture.cookies["Foo"] = "Bar"

labylib.update()
```
### HTTP POST Body
Binary form-data can be added by calling `self.appendBinaryFormData(name,payload)`. Attach `Content-Type`-less form data by supplying a 'name' and 'payload'. Setting 'name' to "file" allows you to upload a `image/png` as BLOB. "payload" excpects a file-path in this case
```python
texture = Cape.Texture("<String PHPSESSID>","<String PATH_TO_PNG>")

texture.appendBinaryFormData(b"foo",b"bar")
texture.appendBinaryFormData(b"file","/home/VicW/home/VicW/coolCape-2.png") # Note that 'payload' is a String in this case (as opposed to Binary)
```

# Additional information:

## Find your `PHPSESSID`-cookie
Instructions for your browser:
* [Chrome](#chrome)
* [Firefox](#firefox)
* [Safari](#safari)

### Chrome
1. Open [labymod.net](https://www.labymod.net/) and log in with your Labymod account
2. Press <kbd>F12</kbd> on your keyboard (or <kbd>Ctrl</kbd>+<kbd>⇧ Shift</kbd>+<kbd>I</kbd>) to open DevTools
4. Click on the `Application` tab.
5. Expand `Cookies` under the `Storage` cateogry in the sidebar and select `https://www.labymod.net/`
6. Type `PHPSESSID` into the search box called 'Filter'
7. Copy `Value`(PHPSESSID) from the filtered table. If nothing comes up; try navigating to another page on labymod.net
8. Close DevTools

### Firefox
1. Open [labymod.net](https://www.labymod.net/) and log in with your Labymod account
2. Press <kbd>F12</kbd> on your keyboard (or Right-click the page and select "Inspect Element") to open Developer Tools
4. Click on the `Storage` tab.
5. `Cookies` should already be expanded and selected, but if it isn't; expand it and select `https://www.labymod.net`
6. Using the search bar called 'Filter items', type: `PHPSESSID`
7. Copy `Value`(PHPSESSID) from the filtered table. If nothing comes up; try navigating to another page on labymod.net
8. Close Developer Tools

### Safari
1. Open [labymod.net](https://www.labymod.net/) and log in with your Labymod account
2. Right-click the page and select "Inspect Element" (or <kbd>⌥ Option</kbd>+<kbd>⌘ Command</kbd>+<kbd>I</kbd>) to open Web Inspector
4. Click on the `Storage` tab.
5. Expand `Cookies` in the sidebar and select `labymod.net`
6. Find `PHPSESSID` in the table under the 'Name' column
7. Copy `Value`(PHPSESSID) from the filtered table. If nothing comes up; try navigating to another page on labymod.net
8. Close Web Inspector

### Supported cosmetics
| Labymod cosmetic | labylib module name |
|--|--|
| Cloak | Cape |
