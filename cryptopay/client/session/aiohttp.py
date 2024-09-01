from typing import TYPE_CHECKING, cast

from aiohttp import ClientSession
from aiohttp.http import SERVER_SOFTWARE

from cryptopay.__meta__ import __version__

from .base import BaseSession

if TYPE_CHECKING:
    import cryptopay
    from cryptopay.client import APIServer
    from cryptopay.methods import CryptoPayMethod
    from cryptopay.types import CryptoPayType


class AiohttpSession(BaseSession):
    """
    Http session based on aiohttp.

    This class is a wrapper of `aiohttp.ClientSession`.
    """

    def __init__(self, api_server: "APIServer") -> None:
        super().__init__(api_server)
        self._session: ClientSession | None = None

    async def request(
        self,
        token: str,
        client: "cryptopay.CryptoPay",
        method: "CryptoPayMethod[CryptoPayType]",
    ) -> "CryptoPayType":
        """Make http request."""
        if self._session is None or self._session.closed:
            self._session = ClientSession()
        async with self._session as session:
            resp = await session.post(
                url=self.api_server.url(method),
                data=method.model_dump_json(exclude_none=True),
                headers={
                    "Crypto-Pay-API-Token": token,
                    "Content-Type": "application/json",
                    "User-Agent": f"{SERVER_SOFTWARE} aiocpb/{__version__}",
                },
            )
            response = self._check_response(client, method, await resp.text())
        return cast("CryptoPayType", response.result)

    async def close(self) -> None:
        """Close http session."""
        if self._session is not None and not self._session.closed:
            await self._session.close()

    def __del__(self) -> None:
        """Close session connector."""
        if (
            self._session is not None
            and not self._session.closed
            and self._session.connector is not None
            and self._session.connector_owner
        ):
            self._session.connector.close()
