from typing import TYPE_CHECKING

from pydantic import field_serializer

from cryptopay.enums import Asset, Fiat, InvoiceStatus
from cryptopay.types import Invoice, SerList

from .base import CryptoPayMethod

if TYPE_CHECKING:
    import cryptopay


class GetInvoices:
    """getInvoices method."""

    class GetInvoicesMethod(CryptoPayMethod[list[Invoice]]):
        __return_type__ = list[Invoice]
        __method__ = "getInvoices"

        asset: Asset | str | None
        fiat: Fiat | str | None
        invoice_ids: SerList[int] | None
        status: InvoiceStatus | str | None
        offset: int | None
        count: int | None

        @field_serializer("invoice_ids")
        def serialize_ids(self, value: list[int] | None) -> str | None:
            """Serialize list of invoice ids."""
            if value is not None:
                return ",".join(map(str, value))
            return value

    async def get_invoices(
        self: "cryptopay.CryptoPay",
        asset: Asset | None = None,
        fiat: Fiat | None = None,
        invoice_ids: list[int] | None = None,
        status: InvoiceStatus | None = None,
        offset: int | None = None,
        count: int | None = None,
    ) -> list[Invoice]:
        """
        getInvoices method.

        Use this method to get invoices created by your app.
        On success, returns array of :class:`Invoice`.

        Source: https://help.crypt.bot/crypto-pay-api#getInvoices

        :param asset: *Optional*. Cryptocurrency alphabetic code.
        :param fiat: *Optional*. Fiat currency code.
        :param invoice_ids: *Optional*. List of invoice IDs separated by comma.
        :param status: *Optional*. Status of invoices to be returned. Available statuses: “active” and “paid”.
        :param offset: *Optional*. Offset needed to return a specific subset of invoices. Defaults to 0.
        :param count: *Optional*. Number of invoices to be returned. Values between 1-1000 are accepted. Defaults to 100.
        :return: List of :class:`Invoice` objects.
        """
        return await self(self.GetInvoicesMethod(**locals()))
