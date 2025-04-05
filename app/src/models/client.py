from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, validates

from .base import Base

# Table for clients, who come from site
class Client(Base):
    """Model for clients who visit the site"""

    __tablename__ = "clients"
    name: Mapped[str] = mapped_column(String(50), nullable=True, default="Неизвестный")
    phone: Mapped[str] = mapped_column(String(13), nullable=False)
    message: Mapped[str] = mapped_column(String(500), nullable=True)

    def __repr__(self):
        return f"{self.name} - {self.phone}"

    def __str__(self):
        return super().__repr__()

    @validates("phone")
    def validate(self, key, value: str):
        """Validate phone number format"""
        # Check if the phone number is in the correct format
        if len(value) == 13 and value.startswith("+375"):
            # Try to convert int or raise error
            try:
                numeric_part: str = value[1:]
                numeric_part = int(numeric_part)
            except ValueError:
                raise ValueError("Phone number must be numeric")
        return value
