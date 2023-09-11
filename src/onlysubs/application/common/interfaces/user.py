import abc

from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import User, UserId, Username


class UserSaver(abc.ABC):
    @abc.abstractmethod
    async def save_user(self, user: User) -> None:
        raise NotImplementedError


class UserByEmailReader(abc.ABC):
    @abc.abstractmethod
    async def get_user_by_email(self, email: Email) -> User | None:
        raise NotImplementedError


class UserByIdReader(abc.ABC):
    @abc.abstractmethod
    async def get_user_by_id(self, id: UserId) -> User | None:
        raise NotImplementedError


class UserByEmailChecker(abc.ABC):
    @abc.abstractmethod
    async def is_user_exists_by_email(self, email: Email) -> bool:
        raise NotImplementedError


class UserByUsernameChecker(abc.ABC):
    @abc.abstractmethod
    async def is_user_exists_by_username(self, username: Username) -> bool:
        raise NotImplementedError
