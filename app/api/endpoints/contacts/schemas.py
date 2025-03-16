from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional


class Base(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )


class ContactSchema(Base):
    id: UUID
    name: Optional[str] = None
    contact: str


class SocialLinkSchema(Base):
    id: UUID
    name: str
    url: str
    icon: str
