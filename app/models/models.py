from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, unique=True)

    versions = relationship("Version", back_populates="file")


class Version(Base):
    __tablename__ = "versions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    location = Column(String, unique=True)
    version = Column(String)
    file_id = Column(Integer, ForeignKey("files.id"))

    file = relationship("File", back_populates="versions")
