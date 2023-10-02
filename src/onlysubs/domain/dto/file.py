from dataclasses import dataclass

from onlysubs.domain.models.url import URL


@dataclass
class CreateFileDTO:
    name: str
    url: URL
