from typing import TYPE_CHECKING

from cryptopay.enums import Asset
from cryptopay.types import Check

from .base import CryptoPayMethod

if TYPE_CHECKING:
    import cryptopay


class CreateCheck:
    """createCheck method."""

    class CreateCheckMethod(CryptoPayMethod[Check]):
        __return_type__ = Check
        __method__ = "createCheck"

        asset: Asset
        amount: float
        pin_to_user_id: int | None
        pin_to_username: str | None

    async def create_check(
        self: "cryptopay.CryptoPay",
        amount: float,
        asset: Asset | str,
        pin_to_user_id: int | None = None,
        pin_to_username: str | None = None,
    ) -> Check:
        """
        createCheck method.

        Use this method to create a new check.
        On success, returns an object of the created :class:`Check`.

        Source: https://help.crypt.bot/crypto-pay-api#createCheck

        :param amount: Amount of the check in float.
        :param asset: Cryptocurrency alphabetic code.
        :param pin_to_user_id: ID of the user who will be able to activate the check, defaults to None
        :param pin_to_username: A user with the specified username will be able to activate the check, defaults to None
        :return: :class:`cryptopay.types.Check` object
        """
        return await self(self.CreateCheckMethod(**locals()))
