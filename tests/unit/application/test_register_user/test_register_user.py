import pytest

from onlysubs.adapters.db.in_memory.user import InMemoryUserRepository
from onlysubs.application.common.exceptions import (
    UserEmailAlreadyExistsError,
    UsernameAlreadyExistsError,
)
from onlysubs.application.register_user.dto import RegisterUserDTO
from onlysubs.application.register_user.use_case import RegisterUserImpl
from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import Username
from tests.factories.user import create_user


def create_register_user_dto(
    email: Email | None = None,
    username: Username | None = None,
) -> RegisterUserDTO:
    return RegisterUserDTO(
        email=email or Email("test1@test.com"),
        first_name="test",
        last_name="test",
        password="<PASSWORD>",  # noqa: S106
        username=username or Username("test1"),
    )


@pytest.mark.asyncio()
async def test_register_user(
    register_user_use_case: RegisterUserImpl,
    in_memory_user_repository: InMemoryUserRepository,
) -> None:
    data = create_register_user_dto()

    user = await register_user_use_case(data)

    user = await in_memory_user_repository.get_user_by_id(user.id)
    assert user is not None


@pytest.mark.asyncio()
async def test_register_user_with_used_email(
    register_user_use_case: RegisterUserImpl,
    in_memory_user_repository: InMemoryUserRepository,
) -> None:
    user = create_user()
    await in_memory_user_repository.save_user(user)
    data = create_register_user_dto(email=user.email)

    with pytest.raises(UserEmailAlreadyExistsError):
        await register_user_use_case(data)


@pytest.mark.asyncio()
async def test_register_user_with_used_username(
    register_user_use_case: RegisterUserImpl,
    in_memory_user_repository: InMemoryUserRepository,
) -> None:
    user = create_user()
    await in_memory_user_repository.save_user(user)
    data = create_register_user_dto(username=user.username)

    with pytest.raises(UsernameAlreadyExistsError):
        await register_user_use_case(data)
