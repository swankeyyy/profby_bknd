from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Contact


class ContactsService:
    """All CRUD operations for contacts."""

    @staticmethod
    async def get_all_contacts(session: AsyncSession) -> list[Contact]:
        """
                Retrieve all contacts from database

                Args:
                    session: Async database session

                Returns:
                    List of Contact objects (empty list if no contacts found)

                Raises:
                    DatabaseError: If any database error occurs
                """
        try:
            stmt = select(Contact)
            contacts = await session.scalars(stmt)
            return list(contacts)
        except Exception as e:
            raise RuntimeError(f"Database error: {str(e)}") from e
