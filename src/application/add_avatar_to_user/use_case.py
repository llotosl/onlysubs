from src.application.add_avatar_to_user.dto import AddAvatarToUserDTO
from src.application.add_avatar_to_user.interfaces import (
    FileRepository,
    FileStorageGateway,
    UserAvatarRepository,
    UserRepository,
)
from src.application.common.dto.file import LoadFileDTO
from src.application.common.exceptions import UserIdNotFoundError
from src.application.common.interfaces.uow import UoW
from src.application.common.use_case import UseCase
from src.domain.dto.avatar import CreateAvatarDTO
from src.domain.dto.file import CreateFileDTO
from src.domain.models.avatar import UserAvatar
from src.domain.services.avatar import UserAvatarService
from src.domain.services.file import FileService


class AddAvatarToUser(UseCase[AddAvatarToUserDTO, UserAvatar]):
    pass


class AddAvatarToUserImpl(AddAvatarToUser):
    def __init__(
        self,
        user_repo: UserRepository,
        file_repo: FileRepository,
        avatar_repo: UserAvatarRepository,
        file_storage_gateway: FileStorageGateway,
        uow: UoW,
        file_service: FileService,
        avatar_service: UserAvatarService,
    ) -> None:
        self.user_repo = user_repo
        self.file_repo = file_repo
        self.avatar_repo = avatar_repo
        self.file_storage_gateway = file_storage_gateway
        self.uow = uow
        self.file_service = file_service
        self.avatar_service = avatar_service

    async def __call__(self, data: AddAvatarToUserDTO) -> UserAvatar:
        is_user_exists = await self.user_repo.is_user_exists_by_id(
            data.user_id,
        )
        if not is_user_exists:
            raise UserIdNotFoundError(data.user_id)

        file_url = await self.file_storage_gateway.load_file(
            LoadFileDTO(
                content=data.file_content,
                name=data.file_name,
            ),
        )
        file = self.file_service.create_file(
            CreateFileDTO(
                data.file_name,
                url=file_url,
            ),
        )
        await self.file_repo.save_file(file)

        avatar = self.avatar_service.create_avatar(
            CreateAvatarDTO(
                user_id=data.user_id,
                file_id=file.id,
            ),
        )
        await self.avatar_repo.save_avatar(avatar)

        avatar.file = file

        return avatar
