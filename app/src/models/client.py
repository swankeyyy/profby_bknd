from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Client(Base):
    name: Mapped[str] = mapped_column(String(50), nullable=True, default="Неизвестный")
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    
    def __repr__(self):
        return f"{self.name} - {self.phone}"
    
    def __str__(self):
        return super().__repr__()
    
    def validate(self):
        pass