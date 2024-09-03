from enum import Enum


class InvoiceStatus(str, Enum):
    """Status of invoice."""

    ACTIVE = "active"
    PAID = "paid"
    EXPIRED = "expired"
