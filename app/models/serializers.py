from typing import List, Union
from pydantic import BaseModel


class VersionBase(BaseModel):
    version: int
    description: Union[str, None] = None


class Version(VersionBase):
    id: int
    file_id: int

    class Config:
        orm_mode = True


class FileBase(BaseModel):
    location: str


class File(FileBase):
    id: int
    versions: List[Version] = []
