from typing import TypeVar, Generic, Type

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from src.models import Contact, SocialLink, Review, Profession, Section

# Generic type for model
ModelType = TypeVar("ModelType")


class BaseService(Generic[ModelType]):
    """Base service for CRUD operations"""

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_all(self, session: AsyncSession) -> list[ModelType]:
        """
        Retrieve all items from database

        Args:
            session: Async database session

        Returns:
            List of items (empty list if no items found)

        Raises:
            Exception: If any database error occurs
        """
        try:
            stmt = select(self.model).where(self.model.is_published == True)
            items = await session.scalars(stmt)
            return list(items)
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}") from e


# Base services initialization
contact_service = BaseService(Contact)
social_link_service = BaseService(SocialLink)
review_service = BaseService(Review)
profession_service = BaseService(Profession)


class SectionService(BaseService):
    """Special Service for sections with load joined content"""

    async def get_all(self, session: AsyncSession) -> list[ModelType]:
        try:
            # Load images for sections by joinedload
            stmt = (
                select(Section)
                .where(self.model.is_published == True)
                .options(joinedload(Section.images))
            )
            sections = await session.execute(stmt)
            sections = sections.scalars().unique().all()
            return list(sections)
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}") from e

# Initialize especial service for sections
content_service = SectionService(Section)
