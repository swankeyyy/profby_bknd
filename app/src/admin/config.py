from sqladmin import Admin

from src.settings import settings

from .authentication import AdminAuthBackend
from src.models.db_config import db_config
from .models import (
    SocialLinkAdmin,
    ContactAdmin,
    ReviewAdmin,
    ProfessionAdmin,
    SectionAdmin,
    SectionImageAdmin,
)

# List of views for the Admin Panel, add it from .models
list_views = [
    SocialLinkAdmin,
    ContactAdmin,
    ReviewAdmin,
    ProfessionAdmin,
    SectionImageAdmin,
    SectionAdmin,
]


def create_admin(app):
    """Connect Admin Panel to database and to main app"""
    
    # Initialize the Admin Panel with the database engine and authentication backend
    admin = Admin(
        app=app,
        engine=db_config.get_engine(),
        authentication_backend=AdminAuthBackend(secret_key=settings.SECRET_KEY),
    )
    
    # Add views to the Admin Panel
    for view in list_views:
        admin.add_view(view)
    return admin
