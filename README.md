# aiocpa

[![Python](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/vovchic17/static/main/src/badges/python310_313.json)](https://www.python.org/)
[![Crypto Pay API](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/vovchic17/static/refs/heads/main/src/badges/cryptopayapi.json)](https://help.crypt.bot/crypto-pay-api)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
[![Aiohttp](https://img.shields.io/badge/aiohttp-v3-2c5bb4?logo=aiohttp)](https://docs.aiohttp.org/en/stable/)
[![Code linter: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/charliermarsh/ruff)
[![Checked with mypy](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/vovchic17/static/main/src/badges/mypy.json)](https://mypy-lang.org/)

**aiocpa** is a syncronous & asynchronous [Crypto Pay API](https://help.crypt.bot/crypto-pay-api) client.

> [!NOTE]
> ## [Official documentation](https://aiocpa.readthedocs.io/en/latest/)

## Quick start
```python
import asyncio
from cryptopay import CryptoPay


async def main():
    cp = CryptoPay(token="TOKEN")
    app = await cp.get_me()
    print(app.name)  # Your App Name


if __name__ == "__main__":
    asyncio.run(main())
```

## aiogram 3.x integration example

```python
import asyncio
from aiogram import Bot, Dispatcher
from cryptopay import CryptoPay

cp = CryptoPay("TOKEN")
bot = Bot("TOKEN")
dp = Dispatcher()


@dp.message()
async def get_invoice(message):
    invoice = await cp.create_invoice(1, "USDT")
    await message.answer(f"pay: {invoice.bot_invoice_url}")
    invoice.await_payment(message=message)


@cp.polling_handler()
async def handle_payment(invoice, message):
    await message.answer(f"invoice #{invoice.invoice_id} has been paid")


async def main():
    await asyncio.gather(
        dp.start_polling(bot),
        cp.run_polling(),
    )


if __name__ == "__main__":
    asyncio.run(main())
```