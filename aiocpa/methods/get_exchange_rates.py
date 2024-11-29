from typing import TYPE_CHECKING

from aiocpa.types import ExchangeRate

from .base import CryptoPayMethod

if TYPE_CHECKING:
    import aiocpa


class GetExchangeRates:
    """getExchangeRates method."""

    class GetExchangeRates(CryptoPayMethod[list[ExchangeRate]]):
        __return_type__ = list[ExchangeRate]
        __method__ = "getExchangeRates"

    async def get_exchange_rates(
        self: "aiocpa.CryptoPay",
    ) -> list[ExchangeRate]:
        """
        getExchangeRates method.

        Use this method to get exchange rates of supported currencies.
        Requires no parameters.
        Returns array of :class:`ExchangeRate`.

        Source: https://help.crypt.bot/crypto-pay-api#getExchangeRates

        :return: List of :class:`ExchangeRate` objects.
        """
        return await self(self.GetExchangeRates(**locals()))
