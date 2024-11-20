import asyncio

from telegram import Message, Update
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)

from cryptopay import CryptoPay
from cryptopay.types import Invoice

cp = CryptoPay("TOKEN")
app = Application.builder().token("TOKEN").build()


async def get_invoice(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    invoice = await cp.create_invoice(1, "USDT")
    await update.message.reply_text(f"pay: {invoice.mini_app_invoice_url}")
    invoice.await_payment(message=update.message)


@cp.polling_handler()
async def handle_payment(
    invoice: Invoice,
    message: Message,
) -> None:
    await message.reply_text(
        f"payment received: {invoice.amount} {invoice.asset}",
    )


async def main() -> None:
    app.add_handler(MessageHandler(filters.TEXT, get_invoice))
    await app.initialize()
    await app.start()
    await asyncio.gather(
        app.updater.start_polling(allowed_updates=Update.ALL_TYPES),
        cp.run_polling(),
    )


if __name__ == "__main__":
    asyncio.run(main())
