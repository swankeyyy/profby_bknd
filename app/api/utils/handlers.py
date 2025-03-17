from fastapi import HTTPException
from starlette import status


async def get_data(instance, session, text):
    result = await instance.get_all(session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No {text} found in database"
        )
    return result
