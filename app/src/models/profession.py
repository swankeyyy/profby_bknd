from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from src import settings


# Initialize the storage for the Review model
storage = FileSystemStorage(path=settings.PROFESSIONS_STORAGE)


# Table for profession with name description(optional) and image(optional)
class Profession(Base):
    """Table for profession with name description and image"""

    __tablename__ = "professions"
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    image: Mapped[str] = mapped_column(FileType(storage=storage), nullable=True)
