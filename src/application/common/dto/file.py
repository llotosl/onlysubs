from dataclasses import dataclass

from src.application.common.interfaces.readable_file import ReadableFile


@dataclass(frozen=True)
class LoadFileDTO:
    content: ReadableFile
    name: str
