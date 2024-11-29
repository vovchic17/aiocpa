import asyncio

from fastapi import FastAPI
import uvicorn

from aiocpa import CryptoPay
from aiocpa.webhook import FastAPIManager
from aiocpa.types import Invoice

cp = CryptoPay("TOKEN", manager=FastAPIManager())
app = FastAPI()


@cp.webhook_handler(app, "/handler")
async def handler(invoice: Invoice) -> None:
    print(f"Received {invoice.amount} {invoice.asset}")


async def main() -> None:
    invoice = await cp.create_invoice(1, "USDT")
    print("invoice link:", invoice.bot_invoice_url)


if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app)
