from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.service.service import review_service
from .schemas import ReviewSchema
from src.models.db_config import db_config
from api.utils.handlers import errors_handler

router = APIRouter()


@router.get("/", response_model=List[ReviewSchema], summary="Get all reviews for review section", responses={
    status.HTTP_404_NOT_FOUND: {"description": "Links not found"},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"}
})
@errors_handler
async def get_reviews(session: AsyncSession = Depends(db_config.get_session)):
    reviews = await review_service.get_all(session)
    if not reviews:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No links found in database"
        )
    return reviews
