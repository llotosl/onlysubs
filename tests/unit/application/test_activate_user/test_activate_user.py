import pytest

from onlysubs.adapters.activation_crypt.jwt_crypt.jwt_cryptor import (
    JWTActivationCryptor,
)
from onlysubs.adapters.db.in_memory.user import InMemoryUserRepository
from onlysubs.application.activate_user.dto import ActivateUserDTO
from onlysubs.application.activate_user.use_case import ActivateUserImpl
from onlysubs.domain.services.user_activation import UserActivationService
from tests.factories.user import create_user


@pytest.mark.asyncio()
async def test_activate_user(
    activate_user_use_case: ActivateUserImpl,
    in_memory_user_repository: InMemoryUserRepository,
    user_activation_service: UserActivationService,
    jwt_cryptor: JWTActivationCryptor,
) -> None:
    user = create_user(is_active=False)
    await in_memory_user_repository.save_user(user)
    activation = user_activation_service.create_user_activation(user)
    token = jwt_cryptor.encrypt(activation)

    await activate_user_use_case(ActivateUserDTO(token))

    user = await in_memory_user_repository.get_user_by_id(user.id)
    assert user.is_active
