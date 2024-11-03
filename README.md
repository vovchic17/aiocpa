# <p align="center">AsyncIOCryptoPayAPI

[![Python](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/vovchic17/static/main/src/badges/python310_313.json)](https://www.python.org/)
[![Crypto Pay API](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/vovchic17/static/refs/heads/main/src/badges/cryptopayapi.json)](https://help.crypt.bot/crypto-pay-api)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
[![Aiohttp](https://img.shields.io/badge/aiohttp-v3-2c5bb4?logo=aiohttp)](https://docs.aiohttp.org/en/stable/)
[![Code linter: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/charliermarsh/ruff)
[![Checked with mypy](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/vovchic17/static/main/src/badges/mypy.json)](https://mypy-lang.org/)

**aiocpa** is a syncronous & asynchronous [Crypto Pay API](https://help.crypt.bot/crypto-pay-api) client.

## Documentation
* [English](https://aiocpa.readthedocs.io/en/latest/)

## Quick start
```python
import asyncio

from cryptopay import CryptoPay


async def main() -> None:
    cp = CryptoPay(token="TOKEN")

    app = await cp.get_me()

    print(app.name)  # Your App Name


if __name__ == "__main__":
    asyncio.run(main())
```

## Synchronous usage
```python
from cryptopay import CryptoPay

cp = CryptoPay("TOKEN")

app = cp.get_me()

print(app.name)  # Your App Name
```
