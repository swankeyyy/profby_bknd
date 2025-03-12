from .base import Base

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Contact(Base):
    """For contacts like phone number(str)"""
    __tablename__ = "contacts"
    name: Mapped[str] = mapped_column(nullable=True)
    contact: Mapped[str] = mapped_column(String(20))


class SocialLink(Base):
    """For social links with favicons"""
    __tablename__ = "sociallinks"
    name: Mapped[str]
    icon: Mapped[str]
    url: Mapped[str]
