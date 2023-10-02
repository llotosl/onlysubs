import abc

from src.application.common.interfaces.emails import (
    UserConfirmationEmailSender,
)
from src.application.common.interfaces.user import UserByIdReader, UserSaver


class UserRepository(UserByIdReader, UserSaver, abc.ABC):
    pass


class EmailSender(UserConfirmationEmailSender, abc.ABC):
    pass
