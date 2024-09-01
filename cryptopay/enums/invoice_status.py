from enum import StrEnum


class InvoiceStatus(StrEnum):
    """Status of invoice."""

    ACTIVE = "active"
    PAID = "paid"
    EXPIRED = "expired"
