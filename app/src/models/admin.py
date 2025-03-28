from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

# Table for admins with username and password, use create_superuser.py to create superuser
class Admin(Base):
    __tablename__ = 'admins'
    
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)

