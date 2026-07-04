from typing import TYPE_CHECKING

from aiosend.webhook.starlette_manager import StarletteManager

if TYPE_CHECKING:
    from fastapi import FastAPI


class FastAPIManager(StarletteManager):
    """
    FastAPI webhook manager.

    Webhook manager based on :class:`fastapi.FastAPI` (kinda lie here for now)
    """

    def __init__(
        self,
        app: "FastAPI",
        path: str,
    ) -> None:
        super().__init__(app, path)
