from fastapi import HTTPException, Request, Depends
from passlib.context import CryptContext
from sqladmin.authentication import AuthenticationBackend
from sqlalchemy import select
import bcrypt

from src.models.db_config import db_config
from src.models import Admin

# fix the problem with bcrypt(version problem)
bcrypt.__about__ = bcrypt

# create a password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AdminAuthBackend(AuthenticationBackend):
    """Authentication backend for Admin Panel"""

    async def login(self, request: Request) -> bool:
        # takes username and password from form
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        if not username or not password:
            raise HTTPException(
                status_code=400, detail="Username and password required"
            )

        # check user in database
        async for session in db_config.get_session():
            stmt = select(Admin).where(Admin.username == username)
            admin = await session.execute(stmt)
            admin = admin.scalars().first()

            if not admin:
                raise HTTPException(status_code=401, detail="Неверные данные")

            # check input password with password in database and if it is correct, create session
            hashed_password = admin.password

            if pwd_context.verify(password, hashed_password):
                request.session.update({"user": username})
                return True
            else:
                raise HTTPException(status_code=401, detail="Неверные данные")

    async def logout(self, request: Request) -> bool:
        # clear session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        # check if user is in session
        return "user" in request.session
