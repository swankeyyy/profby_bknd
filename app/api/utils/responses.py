from starlette import status


def get_responses(text):
    """Responses for api endpoints with text for messages"""
    responses = {
        status.HTTP_404_NOT_FOUND: {"description": f"{text} not found"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"}
    }
    return responses
