from typing import TYPE_CHECKING

from aiosend.webhook.base import _APP, WebhookManager

if TYPE_CHECKING:
    from fastapi import APIRouter, FastAPI  # noqa: F401
    from fastapi.params import Depends
    from starlette.applications import Starlette  # noqa: F401
    from starlette.routing import Router  # noqa: F401

    from aiosend.webhook.base import WebServerHandler


class StarletteManager(
    WebhookManager["FastAPI | APIRouter | Starlette | Router"],
):
    """
    Starlette & FastAPI webhook manager.

    Webhook manager based on `Starlette <https://www.starlette.io/applications/>`_
    and `FastAPI <https://fastapi.tiangolo.com/reference/fastapi/>`_.
    """

    def __init__(
        self,
        app: _APP,
        path: str,
        dependencies: list["Depends"] | None = None,
    ) -> None:
        self._dependencies = dependencies or []
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
                raise HTTPException(status_code=500, detail=str(resp))

            return JSONResponse(resp)

        try:
            from fastapi import APIRouter, FastAPI  # noqa: PLC0415
        except ModuleNotFoundError:
            self._dependencies = []
        else:
            if isinstance(self._app, APIRouter | FastAPI):
                self._app.add_api_route(
                    self._path,
                    handle,
                    methods=["POST"],
                    dependencies=self._dependencies,
                )
                return

            self._dependencies = []

        self._app.add_route(
            self._path,
            handle,
            methods=["POST"],
        )


FastAPIManager = StarletteManager
