from typing import TYPE_CHECKING

from aiocpa.enums import InvoiceStatus

if TYPE_CHECKING:
    import aiocpa


class DeleteAllInvoices:
    """Delete all invoices."""

    async def delete_all_invoices(
        self: "aiocpa.CryptoPay",
    ) -> None:
        """
        Delete all invoices.

        Wrapper for :class:`cryptopay.CryptoPay.get_invoices`
        and :class:`cryptopay.CryptoPay.delete_invoice`

        Use this method to delete all existing
        invoices created by your app.

        :return:
        """
        invoices = await self.get_invoices(status=InvoiceStatus.ACTIVE)
        for invoice in invoices:
            await invoice.delete()
