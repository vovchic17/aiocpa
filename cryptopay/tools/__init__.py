import asyncio
import inspect
from typing import TYPE_CHECKING

from .delete_all_checks import DeleteAllChecks
from .delete_all_invoices import DeleteAllInvoices
from .exchange import Exchange
from .get_balance_by_asset import GetBalanceByAsset

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any, ParamSpecArgs, ParamSpecKwargs

    import cryptopay


class Tools(
    DeleteAllChecks,
    DeleteAllInvoices,
    Exchange,
    GetBalanceByAsset,
):
    def _run_sync_async(
        self: "cryptopay.CryptoPay",
        method: "Callable[..., Any]",
        *args: "ParamSpecArgs",
        **kwargs: "ParamSpecKwargs",
    ) -> object:
        coro = method(*args, **kwargs)
        if inspect.iscoroutinefunction(method):
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(coro)
        return coro


__all__ = (
    "DeleteAllChecks",
    "DeleteAllInvoices",
    "Exchange",
    "GetBalanceByAsset",
)
