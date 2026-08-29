import asyncio
import warnings
from typing import TYPE_CHECKING

from aiosend import loggers

from .base import PollingConfig
from .check import CheckPollingManager
from .invoice import InvoicePollingManager

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any

    from aiosend._typing import ClientWebhookManagerProtocol


class PollingManager(InvoicePollingManager, CheckPollingManager):
    """
    Polling manager class.

    This class is used to handle payments
    and check activation via polling method.
    """

    def __init__(
        self,
        config: PollingConfig,
    ) -> None:
        InvoicePollingManager.__init__(self)
        CheckPollingManager.__init__(self)

        self._timeout = config.timeout
        self._delay = config.delay

        self._running_lock = asyncio.Lock()
        self._stop_signal: asyncio.Event | None = None
        self._stopped_signal: asyncio.Event | None = None

    async def stop_polling(self) -> None:
        """Stop polling."""
        if not self._running_lock.locked():
            msg = "Polling is not started"
            raise RuntimeError(msg)

        if self._stop_signal is None or self._stopped_signal is None:
            return

        self._stop_signal.set()
        await self._stopped_signal.wait()

    async def start_polling(
        self: "ClientWebhookManagerProtocol",
        background: "Callable[[], Any] | None" = None,
    ) -> None:
        """
        Run polling.

        :param background: function to run in background.
        """
        if self._webhook_manager is not None:
            red = "\033[91m"
            reset = "\033[0m"
            warnings.warn(
                f"{red}Webhook manager is set. "
                f"Using polling may lead to event duplication.{reset}",
                stacklevel=2,
            )

        async with self._running_lock:
            if self._stop_signal is None:
                self._stop_signal = asyncio.Event()

            if self._stopped_signal is None:
                self._stopped_signal = asyncio.Event()

            self._stop_signal.clear()
            self._stopped_signal.clear()

            if background is not None:
                loop = asyncio.get_running_loop()
                loop.run_in_executor(None, background)

            loggers.polling.info("Start polling")

            tasks = [
                asyncio.create_task(
                    self._start_invoice_polling(),
                ),
                asyncio.create_task(
                    self._start_check_polling(),
                ),
                asyncio.create_task(
                    self._stop_signal.wait(),
                ),
            ]

            try:
                done, pending = await asyncio.wait(
                    tasks,
                    return_when=asyncio.FIRST_COMPLETED,
                )

                for task in pending:
                    task.cancel()

                await asyncio.gather(
                    *pending,
                    return_exceptions=True,
                )

                await asyncio.gather(*done)

            except (
                asyncio.CancelledError,
                KeyboardInterrupt,
                SystemExit,
            ):
                self._stop_signal.set()
                raise

            finally:
                for task in tasks:
                    if not task.done():
                        task.cancel()

                await asyncio.gather(
                    *tasks,
                    return_exceptions=True,
                )

                loggers.polling.info("Polling stopped")
                self._stopped_signal.set()
