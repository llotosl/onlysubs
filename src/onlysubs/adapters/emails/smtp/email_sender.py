from onlysubs.application.common.interfaces.emails import (
    UserActivationEmailSender,
    UserConfirmationEmailSender,
)


class SMTPEmailSender(UserConfirmationEmailSender, UserActivationEmailSender):
    pass
