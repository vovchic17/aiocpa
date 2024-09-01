from abc import ABC
from typing import ClassVar, Generic

from pydantic import BaseModel, ConfigDict

from cryptopay.types import CryptoPayType


class CryptoPayMethod(BaseModel, Generic[CryptoPayType], ABC):
    """Base `Crypto Pay API` method class."""

    model_config = ConfigDict(
        extra="ignore",
        frozen=True,
    )

    __return_type__: ClassVar[type[CryptoPayType]]
    __method__: ClassVar[str]
