from functools import partial
from http import HTTPStatus
from typing import TYPE_CHECKING

from aiosend.webhook.base import _APP, WebhookManager

if TYPE_CHECKING:
    from fastapi import APIRouter, FastAPI  # noqa: F401
    from fastapi.params import Depends

    from aiosend.webhook.base import WebServerHandler


class FastAPIManager(
    WebhookManager["FastAPI | APIRouter"],
):
    """
    FastAPI webhook manager.

    Webhook manager based on `FastAPI <https://fastapi.tiangolo.com/reference/fastapi/>`_.
    """

    def __init__(
        self,
        app: _APP,
        path: str,
        dependencies: list["Depends"] | None = None,
    ) -> None:
        super().__init__(app, path)
        self._dependencies = dependencies

    def register_handler(
        self,
        feed_update: "WebServerHandler",
    ) -> None:
        """Register webhook handler."""
        try:
            from fastapi import HTTPException, Request  # noqa: PLC0415
            from fastapi.responses import JSONResponse  # noqa: PLC0415

            from aiosend._utils.fastapi_dependencies import (  # noqa: PLC0415
                resolve_fastapi_dependencies,
            )
        except ModuleNotFoundError as e:
            msg = "FastAPI is not installed"
            raise RuntimeError(msg) from e

        async def handle(request: Request) -> JSONResponse:

            dependency_resolver = partial(
                resolve_fastapi_dependencies,
                request,
            )

            status = await feed_update(
                (await request.body()).decode(),
                dict(request.headers),
                fastapi_resolver=dependency_resolver,
            )

            resp = {"ok": status}

            if not status:
                raise HTTPException(
                    status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                    detail=str(resp),
                )

            return JSONResponse(resp)

        self._app.add_api_route(
            self._path,
            handle,
            methods=["POST"],
            dependencies=self._dependencies,
        )
