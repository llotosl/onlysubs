from dataclasses import dataclass

from onlysubs.application.common.interfaces.readable_file import ReadableFile


@dataclass(frozen=True)
class LoadFileDTO:
    content: ReadableFile
    name: str
