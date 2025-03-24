from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.service.crud import review_service
from .schemas import ReviewSchema
from src.models.db_config import db_config
from api.utils.decorators import errors_handler
from api.utils.responses import get_responses
from api.utils.handlers import get_data

router = APIRouter()


@router.get("/", response_model=List[ReviewSchema], summary="Get all reviews for review section",
            responses=get_responses("Reviews"))
@errors_handler
async def get_reviews(session: AsyncSession = Depends(db_config.get_session)):
    """
            Retrieve all reviews for website footer including phone numbers and other contact information.

            Returns:
            - List of contact objects with details
            - 404 if no contacts found
            - 500 for server errors
            """
    return await get_data(instance=review_service, session=session, text="Reviews")
