from typing import TYPE_CHECKING

from aiocpa.enums import CheckStatus

if TYPE_CHECKING:
    import aiocpa


class DeleteAllChecks:
    """Delete all checks."""

    async def delete_all_checks(
        self: "aiocpa.CryptoPay",
    ) -> None:
        """
        Delete all checks.

        Wrapper for :class:`cryptopay.CryptoPay.get_checks`
        and :class:`cryptopay.CryptoPay.delete_check`

        Use this method to delete all existing
        checks created by your app.

        :return:
        """
        checks = await self.get_checks(status=CheckStatus.ACTIVE)
        for check in checks:
            await check.delete()
