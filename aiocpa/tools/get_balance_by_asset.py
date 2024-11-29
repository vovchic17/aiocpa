from typing import TYPE_CHECKING

from aiocpa.exceptions import CryptoPayError

if TYPE_CHECKING:
    import aiocpa
    from aiocpa.enums import Asset


class GetBalanceByAsset:
    """Get balance by Asset."""

    async def get_balance_by_asset(
        self: "aiocpa.CryptoPay",
        asset: "Asset | str",
    ) -> float:
        """
        Get the balance of a specific asset.

        Wrapper for :class:`cryptopay.CryptoPay.get_balance`.

        Use this method to get total avaliable
        amount in float of a specific asset.

        :return: :class:`float` on success.
        :raise: :class:`CryptoPayError` if there is no such asset.
        """
        balances = await self.get_balance()
        for balance in balances:
            if balance.currency_code == asset:
                return balance.available
        msg = f"Balance for {asset} not found"
        raise CryptoPayError(msg)
