![Labylib](https://storage.googleapis.com/public.victorwesterlund.com/github/VictorWesterlund/labylib/labylib.png)

### Cosmetics API for Labymod
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/VictorWesterlund/labylib?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/VictorWesterlund/labylib)
![Maintenance](https://img.shields.io/maintenance/yes/2021)

Modify LabyMod cosmetics programmatically with Python.

|![VicW](https://crafatar.com/renders/body/53c40674-f0a2-4f95-9ce1-479bdd1d8b67?scale=2) | Created by VicW | 
|--|--|

_labylib or Victor Westerlund is in no way sponsored by or affiliated with LabyMod or LabyMedia GmbH._<br>
_This program is offered as-is and might stop working at any time_

## Installation
1. Download and install [Python 3](https://www.python.org/downloads/) for your architecture.
2. Install the latest version of labylib with [`pip3`](https://pypi.org/project/labylib/)
```bash
$ python3 -m pip install labylib
```
*..or if that doesn't work*
```python
$ pip3 install labylib
```

## Quickstart
1. Import a labylib Module from the [list of available modules](https://github.com/VictorWesterlund/labylib/wiki/labylib-Modules).
```python3
from labylib import <MODULE>
```
2. Each Module comes with a set of classes available to each cosmetic. Pick a class for your Module. (`Visibility`,`Texture` etc.)
3. Initialize the class by passing it a `PHPSESSID`<br>
[**Here's what it is and where to find it**](https://github.com/VictorWesterlund/labylib/wiki/Find-your-PHPSESSID)
```python3
# Example
cape_vis = Cape.Visibility(PHPSESSID)
```
4. Call `update()` with a value expected by the class. Just like Modules, the value expected depends on the class.
```python3
# Example
cape_vis.update("show")
```

# Advanced Usage
## Request headers, cookies and body
Each class instance can be modified before `update()` is called to make changes to the request headers, cookies etc. You can even add additional encoded form data to the request body if necessary.

labylib uses [`Requests`](https://requests.readthedocs.io/en/master/) under the hood and request parameters like headers and cookies can be modified in accordance with `Request`'s conventions.
```python3
# This will send add a "foo=bar" cookie and header with the request
cape_vis.cookies["foo"] = "bar"
cape_vis.headers["foo"] = "bar"

cape_vis.update("show")
```

### To append form data to the request body of an instance:

**For `x-www-form-urlencoded` requests:** Append form data with the `addEncodedFormData(key,value)` method:
```python3
# This will add "foo=bar" to the URL encoded payload
cape_vis.addEncodedFormData("foo","bar")
cape_vis.update("show")
```

**For `multipart/form-data` requests:** Append binary form data with the `addBinaryFormData(key,payload)` method:
```python3
# This will create a new payload boundary containing "foo=bar"
cape_texture.addBinaryFormData(b"foor",b"bar")
cape_texture.update("show")
```
You can also append `image/png` files by passing "file" as the `key` argument. You can either pass binary data directly as a BLOB to `payload` or use `bOpen(<Path_to_PNG>)` to load an image from disk:
```python3
# This will create a new payload boundary with a "Content-Type: image/png" header and BLOB body
cape_texture.addBinaryFormData(b"file",cape_vis.bOpen("~/someImage.png"))
cape_texture.update("~/myAwesomeTexture.png")
```

## Contribute

If you find any bugs with- or would like to suggest features to labylib, please submit them under [Issues](https://github.com/VictorWesterlund/labylib/issues)

Pull requests to labylib are highly encouraged!

## License

[GNU General Public License v3.0](https://github.com/VictorWesterlund/labylib/blob/master/LICENSE)
