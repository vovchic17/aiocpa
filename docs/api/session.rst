=======
Session
=======

.. automodule:: aiocpa.client.session
    :show-inheritance:
    :members:

**aiocpa** uses `aiohttp <https://docs.aiohttp.org/en/stable/index.html>`_ session by default.
You can implement your own session by inheriting :class:`BaseSession <aiocpa.client.session.BaseSession>`
and overriding :attr:`request <aiocpa.client.session.BaseSession.request>`
and :attr:`close <aiocpa.client.session.BaseSession.close>` methods.