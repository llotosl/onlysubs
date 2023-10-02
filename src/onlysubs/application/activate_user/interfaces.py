import abc

from onlysubs.application.common.interfaces.emails import (
    UserConfirmationEmailSender,
)
from onlysubs.application.common.interfaces.user import (
    UserByIdReader,
    UserSaver,
)


class UserRepository(UserByIdReader, UserSaver, abc.ABC):
    pass


class EmailSender(UserConfirmationEmailSender, abc.ABC):
    pass
