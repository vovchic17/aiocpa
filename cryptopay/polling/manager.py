import asyncio
import inspect
from dataclasses import dataclass
from typing import TYPE_CHECKING, cast

from cryptopay.enums import InvoiceStatus
from cryptopay.exceptions import CryptoPayError

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable
    from typing import Any

    import cryptopay
    from cryptopay.types import Invoice

    Handler = Callable[[Invoice, *Any], Awaitable]


@dataclass(slots=True)
class PollingConfig:
    """Polling configuration."""

    timeout: int = 300
    """Timeout in seconds."""
    delay: int = 2
    """Time to wait between the requests in seconds."""


@dataclass(slots=True)
class PollingTask:
    """
    Wrapper for an Invoice.

    This class is used to make a polling task.
    """

    invoice: "Invoice"
    """Invoice object."""
    timeout: int
    """Remaining time for checking the invoice status."""
    data: "dict[str, Any]"
    """Additional payload"""


class PollingManager:
    """
    Polling manager class.

    This class is used to handle payments
    via invoices polling method.
    """

    def __init__(
        self,
        config: PollingConfig,
    ) -> None:
        self.timeout = config.timeout
        self.delay = config.delay
        self.tasks: dict[int, PollingTask] = {}
        self.handler: Handler | None = None

    def polling_handler(self) -> "Callable[[Handler], Handler]":
        """
        Register a handler for polling invoice updates.

        Decorator for handler function.

        :return: handler function.
        """

        def wrapper(handler: "Handler") -> "Handler":
            self.handler = handler
            return handler

        return wrapper

    def _add_invoice(
        self,
        invoice: "Invoice",
        data: "dict[str, Any]",
    ) -> None:
        self.tasks[invoice.invoice_id] = PollingTask(
            invoice=invoice,
            timeout=self.timeout,
            data=data,
        )

    async def __process_invoice(
        self,
        invoice: "Invoice",
    ) -> None:
        if invoice.status == InvoiceStatus.PAID:
            spec = inspect.getfullargspec(self.handler)
            data = self.tasks[invoice.invoice_id].data
            handler = cast("Handler", self.handler)
            await handler(
                invoice,
                **data
                if spec.varkw is not None
                else {k: v for k, v in data.items() if k in spec.args},
            )
        else:
            self.tasks[invoice.invoice_id].timeout -= self.delay
        if (
            invoice.status in (InvoiceStatus.PAID, InvoiceStatus.EXPIRED)
            or self.tasks[invoice.invoice_id].timeout <= 0
        ):
            del self.tasks[invoice.invoice_id]

    async def run_polling(self: "cryptopay.CryptoPay") -> None:
        """
        Run invoices polling.

        :raises CryptoPayError: when polling handler is not defined.
        """
        if self.handler is None:
            msg = (
                "Polling handler hasn't been declared, example:\n"
                "from cryptopay import CryptoPay\n"
                'cp = CryptoPay("TOKEN")\n'
                "@cp.polling_handler()\n"
                "async def handler(invoice): ..."
            )
            raise CryptoPayError(msg)
        while True:
            await asyncio.sleep(self.delay)
            if not self.tasks:
                continue
            invoices = await self.get_invoices(
                invoice_ids=list(self.tasks),
            )
            for invoice in invoices:
                await self.__process_invoice(invoice)
