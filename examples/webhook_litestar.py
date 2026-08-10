import asyncio
import uvicorn
from litestar import Litestar
from aiosend import CryptoPay
from aiosend.types import Invoice
from aiosend.webhook import LitestarManager

app = Litestar()
cp = CryptoPay(
    "TOKEN",
    webhook_manager=LitestarManager(app, "/handler"),
)

@cp.invoice_paid()
async def handler(invoice: Invoice) -> None:
    print(f"Received {invoice.amount} {invoice.asset}")

async def main() -> None:
    invoice = await cp.create_invoice(1, "USDT")
    print("invoice link:", invoice.bot_invoice_url)

if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app)