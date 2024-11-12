import asyncio

from cryptopay import CryptoPay
from cryptopay.types import Invoice

cp = CryptoPay("TOKEN")


@cp.polling_handler()
async def payment_handler(invoice: Invoice, payload: str):
    print(f"Received", invoice.amount, invoice.asset.value, payload)


@cp.expired_handler()
async def expired_invoice_handler(invoice: Invoice, payload: str):
    print(f"Expired invoice", invoice.invoice_id, payload)


async def main() -> None:
    invoice = await cp.create_invoice(1, "USDT")
    print("invoice link:", invoice.bot_invoice_url)
    invoice.await_payment(payload="payload")
    await cp.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
