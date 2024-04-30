import abc

from onlysubs.application.common.interfaces.emails import (
    UserActivationEmailSender,
)
from onlysubs.application.common.interfaces.user import UserByEmailReader


class UserRepository(UserByEmailReader, abc.ABC):
    pass


class EmailSender(UserActivationEmailSender, abc.ABC):
    pass
