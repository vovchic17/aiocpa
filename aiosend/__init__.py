"""
       .@@. .*.
     .@@@++@@@@@.                 .                                       ..
   .#@@++@@@@@@@@@.              #@                                       @@
 .#@@++@@@@@@@@@@@@      .@@@+.  **   *@@@.  .@@@@   *@@@.   .*@+.   .*@@*@@
*@@++++#@@@@@@@@@@%     @@   @@. #@ .@@  #@% @@    .@%  #@% @@@ #@+ @@@  #@@
 -+++++++@@@@@@@@       @@    @@ #@ #@    @@  =@@@ #@@@@@@@ @@   @@ @@    @@
   ++++++++@@@@         @@@.-@@@ #@  @@..@@% .+  @% @@   _  @@   @@ #@@..@@%
     +++++++@             #== == ==    ==%    #==    %==%   =%   ==   #==%
       ++++

aiosend is a synchronous & asynchronous Crypto Pay API client.

It provides a fully typed interface for working with the Crypto Pay API,
along with event routing, polling, webhook handling, filters, dependency
injection, and convenient utilities for building Crypto Pay integrations.
"""

from aiosend._events import PayloadData
from aiosend._utils.sync import CryptoPay
from aiosend.client import MAINNET, TESTNET
from aiosend.polling import PollingRouter
from aiosend.webhook import WebhookRouter

from .__meta__ import __api_version__, __version__

__all__ = (
    "MAINNET",
    "TESTNET",
    "CryptoPay",
    "PayloadData",
    "PollingRouter",
    "WebhookRouter",
    "__api_version__",
    "__version__",
)
