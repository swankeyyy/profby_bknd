from src.models.db_config import db_config
from .models import SocialLinkAdmin, ContactAdmin, ReviewAdmin, ProfessionAdmin
from sqladmin import Admin

list_views = [SocialLinkAdmin, ContactAdmin, ReviewAdmin, ProfessionAdmin]


def create_admin(app):
    """Connect Admin Panel to database and to main app"""
    admin = Admin(app=app, engine=db_config.get_engine())
    for view in list_views:
        admin.add_view(view)
    return admin
