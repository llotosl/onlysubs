from dataclasses import dataclass

from src.application.common.interfaces.readable_file import ReadableFile
from src.domain.models.user import UserId


@dataclass(frozen=True)
class AddAvatarToUserDTO:
    user_id: UserId
    file_name: str
    file_content: ReadableFile
