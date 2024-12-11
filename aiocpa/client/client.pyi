from builtins import bool as _bool
from builtins import float as _float
from builtins import list as _list
from collections.abc import Awaitable, Callable, Generator
from datetime import datetime
from types import NoneType as _NoneType
from typing import Any, TypeVar

from typing_extensions import Self

from aiocpa.client import APIServer
from aiocpa.enums import (
    Asset,
    CheckStatus,
    CurrencyType,
    Fiat,
    InvoiceStatus,
    LiteralAsset,
    LiteralCheckStatus,
    LiteralCurrencyType,
    LiteralFiat,
    LiteralInvoiceStatus,
    LiteralPaidBtnName,
    PaidBtnName,
)
from aiocpa.methods import CryptoPayMethod
from aiocpa.polling import PollingConfig
from aiocpa.polling.manager import Handler, PollingTask
from aiocpa.types import (
    App,
    AppStats,
    Balance,
    Check,
    Currency,
    ExchangeRate,
    Invoice,
    Transfer,
    _CryptoPayType,
)
from aiocpa.webhook import (
    _APP,
    WebhookManager,
)

from .session import BaseSession

_T = TypeVar("_T")

# These classes are needed for syncronous type hinting.
# Stub file annotates the methods as syncronous, but
# while using this lib asynchronously, the actual return type
# is a coroutine that returns an annotated type, so these classes
# will annotate awaited object as return type.

class list(_list[_T]):  # noqa: A001, N801
    def __await__(self) -> Generator[None, None, Self]: ...

class bool(_bool):  # type: ignore[misc]  # noqa: A001, N801
    def __await__(self) -> Generator[None, None, Self]: ...

class float(_float):  # noqa: A001, N801
    def __await__(self) -> Generator[None, None, Self]: ...

class NoneType(_NoneType):  # type: ignore[misc, valid-type]
    def __await__(self) -> Generator[None, None, None]: ...

class CryptoPay:
    _token: str
    session: BaseSession
    _timeout: int
    _delay: int
    _tasks: dict[int, PollingTask]
    _handler: Handler | None
    _exp_handler: Handler | None
    _webhook_manager: WebhookManager

    def __init__(
        self,
        token: str,
        api_server: APIServer = ...,
        session: type[BaseSession] = ...,
        manager: WebhookManager[_APP] | None = None,
        polling_config: PollingConfig | None = None,
    ) -> None: ...
    async def __call__(
        self,
        method: CryptoPayMethod[_CryptoPayType],
    ) -> _CryptoPayType: ...
    def get_me(self) -> App: ...
    def create_invoice(
        self,
        amount: _float,
        asset: Asset | LiteralAsset | str | None = None,
        *,
        currency_type: CurrencyType | LiteralCurrencyType | str | None = None,
        fiat: Fiat | LiteralFiat | str | None = None,
        accepted_assets: _list[Asset | LiteralAsset | str] | None = None,
        description: str | None = None,
        hidden_message: str | None = None,
        paid_btn_name: PaidBtnName | LiteralPaidBtnName | str | None = None,
        paid_btn_url: str | None = None,
        payload: str | None = None,
        allow_comments: bool | None = None,
        allow_anonymous: bool | None = None,
        expires_in: int | None = None,
    ) -> Invoice: ...
    def delete_invoice(
        self,
        invoice_id: int,
    ) -> bool: ...
    def create_check(
        self,
        amount: _float,
        asset: Asset | LiteralAsset | str,
        pin_to_user_id: int | None = None,
        pin_to_username: str | None = None,
    ) -> Check: ...
    def delete_check(
        self,
        check_id: int,
    ) -> bool: ...
    def transfer(
        self,
        user_id: int,
        asset: str,
        amount: _float,
        spend_id: str | None = None,
        comment: str | None = None,
        disable_send_notification: bool | None = None,
    ) -> Transfer: ...
    def get_invoices(
        self,
        asset: Asset | LiteralAsset | str | None = None,
        fiat: Fiat | LiteralFiat | str | None = None,
        invoice_ids: _list[int] | None = None,
        status: InvoiceStatus | LiteralInvoiceStatus | str | None = None,
        offset: int | None = None,
        count: int | None = None,
    ) -> list[Invoice]: ...
    def get_checks(
        self,
        asset: Asset | LiteralAsset | str | None = None,
        check_ids: _list[int] | None = None,
        status: CheckStatus | LiteralCheckStatus | str | None = None,
        offset: int | None = None,
        count: int | None = None,
    ) -> list[Check]: ...
    def get_transfers(
        self,
        asset: Asset | LiteralAsset | str | None = None,
        transfer_ids: _list[int] | None = None,
        spend_id: str | None = None,
        offset: int | None = None,
        count: int | None = None,
    ) -> list[Transfer]: ...
    def get_balance(self) -> list[Balance]: ...
    def get_exchange_rates(self) -> list[ExchangeRate]: ...
    def get_currencies(self) -> list[Currency]: ...
    def get_stats(
        self,
        start_at: datetime | None = None,
        end_at: datetime | None = None,
    ) -> AppStats: ...
    def delete_all_checks(self) -> NoneType: ...
    def delete_all_invoices(self) -> NoneType: ...
    def exchange(
        self,
        amount: _float,
        source: Asset | LiteralAsset | Fiat | LiteralFiat | str,
        target: Asset | LiteralAsset | Fiat | LiteralFiat | str,
    ) -> float: ...
    def get_balance_by_asset(
        self,
        asset: Asset | LiteralAsset | str,
    ) -> float: ...
    def polling_handler(self) -> Callable[[Handler], Handler]: ...
    def expired_handler(self) -> Callable[[Handler], Handler]: ...
    def webhook_handler(
        self,
        app: _APP,
        path: str,
    ) -> Callable[
        [Callable[[Invoice], Awaitable]],
        Callable[[Invoice], Awaitable],
    ]: ...
    def feed_update(
        self,
        handler: Callable[[Invoice], Awaitable],
        body: dict[str, Any],
        headers: dict[str, str],
    ) -> NoneType: ...
    async def __process_invoice(
        self,
        invoice: Invoice,
    ) -> NoneType: ...
    def _add_invoice(
        self,
        invoice: Invoice,
        data: dict[str, Any],
    ) -> NoneType: ...
    def start_polling(
        self,
        parallel: Callable[[], Any] | None = None,
    ) -> NoneType: ...
    def get_invoice(
        self,
        invoice: int | Invoice,
    ) -> Invoice | NoneType: ...
