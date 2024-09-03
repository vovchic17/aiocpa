=======
Polling
=======

Polling is a method of receiving updates by periodically sending requests.
Once :attr:`invoice status <cryptopay.types.Invoice.status>` is changed to
:attr:`PAID <cryptopay.enums.InvoiceStatus.PAID>`,
:attr:`polling manager <cryptopay.polling.PollingManager>` will call the handler.
Polling uses the :attr:`/getInvoices <cryptopay.CryptoPay.get_invoices>` method.

.. attention::
    :attr:`Polling manager <cryptopay.polling.PollingManager>` has
    :attr:`configuration <cryptopay.polling.PollingConfig>`
    that defines the :attr:`delay <cryptopay.polling.PollingConfig.delay>` (between requests)
    and :attr:`timeout <cryptopay.polling.PollingConfig.timeout>`
    for each invoice in the awaiting queue.
    After the timeout polling manager will stop polling that invoice.

    **Default is 2 seconds delay and 300 seconds (5 min) timeout**.

    :ref:`You can change the polling configuration. <PC>`

.. automethod:: cryptopay.CryptoPay.polling_handler

Usage example
-------------
.. literalinclude:: ../../examples/polling.py

.. autoclass:: cryptopay.polling.PollingConfig
    :members:

.. _PC:

Polling configuration
---------------------
You can configure your own polling configuration.

.. literalinclude:: ../../examples/polling_config.py

.. autoclass:: cryptopay.polling.PollingManager
    :members: