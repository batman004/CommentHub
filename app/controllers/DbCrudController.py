from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from models import models, serializers


class DbCrudController:
    def __init__(self, DbSession) -> None:
        self.db = DbSession

    def create_file(self, file: serializers.FileCreate):
        try:
            db_file = models.File(location=file.location)
            self.db.add(db_file)
            self.db.commit()
            self.db.refresh(db_file)
            return db_file
        except SQLAlchemyError as e:
            self.db.rollback()
            return type(e)

    def get_file_id(self, location: str):
        try:
            file_id_query = (
                self.db.query(models.File.id)
                .filter(models.File.location == location)
                .first()
            )
            return int(file_id_query.id)
        except SQLAlchemyError as e:
            self.db.rollback()
            return type(e)

    def get_file_by_location(self, location: str):
        try:
            get_file = (
                self.db.query(models.File)
                .filter(models.File.location == location)
                .first()
            )
            file = get_file.__dict__
            return file
        except SQLAlchemyError as e:
            self.db.rollback()
            return type(e)

    def get_file_versions(self, file_id: int):
        try:
            file_versions = []
            file_version_query = (
                self.db.query(models.Version)
                .filter(models.Version.file_id == file_id)
                .all()
            )

            for file_version in file_version_query:
                file_versions.append(file_version.__dict__)

            return file_versions

        except SQLAlchemyError as e:
            self.db.rollback()
            return type(e)

    def get_file_version(self, file_id: int, version_id: int):
        try:

            file_version_query = (
                self.db.query(models.Version)
                .filter(
                    models.Version.file_id == file_id,
                    models.Version.version == version_id,
                )
                .one()
            )
            return file_version_query.__dict__

        except SQLAlchemyError as e:
            self.db.rollback()
            return type(e)

    def get_latest_file_version(self, file_id: int):
        try:
            latest_version = (
                self.db.query(models.Version)
                .filter(
                    models.Version.file_id == file_id,
                    models.Version.version
                    == self.db.query(
                        func.max(models.Version.version)
                    ).scalar_subquery(),
                )
                .one()
            )
            return latest_version.__dict__
        except SQLAlchemyError as e:
            self.db.rollback()
            return type(e)

    def create_file_version(self, version: serializers.Version):
        try:
            db_file_version = models.Version(**version.dict())
            self.db.add(db_file_version)
            self.db.commit()
            self.db.refresh(db_file_version)
            return db_file_version

        except SQLAlchemyError as e:
            self.db.rollback()
            return type(e)

    def edit_file_name(self, new_file: serializers.FileNameEdit, location: str):
        pass
