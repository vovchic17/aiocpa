from typing import TYPE_CHECKING

from fastapi import Request

from .base import WebhookManager

if TYPE_CHECKING:
    from fastapi import FastAPI

    from .base import Handler


class FastAPIManager(WebhookManager["FastAPI"]):
    """
    aiohttp webhook manager.

    Webhook manager based on :class:`fastapi.FastAPI`.
    """

    def register_handler(
        self,
        app: "FastAPI",
        path: str,
        handler: "Handler",
    ) -> None:
        """Register webhook handler."""

        @app.post(path)
        async def handle(request: Request) -> dict:
            await handler(
                await request.json(),
                request.headers,
            )
            return {"ok": True}
