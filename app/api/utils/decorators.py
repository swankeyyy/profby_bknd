import functools

from fastapi import HTTPException
from starlette import status

# Error handler decorator for endpoints that may raise database exceptions 
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
