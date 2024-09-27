=======
Webhook
=======

.. tip::
    To use webhooks you need to enable them in the `@CryptoBot <https://send.t.me>`_ settings as follows:

    🏝 Crypto Pay -> My Apps -> YOUR APP -> Webhooks -> 🌕 Enable webhooks.

.. automethod:: cryptopay.CryptoPay.webhook_handler

Usage example with `aiohttp web server <https://docs.aiohttp.org/en/stable/web_quickstart.html>`_
-------------
.. literalinclude:: ../../examples/webhook_aiohttp.py

Usage example with `fastapi web server <https://fastapi.tiangolo.com/tutorial/first-steps/>`_
-------------
.. literalinclude:: ../../examples/webhook_fastapi.py

**aiocpa** uses `aiohttp <https://docs.aiohttp.org/en/stable/index.html>`_ as web server by default.
You can implement your own webhook manager by inheriting :class:`cryptopay.webhook.WebhookManager`
and overriding :attr:`cryptopay.webhook.WebhookManager.register_handler`.

.. autoclass:: cryptopay.webhook.WebhookManager
    :members:

.. autoclass:: cryptopay.webhook.AiohttpManager
    :show-inheritance:
    :members:

.. autoclass:: cryptopay.webhook.FastAPIManager
    :show-inheritance:
    :members: