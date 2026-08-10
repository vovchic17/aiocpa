from http import HTTPStatus
from typing import TYPE_CHECKING

from aiosend.webhook.base import _APP, WebhookManager

if TYPE_CHECKING:
    from litestar import Litestar, Router  # noqa: F401

    from aiosend.webhook.base import WebServerHandler


class LitestarManager(
    WebhookManager["Litestar | Router"],
):
    """
    Litestar webhook manager.

    ```
    Webhook manager based on `Litestar <https://litestar.dev/>`_.
    ```
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
            from litestar import post  # noqa: PLC0415
            from litestar.exceptions import (  # noqa: PLC0415
                InternalServerException,
            )
        except ModuleNotFoundError as e:
            msg = "Litestar is not installed"
            raise RuntimeError(msg) from e

        @post(
            path=self._path,
            status_code=HTTPStatus.OK,
        )
        async def handle(
            body: bytes,
            headers: dict[str, str],
        ) -> dict[str, bool]:
            status = await feed_update(
                body,
                headers,
            )

            resp = {"ok": status}

            if not status:
                raise InternalServerException(
                    detail=str(resp),
                )

            return resp

        self._app.register(handle)
