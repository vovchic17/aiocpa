from typing import TYPE_CHECKING

from cryptopay.client import MAINNET
from cryptopay.methods import Methods
from cryptopay.polling import PollingConfig, PollingManager
from cryptopay.tools import Tools
from cryptopay.webhook import AiohttpManager, RequestHandler

from .session import AiohttpSession

if TYPE_CHECKING:
    from cryptopay.client import APIServer
    from cryptopay.methods import CryptoPayMethod
    from cryptopay.types import CryptoPayType
    from cryptopay.webhook import _APP, WebhookManager

    from .session import BaseSession


class CryptoPay(Methods, Tools, RequestHandler, PollingManager):
    """
    Client class providing API methods.

    :param token: Crypto Bot API token
    :param session: HTTP Session
    :param api_server: Crypto Bot API server
    """

    def __init__(
        self,
        token: str,
        api_server: "APIServer" = MAINNET,
        session: "type[BaseSession]" = AiohttpSession,
        manager: "WebhookManager[_APP] | None" = None,
        polling_config: "PollingConfig | None" = None,
    ) -> None:
        self._token = token
        self._session = session(api_server)
        RequestHandler.__init__(self, manager or AiohttpManager())
        PollingManager.__init__(self, polling_config or PollingConfig())

    async def __call__(
        self,
        method: "CryptoPayMethod[CryptoPayType]",
    ) -> "CryptoPayType":
        """
        Request method.

        Use this method to make an API request.

        :param method: CryptoPayMethod object.
        :return: :class:`CryptoPayType` object.
        """
        return await self._session.request(self._token, self, method)
