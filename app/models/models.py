from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, unique=True)
    created = Column(DateTime, default=datetime.utcnow)

    versions = relationship(
        "Version", back_populates="file", cascade="all, delete", passive_deletes=True
    )

    def __repr__(self):
        return (
            f"File(id={self.id}, location={self.location}, created_at={self.created})"
        )


class Version(Base):
    __tablename__ = "versions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    location = Column(String, unique=True)
    version = Column(Integer, autoincrement=True)
    file_id = Column(Integer, ForeignKey("files.id", ondelete="CASCADE"))

    file = relationship("File", back_populates="versions")

    def __repr__(self):
        return f"Version(id={self.id}, location={self.location}, version={self.version}, file_id={self.file_id})"
