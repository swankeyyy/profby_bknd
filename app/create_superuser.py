import asyncio

from sqlalchemy import select

from src.models.db_config import db_config
from src.models import Admin
from src.admin.authentication import pwd_context


# function to create a superuser by cmd
async def create_superuser(username: str, password: str):
    """Create a superuser with the given username and password."""
    async for session in db_config.get_session():
        stmt = select(Admin).where(Admin.username == username)
        existing = await session.execute(stmt)

        if existing.scalar():
            print(f"User {username} already exists!")
            return

        # hash the password by bcrypt
        hashed_password = pwd_context.hash(password)
        superuser_data = {
            "username": username,
            "password": hashed_password,
        }
        admin = Admin(**superuser_data)
        session.add(admin)
        await session.commit()
        await session.close()


# run the function
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python create_superuser.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    asyncio.run(create_superuser(username, password))
    print(f"Superuser {username} created successfully.")
