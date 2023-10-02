import os
import uuid

import aiofiles

from onlysubs.application.common.dto.file import LoadFileDTO
from onlysubs.application.common.interfaces.file import FileStorageLoader
from onlysubs.domain.models.url import URL


class LocalFileStorageGateway(FileStorageLoader):
    async def load_file(self, data: LoadFileDTO) -> URL:
        file_name_in_storage = str(uuid.uuid4()) + data.name
        file_path_in_storage = os.path.join("media/", file_name_in_storage)

        async with aiofiles.open(file_path_in_storage, "ab+") as file_obj:
            await file_obj.write(await data.content.read())

        return URL(file_path_in_storage)
