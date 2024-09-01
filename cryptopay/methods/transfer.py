import secrets
from typing import TYPE_CHECKING

from pydantic import field_validator

from cryptopay.enums import Asset
from cryptopay.types import Transfer as TransferType

from .base import CryptoPayMethod

if TYPE_CHECKING:
    import cryptopay


class Transfer:
    """transfer method."""

    class TransferMethod(CryptoPayMethod[TransferType]):
        __return_type__ = TransferType
        __method__ = "transfer"

        user_id: int
        asset: Asset | str
        amount: float
        spend_id: str | None
        comment: str | None
        disable_send_notification: bool | None

        @field_validator("spend_id", mode="before")
        @classmethod
        def generate_spend_id(cls, v: str | None) -> str:
            """Generate spend_id if not present."""
            if v is None:
                v = secrets.token_hex()
            return v

    async def transfer(
        self: "cryptopay.CryptoPay",
        user_id: int,
        asset: str,
        amount: float,
        spend_id: str | None = None,
        comment: str | None = None,
        disable_send_notification: bool | None = None,
    ) -> TransferType:
        """
        transfer method.

        Use this method to send coins from your app's balance to a user.
        On success, returns completed :class:`Transfer`.
        This method must first be enabled in the security settings of your app.

        Source: https://help.crypt.bot/crypto-pay-api#transfer

        :param user_id: User ID in Telegram. User must have previously used @CryptoBot (@CryptoTestnetBot for testnet).
        :param asset: Cryptocurrency alphabetic code.
        :param amount: Amount of the transfer in float. The minimum and maximum amount limits for each of the supported assets roughly correspond to 1-25000 USD.
        :param spend_id: Random UTF-8 string unique per transfer for idempotent requests. The same spend_id can be accepted only once from your app. Up to 64 symbols.
        :param comment: *Optional*. Comment for the transfer. Users will see this comment in the notification about the transfer. Up to 1024 symbols.
        :param disable_send_notification: *Optional*. Pass true to not send to the user the notification about the transfer. Defaults to false.
        :return: :class:`Transfer` object.
        """
        return await self(self.TransferMethod(**locals()))
