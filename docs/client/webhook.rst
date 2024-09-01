=======
Webhook
=======

.. tip::
    To use webhooks you need to enable them in the `@CryptoBot <https://send.t.me>`_ settings as follows:

    🏝 Crypto Pay -> My Apps -> YOUR APP -> Webhooks -> 🌕 Enable webhooks.

.. automethod:: cryptopay.CryptoPay.webhook_handler

Usage example
-------------
.. literalinclude:: ../../examples/webhook.py

**aiocpa** uses `aiohttp <https://docs.aiohttp.org/en/stable/index.html>`_ as web server by default.
You can implement your own webhook manager by inheriting :class:`cryptopay.webhook.WebhookManager`
and overriding :attr:`cryptopay.webhook.WebhookManager.register_handler`.

.. autoclass:: cryptopay.webhook.WebhookManager
    :members:

.. autoclass:: cryptopay.webhook.AiohttpManager
    :show-inheritance:
    :members: