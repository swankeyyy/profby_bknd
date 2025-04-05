from datetime import datetime
from typing import TypeVar, Generic, Type

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

import telebot
from telegram.error import TelegramError

from src.settings import settings
from src.models import Contact, SocialLink, Review, Profession, Section, Client

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


# Special service for sections with load joined content
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


# Special service for clients
class ClientService(Generic[ModelType]):
    """Special Service for clients"""

    def __init__(self, model):
        # Initialize model
        self.model = model

    async def create_client(
        self, client: dict, session: AsyncSession
    ) -> bool | Exception:
        """Create new client from dict and commit to database"""
        # Try to create client
        try:
            name, phone, message = (
                client.get("name", "Неизвестный"),
                client.get("phone"),
                client.get("message"),
            )
            stmt = self.model(name=name, phone=phone, message=message)
            session.add(stmt)
            await session.commit()

            # Send notification
            await self.create_tg_notification(name, phone, message)
            return True
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")

    async def create_tg_notification(self, name: str, phone: str, message: str):
        try:
            # Init TG bot and TG chat
            message = (
                "🆕 Новый клиент:\n"
                f"👤 Имя: {name}\n"
                f"📞 Телефон: {phone}\n"
                f"📝 Примечание: {message}\n"
                f"⏰ Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            bot = telebot.TeleBot(token=settings.BOT_TOKEN)
            chat_id = settings.CHAT_ID
            bot.send_message(chat_id=chat_id, text=message)

        except TelegramError as e:
            print(f"Telegram notification failed: {str(e)}")


# Initialize especial service for clients
client_service = ClientService(Client)
