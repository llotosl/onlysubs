from dataclasses import dataclass

from src.domain.models.url import URL


@dataclass
class CreateFileDTO:
    name: str
    url: URL
