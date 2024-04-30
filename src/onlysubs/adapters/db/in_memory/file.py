from onlysubs.application.common.interfaces.file import FileSaver
from onlysubs.domain.models.file import File, FileId

file_data: dict[int, File] = {}
file_id = 0


class InMemoryFileRepository(FileSaver):
    async def save_file(self, file: File) -> None:
        global file_data
        global file_id
        file_id += 1

        file_data[file_id] = file
        file.id = FileId(file_id)
