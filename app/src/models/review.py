from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_storages.integrations.sqlalchemy import ImageType
from fastapi_storages import FileSystemStorage

from src.settings import settings
from .base import Base

# Initialize the storage for the Review model
storage = FileSystemStorage(path=settings.REVIEWS_STORAGE)

# Professions and images are optional
class Review(Base):
    """People review model of choosen profession with photo, name, profession"""
    __tablename__ = 'reviews'
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    profession: Mapped[str] = mapped_column(String(30), nullable=True)
    review: Mapped[str] = mapped_column(String(500), nullable=False)
    image: Mapped[str] = mapped_column(ImageType(storage=storage), nullable=True)
