from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, field_validator

from src.settings import settings


class ReviewBase(BaseModel):
    id: UUID
    model_config = ConfigDict(
        from_attributes=True
    )


class ReviewSchema(ReviewBase):
    """Schema for Reviews read."""

    name: str
    profession: Optional[str] = None
    review: str
    image: Optional[str] = None

    @field_validator("image")
    def format_image(cls, v):
        """Format image url by add into start url, looks like hardcode"""
        v = settings.URL + '/' + v
        return v
