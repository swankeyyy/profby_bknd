from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ClientSchema
from src.models.db_config import db_config
from api.service.crud import client_service
from api.utils.decorators import errors_handler

# Init router
router = APIRouter()


# Endpoint for form with client's data(name and phone)
@router.post(
    "/",
    responses={
        status.HTTP_200_OK: {"description": "Client created successfully"},
        status.HTTP_400_BAD_REQUEST: {"description": "Bad request"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"},
    },
)
@errors_handler
async def create_client(
    client: Annotated[ClientSchema, Form()],
    session: AsyncSession = Depends(db_config.get_session),
):
    created_client = await client_service.create_client(
        client=client.model_dump(), session=session
    )

    # Check if client was created
    if created_client:
        return {"description": "Client created successfully"}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create client"
    )
