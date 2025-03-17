from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.db_config import db_config
from .schemas import SectionSchema
from api.service.crud import content_service
from api.utils.responses import get_responses
from api.utils.handlers import get_data
from api.utils.decorators import errors_handler

router = APIRouter()


@router.get("/", response_model=List[SectionSchema], responses=get_responses("Content"))
@errors_handler
async def get_all_content(session: AsyncSession = Depends(db_config.get_session)):
    return await get_data(instance=content_service, session=session, text="Content")
