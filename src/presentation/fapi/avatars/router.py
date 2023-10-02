from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile

from src.application.add_avatar_to_user.dto import AddAvatarToUserDTO
from src.application.add_avatar_to_user.use_case import AddAvatarToUser
from src.domain.models.avatar import UserAvatar
from src.domain.models.user import UserId
from src.presentation.fapi.avatars.models import PublicAvatarModel

avatar_router = APIRouter()


@avatar_router.post("/{user_id}", response_model=PublicAvatarModel)
async def add_avatar_to_user_route(
    user_id: int,
    add_avatar_to_user: Annotated[AddAvatarToUser, Depends()],
    file: UploadFile,
) -> UserAvatar:
    return await add_avatar_to_user(
        AddAvatarToUserDTO(
            user_id=UserId(user_id),
            file_name=file.filename or "",
            file_content=file,
        ),
    )
