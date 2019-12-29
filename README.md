# aiocached

> **aioached** is a simple package with decorator `cached` to cache results of
>ordinary and coroutine functions with configurable TTL and `None` value support

[![Latest Version](https://img.shields.io/pypi/v/aiocached.svg)](https://pypi.python.org/pypi/aiocached)
[![Python Version](https://img.shields.io/pypi/pyversions/aiocached.svg)](https://pypi.python.org/pypi/aiocached)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


I wrote a simple helper to cache results in one service because I found it easy
to do. As soon as I needed the helper in another project, I realized that it
should be in a separate package published on PyPI. Having found `aiocache`
project I was disappointed because it wasn't able to cache `None` values.
So I had a reason to create `aiocached`.


Table of contents
--------------------------------------------------------------------------------
* [Usage examples](#usage-examples)
* [Installation](#installation)

Usage examples
--------------------------------------------------------------------------------

In this example `foo(1)` will be run just once:
```python
import asyncio
from aiocached import cached

@cached
async def foo(n):
    await asyncio.sleep(n)

async def main():
    await asyncio.gather(*[foo(1) for _ in range(1000)])

asyncio.run(main())
```

In this example `bar(1)` will be run twice because of TTL:
```python
import asyncio
from aiocached import cached

@cached(ttl=2)
async def bar(n):
    await asyncio.sleep(n)

async def main():
    await bar(1)
    await asyncio.sleep(2)
    await bar(1)

asyncio.run(main())
```

If you want to cache an ordinary function, you can do it as well. In this
example `foobar(1)` will be run twice for the same reason as above:
```python
import time
from aiocached import cached

@cached(ttl=2)
def foobar(n):
    time.sleep(n)

def main():
    foobar(1)
    time.sleep(2)
    foobar(1)

main()
```

Installation
--------------------------------------------------------------------------------

Use pip to install:
```shell
$ pip install aiocached
```
