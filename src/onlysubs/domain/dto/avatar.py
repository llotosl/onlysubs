from dataclasses import dataclass
from onlysubs.domain.models.file import FileId

from onlysubs.domain.models.user import UserId


@dataclass(frozen=True)
class CreateAvatarDTO:
    user_id: UserId
    file_id: FileId
