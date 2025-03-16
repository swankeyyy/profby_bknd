from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from starlette import status

from api.utils.handlers import errors_handler
from .schemas import ContactSchema, SocialLinkSchema
from src.models.db_config import db_config
from api.service.service import contact_service, social_link_service

router = APIRouter()


@router.get("/", response_model=List[ContactSchema], summary="List all contacts for footer",
            responses={
                status.HTTP_404_NOT_FOUND: {"description": "Contacts not found"},
                status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"}
            })
@errors_handler
async def get_contacts(session: AsyncSession = Depends(db_config.get_session)) -> List[ContactSchema]:
    """
        Retrieve all contacts for website footer including phone numbers and other contact information.

        Returns:
        - List of contact objects with details
        - 404 if no contacts found
        - 500 for server errors
        """

    contacts = await contact_service.get_all(session)
    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No contacts found in database"
        )
    return contacts


@router.get("/links/", response_model=List[SocialLinkSchema], summary="List all links of socials for footer",
            responses={
                status.HTTP_404_NOT_FOUND: {"description": "Links not found"},
                status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"}
            })
@errors_handler
async def get_links(session: AsyncSession = Depends(db_config.get_session)) -> List[SocialLinkSchema]:
    """
           Retrieve all links for website footer.

           Returns:
           - List of links objects with details
           - 404 if no contacts found
           - 500 for server errors
           """
    links = await social_link_service.get_all(session)
    if not links:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No links found in database"
        )
    return links
