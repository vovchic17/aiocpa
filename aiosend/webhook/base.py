import hashlib
import re
from abc import ABC, abstractmethod
from hmac import HMAC, compare_digest
from typing import TYPE_CHECKING, Any, Concatenate, Generic, ParamSpec, TypeVar

from aiosend import loggers
from aiosend.types import Update

from .router import WebhookRouter

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable, Mapping

    P = ParamSpec("P")

    FastAPIResolver = Callable[
        [Callable[..., Any]],
        Awaitable[dict[str, Any]],
    ]

    WebServerHandler = Callable[
        Concatenate[bytes, Mapping[str, str], P],
        Awaitable[bool],
    ]

_APP = TypeVar("_APP", bound=Any)


class WebhookManager(ABC, Generic[_APP]):
    """
    Webhook manager.

    If you want to implement your own webhook
    manager, you must inherit from this class.
    """

    def __init__(self, app: _APP, path: str) -> None:
        self._app = app
        self._path = path

    @abstractmethod
    def register_handler(
        self,
        feed_update: "WebServerHandler",
    ) -> None:
        """
        Register webhook handler.

        Override this method in your own webhook manager class.
        This method is used for registering webhook handler in your app.

        :param feed_update: Web server handler object.
        :return:
        """


class WebhookHandler(WebhookRouter):
    """Updates handler."""

    _token: str
    _kwargs: dict[str, "Any"]

    def __init__(
        self,
        manager: WebhookManager[_APP] | None,
    ) -> None:
        if manager is not None:
            manager.register_handler(self.feed_update)
        self._webhook_manager = manager

    def _check_signature(
        self,
        body: bytes,
        headers: "Mapping[str, str]",
    ) -> bool:
        """
        Verify the received update and the integrity of the received data.

        Source: https://help.send.tg/en/articles/10279948-crypto-pay-api#h_f0180ed474

        :param body: raw request body.
        :param headers: request headers.
        :return: True if the signature is correct, False otherwise.
        """
        secret = hashlib.sha256(self._token.encode()).digest()
        hmac = HMAC(secret, body, hashlib.sha256).hexdigest()
        signature = headers.get(
            "Crypto-Pay-Api-Signature",
        ) or headers.get(
            "crypto-pay-api-signature",
        )
        if signature is None:
            return False
        return compare_digest(hmac, signature)

    @staticmethod
    def _extract_update_id(body: bytes) -> int:
        mtch = re.match(rb'"update_id"\s*:\s*(\d+)', body)

        if mtch is None:
            msg = "Can't extract update_id from request body"
            raise ValueError(msg)

        return int(mtch.group(1))

    async def feed_update(
        self,
        body: bytes,
        headers: "Mapping[str, str]",
        fastapi_resolver: "FastAPIResolver | None" = None,
        **kwargs: object,
    ) -> bool:
        """
        Feed an update to the invoice handler.

        :param body: raw request body.
        :param headers: request headers.
        :param fastapi_resolver: FastAPI dependency resolver.

        :return: :code:`True` on success.
        """
        try:
            if not self._check_signature(body, headers):
                try:
                    update_id = self._extract_update_id(body)
                    loggers.webhook.warning(
                        "Webhook Update id=%d is not handled. "
                        "Signature is invalid.",
                        update_id,
                    )
                except ValueError as e:
                    loggers.webhook.warning(
                        "Webhook Update is not handled. "
                        "Signature is invalid. %s",
                        e,
                    )
                return False
            update = Update.model_validate_json(body, context={"client": self})
            if await self.propagate_event(
                update.payload,
                update.update_type,
                fastapi_resolver=fastapi_resolver,
                **self._kwargs | kwargs,
            ):
                loggers.webhook.info(
                    "Webhook Update id=%d is handled.",
                    update.update_id,
                )
            else:
                loggers.webhook.info(
                    "Webhook Update id=%d is not handled. "
                    "No suitable handlers.",
                    update.update_id,
                )
        except Exception:  # noqa: BLE001
            loggers.webhook.exception("Error while handling update:\n")
            return False
        return True
