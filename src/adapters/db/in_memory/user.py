from src.application.common.interfaces.user import (
    UserByEmailChecker,
    UserByEmailReader,
    UserByIdChecker,
    UserByIdReader,
    UserByUsernameChecker,
    UserSaver,
)
from src.domain.models.email import Email
from src.domain.models.user import User, UserId, Username

user_data: dict[int, User] = {}
user_id = 0


class InMemoryUserRepository(
    UserSaver,
    UserByEmailChecker,
    UserByEmailReader,
    UserByIdReader,
    UserByUsernameChecker,
    UserByIdChecker,
):
    async def save_user(self, user: User) -> None:
        global user_id
        global user_data
        user_id += 1

        user_data[user_id] = user
        user.id = UserId(user_id)

    async def get_user_by_id(self, id: UserId) -> User | None:
        return user_data.get(int(id))

    async def get_user_by_email(self, email: Email) -> User | None:
        for user in user_data.values():
            if user.email == email:
                return user

    async def is_user_exists_by_email(self, email: Email) -> bool:
        return any(user.email == email for user in user_data.values())

    async def is_user_exists_by_username(self, username: Username) -> bool:
        return any(user.username == username for user in user_data.values())

    async def is_user_exists_by_id(self, id: UserId) -> bool:
        return user_data.get(int(id)) is not None
