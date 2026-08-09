from http import HTTPStatus
from typing import TYPE_CHECKING

from aiosend.webhook.base import _APP, WebhookManager

if TYPE_CHECKING:
    from starlette.applications import Starlette  # noqa: F401
    from starlette.routing import Router  # noqa: F401

    from aiosend.webhook.base import WebServerHandler


class StarletteManager(
    WebhookManager["Starlette | Router"],
):
    """
    Starlette webhook manager.

    Webhook manager based on `Starlette <https://www.starlette.io/applications/>`_.
    """

    def __init__(
        self,
        app: _APP,
        path: str,
    ) -> None:
        super().__init__(app, path)

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
            msg = "Starlette is not installed"
            raise RuntimeError(msg) from e

        async def handle(request: Request) -> JSONResponse:
            status = await feed_update(
                (await request.body()).decode(),
                dict(request.headers),
            )

            resp = {"ok": status}

            if not status:
                raise HTTPException(
                    status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                    detail=str(resp),
                )

            return JSONResponse(resp)

        self._app.add_route(
            self._path,
            handle,
            methods=["POST"],
        )
