=======
Session
=======

.. automodule:: cryptopay.client.session
    :show-inheritance:
    :members:

**aiocpa** uses `aiohttp <https://docs.aiohttp.org/en/stable/index.html>`_ session by default.
You can implement your own session by inheriting :class:`cryptopay.client.session.BaseSession`
and overriding :attr:`cryptopay.client.session.BaseSession.request` and :attr:`cryptopay.client.session.BaseSession.close` methods.