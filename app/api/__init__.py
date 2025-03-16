from fastapi import APIRouter

from src.settings import settings
from api.contacts.views import router as contacts_router

router = APIRouter(prefix=settings.API_PREFIX)
router.include_router(contacts_router, prefix="/contacts", tags=["contacts"])
