import abc

from src.application.common.interfaces.emails import UserActivationEmailSender
from src.application.common.interfaces.user import (
    UserByEmailChecker,
    UserByEmailReader,
    UserByUsernameChecker,
    UserSaver,
)


class UserRepository(
    UserSaver,
    UserByEmailReader,
    UserByEmailChecker,
    UserByUsernameChecker,
    abc.ABC,
):
    pass


class EmailSender(UserActivationEmailSender, abc.ABC):
    pass
