from typing import Optional, List

from pydantic import BaseModel, ConfigDict, field_validator
from uuid import UUID

from src.settings import settings


class Base(BaseModel):
    """Base schema with ID"""
    id: UUID
    model_config = ConfigDict(
        from_attributes=True
    )


class SectionImageSchema(Base):
    """Schema for section images"""
    image: Optional[str] = None

    @field_validator("image")
    def format_image(cls, v):
        """Format image url by add into start url, looks like hardcode"""
        
        # If image is not None, add the URL to the image, it needs for the frontend to display the image
        v = settings.URL + '/' + v
        return v

# Images are optional 
class SectionSchema(Base):
    """Section of content Schema"""
    name: str
    title: str
    content: str
    images: Optional[List[SectionImageSchema]] = None
