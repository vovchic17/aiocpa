import asyncio
from aiogram import Dispatcher, Bot

from cryptopay.client.client import CryptoPay


async def main() -> None:
    cp = CryptoPay("TOKEN")
    bot = Bot(token="TOKEN")
    dp = Dispatcher()

    await asyncio.gather(dp.start_polling(bot))
