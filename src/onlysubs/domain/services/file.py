from datetime import datetime, UTC

from onlysubs.domain.dto.file import CreateFileDTO
from onlysubs.domain.models.file import File


class FileService:
    def create_file(self, data: CreateFileDTO) -> File:
        now = datetime.now(tz=UTC)
        return File(
            name=data.name,
            url=data.url,
            created_at=now,
            updated_at=now,
        )
