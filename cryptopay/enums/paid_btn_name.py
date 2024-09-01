from enum import StrEnum


class PaidBtnName(StrEnum):
    """
    Paid button name.

    Label of the button which will be presented
    to a user after the invoice is paid.
    """

    VIEWITEM = "viewItem"
    OPENCHANNEL = "openChannel"
    OPENBOT = "openBot"
    CALLBACK = "callback"
