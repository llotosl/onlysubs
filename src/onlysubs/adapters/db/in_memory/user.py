from onlysubs.application.common.interfaces.user import (
    UserByEmailChecker,
    UserByEmailReader,
    UserByIdChecker,
    UserByIdReader,
    UserByUsernameChecker,
    UserSaver,
)
from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import User, UserId, Username


class InMemoryUserRepository(
    UserSaver,
    UserByEmailChecker,
    UserByEmailReader,
    UserByIdReader,
    UserByUsernameChecker,
    UserByIdChecker,
):
    def __init__(self) -> None:
        self._user_data: dict[int, User] = {}
        self._user_id = 0

    async def save_user(self, user: User) -> None:
        self._user_id += 1

        self._user_data[self._user_id] = user
        user.id = UserId(self._user_id)

    async def get_user_by_id(self, id: UserId) -> User | None:
        return self._user_data.get(int(id))

    async def get_user_by_email(self, email: Email) -> User | None:
        for user in self._user_data.values():
            if user.email == email:
                return user

    async def is_user_exists_by_email(self, email: Email) -> bool:
        return any(user.email == email for user in self._user_data.values())

    async def is_user_exists_by_username(self, username: Username) -> bool:
        return any(
            user.username == username for user in self._user_data.values()
        )

    async def is_user_exists_by_id(self, id: UserId) -> bool:
        return self._user_data.get(int(id)) is not None
