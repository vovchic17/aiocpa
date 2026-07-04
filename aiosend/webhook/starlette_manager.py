from typing import TYPE_CHECKING

from aiosend.webhook.base import WebhookManager

if TYPE_CHECKING:
    from starlette.applications import Starlette  # noqa: F401
    from starlette.routing import Router  # noqa: F401

    from aiosend.webhook.base import WebServerHandler


class StarletteManager(WebhookManager["Starlette | Router"]):
    """
    Starlette webhook manager.

    Webhook manager based on :class:`fastapi.Starlette`.
    """

    def register_handler(
        self,
        feed_update: "WebServerHandler",
    ) -> None:
        """Register webhook handler."""
        try:
            from starlette.exceptions import HTTPException  # noqa: PLC0415
            from starlette.requests import Request  # noqa: PLC0415
            from starlette.responses import JSONResponse  # noqa: PLC0415
        except ModuleNotFoundError as e:
            msg = "fastapi is not installed"
            raise RuntimeError(msg) from e

        async def handle(request: Request) -> "JSONResponse":
            status = await feed_update(
                (await request.body()).decode(),
                dict(request.headers),
            )
            resp = {"ok": status}
            if not status:
                raise HTTPException(500, str(resp))

            return JSONResponse(resp)

        self._app.add_route(self._path, handle, methods=["POST"])
