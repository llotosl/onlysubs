from dataclasses import dataclass

from src.domain.models.email import Email
from src.domain.models.user import UserId, Username


class ApplicationError(Exception):
    pass


@dataclass(eq=True)
class UserEmailAlreadyExistsError(ApplicationError):
    email: Email

    @property
    def message(self) -> str:
        return f"User with email `{self.email}` already exists"


@dataclass(eq=True)
class UsernameAlreadyExistsError(ApplicationError):
    username: Username

    @property
    def message(self) -> str:
        return f"User with username `{self.username}` already exists"


@dataclass(eq=True)
class UserIdNotFoundError(ApplicationError):
    user_id: UserId

    @property
    def message(self) -> str:
        return f"User with id `{self.user_id}` not exists"


@dataclass(eq=True)
class UserEmailNotFoundError(ApplicationError):
    email: Email

    @property
    def message(self) -> str:
        return f"User with email `{self.email}` not exists"
