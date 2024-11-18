from enum import Enum


class Asset(str, Enum):
    """Cryptocurrency alphabetic code."""

    USDT = "USDT"
    TON = "TON"
    BTC = "BTC"
    LTC = "LTC"
    ETH = "ETH"
    BNB = "BNB"
    TRX = "TRX"
    USDC = "USDC"
    JET = "JET"
    SEND = "SEND"
