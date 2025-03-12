from .base import Base

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Contact(Base):
    """For contacts like phone number(str)"""
    __tablename__ = "contacts"
    contact: Mapped[str] = mapped_column(String(20))


class SocialLink(Base):
    """For social links with favicons"""
    __tablename__ = "sociallinks"
    icon: Mapped[str]
    url: Mapped[str]
