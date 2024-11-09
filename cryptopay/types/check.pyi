from datetime import datetime

from cryptopay.client.client import bool
from cryptopay.enums import Asset, CheckStatus

from .base import CryptoPayObject

class Check(CryptoPayObject):
    check_id: int
    hash: str
    asset: Asset | str
    amount: float
    bot_check_url: str
    status: CheckStatus | str
    created_at: datetime
    activated_at: datetime | None = None

    def delete(self) -> bool: ...
