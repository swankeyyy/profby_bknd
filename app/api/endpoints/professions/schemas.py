from pydantic import BaseModel, ConfigDict, field_validator
from uuid import UUID
from typing import Optional

from src.settings import settings


class Base(BaseModel):
    """Base schema with id"""
    id: UUID
    model_config = ConfigDict(
        from_attributes=True
    )


class ProfessionSchema(Base):
    """Schema for Profession wit id, name. Description and Image will show if it exists"""
    name: str
    description: Optional[str] = None
    image: Optional[str] = None

    @field_validator("image")
    def format_image(cls, v):
        """Format image url by add into start url, looks like hardcode"""
        v = settings.URL + '/' + v
        return v
