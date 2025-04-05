from typing import Optional
from pydantic import BaseModel, field_validator


class ClientSchema(BaseModel):
    """Client from form schema"""

    name: str
    phone: str
    message: Optional[str] = "Без примечания"

    @field_validator("phone")
    def validate_phone(cls, v):
        if len(v) == 13 and v.startswith("+375"):
            return v
        raise ValueError("Phone number must be numeric")
