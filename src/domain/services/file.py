from datetime import UTC, datetime

from src.domain.dto.file import CreateFileDTO
from src.domain.models.file import File


class FileService:
    def create_file(self, data: CreateFileDTO) -> File:
        now = datetime.now(tz=UTC)
        return File(
            name=data.name,
            url=data.url,
            created_at=now,
            updated_at=now,
        )
