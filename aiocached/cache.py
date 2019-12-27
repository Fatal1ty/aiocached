from time import time


UNLIMITED = None


class Cache:
    def __init__(self, ttl=UNLIMITED):
        self.dictionary = {}
        self.ttl = ttl
        self.times = {}

    def __getitem__(self, item):
        if self.ttl is not UNLIMITED:
            self.remove_if_old(item)
        return self.dictionary[item]

    def __setitem__(self, key, value):
        self.dictionary[key] = value
        if self.ttl is not UNLIMITED:
            self.times[key] = time()

    def remove_if_old(self, item):
        t = self.times.get(item)
        if t and time() - t > self.ttl:
            del self.dictionary[item]
            del self.times[item]


class AsyncCache(Cache):
    def __init__(self, *args, **kwargs):
        super(AsyncCache, self).__init__(*args, **kwargs)
        self.futures = {}

    async def get(self, item):
        if self.ttl is not UNLIMITED:
            self.remove_if_old(item)
        try:
            return self.dictionary[item]
        except KeyError as e:
            fut = self.futures.get(item)
            if fut:
                await fut
                return fut.result()
            else:
                raise e from None

    def remove_if_old(self, item):
        t = self.times.get(item)
        if t and time() - t > self.ttl:
            del self.dictionary[item]
            del self.times[item]
            del self.futures[item]


__all__ = [
    'Cache',
    'AsyncCache',
    'UNLIMITED',
]
