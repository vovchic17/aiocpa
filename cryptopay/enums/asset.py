from enum import Enum


class Asset(str, Enum):
    """Cryptocurrency alphabetic code."""

    USDT = "USDT"
    TON = "TON"
    BTC = "BTC"
    ETH = "ETH"
    LTC = "LTC"
    BNB = "BNB"
    TRX = "TRX"
    USDC = "USDC"
    SOL = "SOL"
    JET = "JET"
    DOGS = "DOGS"
    MY = "MY"
    NOT = "NOT"
    GRAM = "GRAM"
