from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType

from src.domain.models.url import URL

FileId = NewType("FileId", int)


@dataclass
class File:
    id: FileId = field(init=False)
    name: str
    url: URL
    created_at: datetime
    updated_at: datetime
