import asyncio
from functools import wraps

from .cache import AsyncCache, UNLIMITED


def cached(ttl=UNLIMITED):

    if callable(ttl):
        return cached(UNLIMITED)(ttl)

    def decorator(func):

        setattr(func, '__cache', AsyncCache(ttl))

        @wraps(func)
        def wrapped(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            try:
                result = func.__cache[cache_key]
            except KeyError:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    raise e from None
                func.__cache[cache_key] = result
            return result

        @wraps(func)
        async def wrapped_coro(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            try:
                result = await func.__cache.get(cache_key)
            except KeyError:
                try:
                    func.__cache.futures[cache_key] = asyncio.Future()
                    result = await func(*args, **kwargs)
                    func.__cache.futures[cache_key].set_result(result)
                except Exception as e:
                    fut = func.__cache.futures.pop(cache_key)
                    fut.cancel()
                    raise e from None
                func.__cache[cache_key] = result
            return result

        if asyncio.iscoroutinefunction(func):
            return wrapped_coro
        else:
            return wrapped

    return decorator


__all__ = [
    'cached',
]
