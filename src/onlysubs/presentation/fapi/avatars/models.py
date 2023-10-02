from datetime import datetime

from pydantic import BaseModel


class PublicFileModel(BaseModel):
    url: str
    created_at: datetime
    updated_at: datetime


class PublicAvatarModel(BaseModel):
    id: int
    file: PublicFileModel
