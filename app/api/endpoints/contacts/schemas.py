from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional


class Base(BaseModel):
    """Base schema with ID"""
    id: UUID
    model_config = ConfigDict(
        from_attributes=True
    )


class ContactSchema(Base):
    """Schema for contacts with id, name(if it exists) and contact"""
    name: Optional[str] = None
    contact: str


class SocialLinkSchema(Base):
    """Schema for social links with id, name and favicon"""
    name: str
    url: str
    icon: str
