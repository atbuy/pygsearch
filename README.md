# pygsearch

![pypi version info](https://img.shields.io/pypi/v/pygsearch.svg)
![python version support](https://img.shields.io/pypi/pyversions/pygsearch.svg)


`pygsearch` is a python library that let's you use google search.
Right now you can't search for images. Image support might be added later. PRs are welcome.


Installing
-----------

**Python 3.6.0 or higher is required**

To install the library you can run the following command:

```sh
# Linux/MacOS
python3 -m pip install --upgrade pygsearch

# Windows
py -3 -m pip install --upgrade pygsearch
```

Quickstart
----------

You can make a simple search query like this:

```py
from pygsearch import gsearch

search = gsearch("github")
print(search.results)
```

Or you can iterate over the results:

```py
from pygsearch import gsearch

results = gsearch("github")
for result in results:
    print(result)
```

You can also change how many results you want, pass your own headers, use proxies or even change the language:

```py
from pygsearch import gsearch

proxies = {
    "http": "proxy_http",
    "https": "proxy_https",
    "ftp": "proxy_ftp"
}

headers = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3",
}

language = "en"
search = gsearch("github", 20, language, headers, proxies)
print(search.results)
```
