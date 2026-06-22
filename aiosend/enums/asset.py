from enum import Enum
from typing import Literal


class Asset(str, Enum):
    """Cryptocurrency alphabetic code."""

    USDT = "USDT"
    TON = "TON"
    SOL = "SOL"
    BTC = "BTC"
    LTC = "LTC"
    ETH = "ETH"
    BNB = "BNB"
    TRX = "TRX"
    USDC = "USDC"
    JET = "JET"
    SEND = "SEND"
    XAUT = "XAUT"


LiteralAsset = Literal[
    "USDT",
    "TON",
    "SOL",
    "BTC",
    "LTC",
    "ETH",
    "BNB",
    "TRX",
    "USDC",
    "JET",
    "SEND",
    "XAUT",
]
