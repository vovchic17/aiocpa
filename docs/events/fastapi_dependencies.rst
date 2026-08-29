====================
FastAPI dependencies
====================

When using :class:`aiosend.webhook.FastAPIManager`, you can use
`FastAPI dependencies <https://fastapi.tiangolo.com/tutorial/dependencies/>`_
directly inside aiosend event handlers.

This allows you to reuse the same dependencies from your FastAPI application,
for example database sessions, services, authentication data or request context.

.. tip::
    To use aiosend with FastAPI, install the ``fastapi`` extra:

.. code-block:: bash
    
    pip install aiosend[fastapi]

Usage example
-------------

.. literalinclude:: ../../examples/fastapi_dependency.py

How it works
-------------

When a webhook update is received, :class:`aiosend.webhook.FastAPIManager`
uses FastAPI's dependency injection system to resolve dependencies declared
in the matched aiosend event handler.

The event object itself, such as :class:`aiosend.types.Invoice`, is provided
by aiosend:

.. code-block:: python

    async def get_service() -> Service:
        return Service()


    @cp.invoice_paid()
    async def handler(
        invoice: Invoice,
        service: Annotated[Service, Depends(get_service)],
    ) -> None:
        await service.process(invoice)

Webhook route dependencies
--------------------------

:class:`aiosend.webhook.FastAPIManager` also accepts FastAPI dependencies
that should be executed for the webhook route itself:

.. code-block:: python

    async def verify_webhook() -> None:
        ...


    cp = CryptoPay(
        "TOKEN",
        webhook_manager=FastAPIManager(
            app,
            "/handler",
            dependencies=[
                Depends(verify_webhook),
            ],
        ),
    )

Nested dependencies
-------------------

Dependencies can depend on other FastAPI dependencies as usual:

.. code-block:: python

    async def get_database() -> Database:
        return Database()


    async def get_service(
        database: Annotated[Database, Depends(get_database)],
    ) -> Service:
        return Service(database)


    @cp.invoice_paid()
    async def handler(
        invoice: Invoice,
        service: Annotated[Service, Depends(get_service)],
    ) -> None:
        await service.process(invoice)