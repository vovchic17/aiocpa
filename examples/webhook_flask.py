import asyncio

from flask import Flask

from cryptopay import CryptoPay
from cryptopay.webhook import FlaskManager
from cryptopay.types import Invoice

cp = CryptoPay("TOKEN", manager=FlaskManager())
app = Flask(__name__)


@cp.webhook_handler(app, "/handler")
async def handler(invoice: Invoice) -> None:
    print(f"Received {invoice.amount} {invoice.asset}")


async def main() -> None:
    invoice = await cp.create_invoice(1, "USDT")
    print("invoice link:", invoice.bot_invoice_url)


if __name__ == "__main__":
    asyncio.run(main())
    app.run(app)
