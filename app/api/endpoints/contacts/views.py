from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from api.utils.decorators import errors_handler
from api.utils.responses import get_responses
from api.utils.handlers import get_data
from .schemas import ContactSchema, SocialLinkSchema
from src.models.db_config import db_config
from api.service.crud import contact_service, social_link_service

# init router
router = APIRouter()

# Endpoints for all contacts, links and socials. Only GET methods are allowed, no need for authentication

@router.get("/", response_model=List[ContactSchema], summary="List all contacts for footer",
            responses=get_responses("Contacts"))
@errors_handler
async def get_contacts(session: AsyncSession = Depends(db_config.get_session)) -> List[ContactSchema]:
    """
        Retrieve all contacts for website footer including phone numbers and other contact information.

        Returns:
        - List of contact objects with details
        - 404 if no contacts found
        - 500 for server errors
        """

    return await get_data(instance=contact_service, session=session, text="Contacts")


@router.get("/links/", response_model=List[SocialLinkSchema], summary="List all links of socials for footer",
            responses=get_responses("Links"))
@errors_handler
async def get_links(session: AsyncSession = Depends(db_config.get_session)) -> List[SocialLinkSchema]:
    """
           Retrieve all links for website footer.

           Returns:
           - List of links objects with details
           - 404 if no contacts found
           - 500 for server errors
           """
    return await get_data(instance=social_link_service, session=session, text="Links")
