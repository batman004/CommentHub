from typing import List, Union
from pydantic import BaseModel


# creating new version of a file
class Version(BaseModel):
    version: int
    description: Union[str, None] = None
    file_id: int
    location: str

    class Config:
        orm_mode = True


# model used for creating file
class FileCreate(BaseModel):
    location: str


# model for querying a file
class File(BaseModel):
    location: str
    versions: List[Version] = []

    class Config:
        orm_mode = True


class FileNameEdit(BaseModel):
    location: str
