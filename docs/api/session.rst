=======
Session
=======

.. automodule:: cryptopay.client.session
    :show-inheritance:
    :members:

**aiocpa** uses `aiohttp <https://docs.aiohttp.org/en/stable/index.html>`_ session by default.
You can implement your own session by inheriting :class:`BaseSession <cryptopay.client.session.BaseSession>`
and overriding :attr:`request <cryptopay.client.session.BaseSession.request>`
and :attr:`close <cryptopay.client.session.BaseSession.close>` methods.