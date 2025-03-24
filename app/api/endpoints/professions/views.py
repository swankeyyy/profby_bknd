from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.db_config import db_config
from api.service.crud import profession_service
from .schemas import ProfessionSchema
from api.utils.decorators import errors_handler
from api.utils.responses import get_responses
from api.utils.handlers import get_data

router = APIRouter()


@router.get("/", response_model=List[ProfessionSchema], summary="List all professions for footer",
            responses=get_responses("Professions"))
@errors_handler
async def get_professions(session: AsyncSession = Depends(db_config.get_session)):
    """
        Retrieve all professions for website footer including phone numbers and other contact information.

        Returns:
        - List of contact objects with details
        - 404 if no contacts found
        - 500 for server errors
        """
    return await get_data(instance=profession_service, session=session, text="Professions")
