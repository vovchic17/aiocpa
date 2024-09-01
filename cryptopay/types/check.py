from datetime import datetime

from cryptopay.enums import Asset, CheckStatus

from .base import CryptoPayObject


class Check(CryptoPayObject):
    """
    Check object.

    Source: https://help.crypt.bot/crypto-pay-api#Check
    """

    check_id: int
    """Unique ID for this check."""
    hash: str
    """Hash of the check."""
    asset: Asset | str
    """Cryptocurrency alphabetic code. Currently, can be “USDT”, “TON”, “BTC”, “ETH”, “LTC”, “BNB”, “TRX” and “USDC” (and “JET” for testnet)."""
    amount: float
    """Amount of the check in float."""
    bot_check_url: str
    """URL should be provided to the user to activate the check."""
    status: CheckStatus | str
    """Status of the check, can be “active” or “activated”."""
    created_at: datetime
    """Date the check was created in ISO 8601 format."""
    activated_at: datetime | None = None
    """Date the check was activated in ISO 8601 format."""

    async def delete(self) -> bool:
        """
        Shortcut for method :class:`cryptopay.CryptoPay.delete_check`.

        Use this method to delete check created by your app.
        Returns :code:`True` on success.

        Source: https://help.crypt.bot/crypto-pay-api#deleteCheck

        :return: :code:`True` on success.
        """
        return await self._client.delete_check(self.check_id)
