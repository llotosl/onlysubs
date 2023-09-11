from onlysubs.application.common.exceptions import (
    UserEmailNotFoundError,
    UserIdNotFoundError,
)
from onlysubs.application.common.interfaces.user import (
    UserByEmailChecker,
    UserByEmailReader,
    UserByIdReader,
    UserByUsernameChecker,
    UserSaver,
)
from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import User, UserId, Username

user_data: dict[int, User] = {}
user_id = 0


class InMemoryUserRepository(
    UserSaver,
    UserByEmailChecker,
    UserByEmailReader,
    UserByIdReader,
    UserByUsernameChecker,
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
        for user in user_data.values():
            if user.email == email:
                return True

        return False

    async def is_user_exists_by_username(self, username: Username) -> bool:
        for user in user_data.values():
            if user.username == username:
                return True

        return False
