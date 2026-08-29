import asyncio
from typing import Annotated
import uvicorn
from fastapi import Depends, FastAPI, Request
from aiosend import CryptoPay
from aiosend.types import Invoice
from aiosend.webhook import FastAPIManager

app = FastAPI(title="My App")
cp = CryptoPay("TOKEN", webhook_manager=FastAPIManager(app, "/handler"))

async def get_app_name(request: Request) -> str:
    return request.app.title

@cp.invoice_paid()
async def handler(
    invoice: Invoice,
    app_name: Annotated[str, Depends(get_app_name)],
) -> None:
    print(f"Received {invoice.amount} {invoice.asset} in {app_name}")

async def main() -> None:
    invoice = await cp.create_invoice(1, "USDT")
    print("invoice link:", invoice.bot_invoice_url)

if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app)