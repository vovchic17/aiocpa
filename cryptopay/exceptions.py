from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cryptopay.methods import CryptoPayMethod
    from cryptopay.types import Error


class CryptoPayError(Exception):
    """Base class for exceptions in this module."""


class APIError(CryptoPayError):
    """Exception for API errors."""

    def __init__(
        self,
        method: "CryptoPayMethod",
        error: "Error",
    ) -> None:
        self.method = method
        self.error = error

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return (
            f"[{self.error.code}] /{self.method.__method__}, "
            f"{self.error.name} {self.error.model_extra}"
        )


class DeserializationError(CryptoPayError):
    """Exception for deserialization errors."""

    def __init__(self, method: "CryptoPayMethod", message: str) -> None:
        self.method = method
        self.message = message

    def __str__(self) -> str:
        """Return a string representation of the exception."""
        return f"/{self.method.__method__} {self.message}"


class MethodValuesError(CryptoPayError):
    """Exception raised when method values are invalid."""

    def __init__(self, message: str) -> None:
        self.message = message
