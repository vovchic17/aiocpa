from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cryptopay.methods import CryptoPayMethod


@dataclass(frozen=True)
class APIServer:
    """Configuration for endpoints."""

    name: str
    """Net name"""
    base: str
    """Base URL"""

    def url(self, method: "CryptoPayMethod") -> str:
        """Return URL for method."""
        return self.base.format(method=method.__method__)


MAINNET = APIServer(
    name="MAINNET",
    base="https://pay.crypt.bot/api/{method}",
)
TESTNET = APIServer(
    name="TESTNET",
    base="https://testnet-pay.crypt.bot/api/{method}",
)
