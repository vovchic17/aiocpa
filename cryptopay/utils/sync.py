import asyncio
import functools
import inspect

from cryptopay.client import CryptoPay
from cryptopay.types import CryptoPayObject


def async_to_sync(obj: object, name: str) -> None:
    """Set asyncio event loop if it's not running."""
    method = getattr(obj, name)

    @functools.wraps(method)
    def sync_wrapper(*args, **kwargs) -> object:
        coro = method(*args, **kwargs)
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        if loop.is_running():
            return coro
        return loop.run_until_complete(coro)

    setattr(obj, name, sync_wrapper)


def syncify(obj: object) -> None:
    """Add decorators to all public methods of the object."""
    for name in dir(obj):
        if not name.startswith("_") and inspect.iscoroutinefunction(
            getattr(obj, name),
        ):
            async_to_sync(obj, name)


for base in (*CryptoPay.__bases__, *CryptoPayObject.__subclasses__()):
    syncify(base)
