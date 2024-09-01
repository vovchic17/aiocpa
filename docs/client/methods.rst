=======
Methods
=======

`Crypto Pay API <https://help.crypt.bot/crypto-pay-api>`_ methods implementation.

.. automethod:: cryptopay.CryptoPay.get_me
    :async:
.. automethod:: cryptopay.CryptoPay.create_invoice
.. automethod:: cryptopay.CryptoPay.delete_invoice
.. tip::
    To use /create_check method you need to enable it to the restriction settings in `@CryptoBot <https://send.t.me>`_ as follows:

    🏝 Crypto Pay -> My Apps -> YOUR APP -> Security -> Checks -> Enable.
.. automethod:: cryptopay.CryptoPay.create_check
.. automethod:: cryptopay.CryptoPay.delete_check
.. tip::
    To use /transfer method you need to enable it to the restriction settings in `@CryptoBot <https://send.t.me>`_ as follows:

    🏝 Crypto Pay -> My Apps -> YOUR APP -> Security -> Transfers -> Enable.
.. automethod:: cryptopay.CryptoPay.transfer
.. automethod:: cryptopay.CryptoPay.get_invoices
.. automethod:: cryptopay.CryptoPay.get_checks
.. automethod:: cryptopay.CryptoPay.get_transfers
.. automethod:: cryptopay.CryptoPay.get_balance
.. automethod:: cryptopay.CryptoPay.get_exchange_rates
.. automethod:: cryptopay.CryptoPay.get_currencies
.. automethod:: cryptopay.CryptoPay.get_stats