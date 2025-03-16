from fastapi import APIRouter

from src.settings import settings
from api.endpoints.contacts.views import router as contacts_router
from api.endpoints.reviews.views import router as review_router

router = APIRouter(prefix=settings.API_PREFIX)
router.include_router(contacts_router, prefix="/contacts", tags=["contacts"])
router.include_router(review_router, prefix="/reviews", tags=["reviews"])
