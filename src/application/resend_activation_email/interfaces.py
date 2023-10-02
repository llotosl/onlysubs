import abc

from src.application.common.interfaces.emails import UserActivationEmailSender
from src.application.common.interfaces.user import UserByEmailReader


class UserRepository(UserByEmailReader, abc.ABC):
    pass


class EmailSender(UserActivationEmailSender, abc.ABC):
    pass
