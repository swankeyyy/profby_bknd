from typing import List

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType
from sqlalchemy import ForeignKey, String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID

from .base import Base
from src.settings import settings

storage = FileSystemStorage(path=settings.SECTIONS_STORAGE)


class SectionImage(Base):
    """Table with images for Section table(FK)"""
    __tablename__ = 'section_images'
    image: Mapped[str] = mapped_column(ImageType(storage))
    section_id: Mapped[UUID] = mapped_column(ForeignKey('sections.id'), nullable=True)
    section_image: Mapped["Section"] = relationship(back_populates="images")

    def __repr__(self):
        return f"{self.image}"

    def __str__(self):
        return f"{self.image}"


class Section(Base):
    """Table for Sections on site with HTML content and background images"""
    __tablename__ = 'sections'
    name: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str]
    images: Mapped[List["SectionImage"]] = relationship(back_populates="section_image", cascade="all, delete-orphan",
                                                        lazy="joined")

    def __repr__(self):
        return f"{self.name} - {self.title}"

    def __str__(self):
        return f"{self.name}"
