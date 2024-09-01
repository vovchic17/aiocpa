from typing import TypeVar

T = TypeVar("T")


def serialize_list(value: list[T] | None) -> str | None:
    """
    List of objects serialization.

    Serialize a list of objects into a
    string of objects separated by commas.
    """
    if value is not None:
        return ",".join(map(str, value))
    return value
