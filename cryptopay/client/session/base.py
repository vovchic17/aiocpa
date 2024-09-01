from abc import ABC, abstractmethod
from types import TracebackType
from typing import TYPE_CHECKING, cast

from pydantic import ValidationError

from cryptopay.exceptions import APIError, DeserializationError
from cryptopay.methods import (
    CryptoPayMethod,
)
from cryptopay.types import (
    CryptoPayType,
    ItemsList,
    Response,
)

if TYPE_CHECKING:
    import cryptopay
    from cryptopay.client import APIServer
    from cryptopay.types import Error


class BaseSession(ABC):
    """
    Abstract session class.

    If you want to implement your own session class,
    you should inherit this class.
    """

    def __init__(self, api_server: "APIServer") -> None:
        self.api_server = api_server

    @abstractmethod
    async def request(
        self,
        token: str,
        client: "cryptopay.CryptoPay",
        method: "CryptoPayMethod[CryptoPayType]",
    ) -> "CryptoPayType":
        """Make http request."""

    @abstractmethod
    async def close(self) -> None:
        """Close http session."""

    def _check_response(
        self,
        client: "cryptopay.CryptoPay",
        method: CryptoPayMethod[CryptoPayType],
        content: str,
    ) -> Response[CryptoPayType]:
        try:
            response = Response[method.__return_type__].model_validate_json(  # type: ignore[name-defined]
                content,
                context={"client": client},
            )
        except ValidationError as e:
            raise DeserializationError(
                method,
                "Failed to deserialize object",
            ) from e

        if not response.ok:
            error = cast("Error", response.error)
            raise APIError(method, error)
        if isinstance(response.result, ItemsList):
            response.result = response.result.items
        return response

    async def __aenter__(self) -> "BaseSession":
        """Enter async context manager."""
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit async context manager."""
        await self.close()
