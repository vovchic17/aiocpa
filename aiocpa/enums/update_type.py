from enum import Enum


class UpdateType(str, Enum):
    """Webhook update type."""

    INVOICE_PAID = "invoice_paid"
