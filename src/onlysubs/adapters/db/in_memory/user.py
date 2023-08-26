from onlysubs.application.common.exceptions import (
    UserEmailNotFoundError,
    UserIdNotFoundError,
)
from onlysubs.application.common.interfaces.user import (
    UserByUsernameChecker,
    UserSaver,
    UserByEmailChecker,
    UserByEmailReader,
    UserByIdReader,
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

    async def get_user_by_id(self, id: UserId) -> User:
        user = user_data.get(int(id))
        if user is not None:
            return user
        raise UserIdNotFoundError(user_id=id)

    async def get_user_by_email(self, email: Email) -> User:
        for user in user_data.values():
            if user.email == email:
                return user

        raise UserEmailNotFoundError(email=email)

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
