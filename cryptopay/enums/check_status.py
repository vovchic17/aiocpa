from enum import Enum


class CheckStatus(str, Enum):
    """Status of check."""

    ACTIVE = "active"
    ACTIVATED = "activated"
