from enum import Enum


class CurrencyType(str, Enum):
    """Type of currency."""

    CRYPTO = "crypto"
    FIAT = "fiat"
