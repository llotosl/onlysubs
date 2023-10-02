from dataclasses import dataclass
from onlysubs.application.common.interfaces.readable_file import ReadableFile

from onlysubs.domain.models.user import UserId


@dataclass(frozen=True)
class AddAvatarToUserDTO:
    user_id: UserId
    file_name: str
    file_content: ReadableFile
