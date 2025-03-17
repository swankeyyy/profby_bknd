import functools

from fastapi import HTTPException
from starlette import status


def errors_handler(endpoint):
    @functools.wraps(endpoint)
    async def wrapper(*args, **kwargs):
        try:
            return await endpoint(*args, **kwargs)
        except Exception as e:
            # Log the error here
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to fetch data: {str(e)}"
            )

    return wrapper
