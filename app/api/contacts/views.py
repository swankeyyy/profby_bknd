from fastapi import APIRouter, Depends, HTTPException
from typing import List, Union

from sqlalchemy.ext.asyncio import AsyncSession

from starlette import status

from .schemas import ContactSchema
from src.models.db_config import db_config
from .service import ContactsService

router = APIRouter()


@router.get("/", response_model=List[ContactSchema], summary="List all contacts for footer",
            responses={
                status.HTTP_404_NOT_FOUND: {"description": "Contacts not found"},
                status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"}
            })
async def get_contacts(session: AsyncSession = Depends(db_config.get_session)) -> List[ContactSchema]:
    """
        Retrieve all contacts for website footer including phone numbers and other contact information.

        Returns:
        - List of contact objects with details
        - 404 if no contacts found
        - 500 for server errors
        """
    try:
        contacts = await ContactsService.get_all_contacts(session)
        if not contacts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No contacts found in database"
            )
        return contacts

    except Exception as e:
        # Log the error here
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch contacts: {str(e)}"
        )
