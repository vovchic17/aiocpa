from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cryptopay.methods import CryptoPayMethod


@dataclass(frozen=True)
class APIServer:
    """Configuration for endpoints."""

    base: str
    """Base URL"""

    def url(self, method: "CryptoPayMethod") -> str:
        """Return URL for method."""
        return self.base.format(method=method.__method__)


MAINNET = APIServer(base="https://pay.crypt.bot/api/{method}")
TESTNET = APIServer(base="https://testnet-pay.crypt.bot/api/{method}")
