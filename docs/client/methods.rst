=======
Methods
=======

`Crypto Pay API <https://help.crypt.bot/crypto-pay-api>`_ methods implementation.

.. automethod:: aiocpa.CryptoPay.get_me
.. automethod:: aiocpa.CryptoPay.create_invoice
.. automethod:: aiocpa.CryptoPay.delete_invoice
.. tip::
    To use /create_check method you need to enable it to the restriction settings in `@CryptoBot <https://send.t.me>`_ as follows:

    🏝 Crypto Pay -> My Apps -> YOUR APP -> Security -> Checks -> Enable.
.. automethod:: aiocpa.CryptoPay.create_check
.. automethod:: aiocpa.CryptoPay.delete_check
.. tip::
    To use /transfer method you need to enable it to the restriction settings in `@CryptoBot <https://send.t.me>`_ as follows:

    🏝 Crypto Pay -> My Apps -> YOUR APP -> Security -> Transfers -> Enable.
.. automethod:: aiocpa.CryptoPay.transfer
.. automethod:: aiocpa.CryptoPay.get_invoices
.. automethod:: aiocpa.CryptoPay.get_checks
.. automethod:: aiocpa.CryptoPay.get_transfers
.. automethod:: aiocpa.CryptoPay.get_balance
.. automethod:: aiocpa.CryptoPay.get_exchange_rates
.. automethod:: aiocpa.CryptoPay.get_currencies
.. automethod:: aiocpa.CryptoPay.get_stats