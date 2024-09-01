import asyncio

from cryptopay import CryptoPay
from cryptopay.polling import PollingConfig
from cryptopay.types import Invoice

cp = CryptoPay(
    "TOKEN",
    polling_config=PollingConfig(
        timeout=600,  # 10 minutes
        delay=3,  # request every 3 seconds
    ),
)


@cp.polling_handler()
async def handler(invoice: Invoice):
    print(f"Received", invoice.amount, invoice.asset)


async def main() -> None:
    invoice = await cp.create_invoice(1, "USDT")
    print("invoice link:", invoice.bot_invoice_url)
    invoice.await_payment()
    await cp.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
