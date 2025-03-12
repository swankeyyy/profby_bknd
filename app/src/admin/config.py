from app.src.models.db_config import db_config
from sqladmin import Admin


def create_admin(app):
    """Connect Admin Panel to database and to main app"""
    admin = Admin(app=app, engine=db_config.get_engine())
    return admin
