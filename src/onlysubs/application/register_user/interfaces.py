import abc

from onlysubs.application.common.interfaces.emails import \
    UserActivationEmailSender
from onlysubs.application.common.interfaces.user import (UserByEmailChecker,
                                                         UserByEmailReader,
                                                         UserByUsernameChecker,
                                                         UserSaver)


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
