from dataclasses import dataclass

from src.domain.models.file import FileId
from src.domain.models.user import UserId


@dataclass(frozen=True)
class CreateAvatarDTO:
    user_id: UserId
    file_id: FileId
