=======
Polling
=======

Polling is a method of receiving updates by periodically sending requests.
Once :attr:`invoice status <aiocpa.types.Invoice.status>` is changed to
:attr:`PAID <aiocpa.enums.InvoiceStatus.PAID>`,
:attr:`polling manager <aiocpa.polling.PollingManager>` will call the
:attr:`polling_handler <aiocpa.CryptoPay.polling_handler>`.
Polling uses the :attr:`/getInvoices <aiocpa.CryptoPay.get_invoices>` method.

.. attention::
    :attr:`Polling manager <aiocpa.polling.PollingManager>` has
    :attr:`configuration <aiocpa.polling.PollingConfig>`
    that defines the :attr:`delay <aiocpa.polling.PollingConfig.delay>` (between requests)
    and :attr:`timeout <aiocpa.polling.PollingConfig.timeout>`
    for each invoice in the awaiting queue.
    After the timeout polling manager will stop polling that invoice
    and call the :attr:`expired_handler <aiocpa.CryptoPay.expired_handler>`
    if it is declared.

    **Default is 2 seconds delay and 300 seconds (5 min) timeout**.

    :ref:`You can change the polling configuration. <PC>`

.. automethod:: aiocpa.CryptoPay.polling_handler
.. automethod:: aiocpa.CryptoPay.expired_handler

Usage example
-------------
.. literalinclude:: ../../examples/polling.py

.. autoclass:: aiocpa.polling.PollingConfig
    :members:

.. _PC:

Polling configuration
---------------------
You can configure your own polling configuration.

.. literalinclude:: ../../examples/polling_config.py

.. autoclass:: aiocpa.polling.PollingManager
    :members: