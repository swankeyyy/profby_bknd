from sqladmin import ModelView

from app.src.models import SocialLink, Contact, Review


class SocialLinkAdmin(ModelView, model=SocialLink):
    """Admin panel for Social Links"""
    name = 'Социальная сеть'
    name_plural = 'Социальные сети'
    page_size = 100
    column_list = [SocialLink.name, SocialLink.is_published]
    column_details_list = [SocialLink.name, SocialLink.url, SocialLink.icon, SocialLink.is_published]


class ContactAdmin(ModelView, model=Contact):
    """Admin panel for Contacts"""
    name = "Контакт"
    name_plural = "Контакты"
    page_size = 100
    column_list = [Contact.name, Contact.is_published]
    column_details_list = [Contact.name, Contact.contact, Contact.is_published]


class ReviewAdmin(ModelView, model=Review):
    """Admin panel for Reviews"""
    name = "Отзыв"
    name_plural = "Отзывы"
    page_size = 100
    column_list = [Review.name, Review.profession, Review.is_published]
    column_details_list = [Review.name, Review.profession, Review.image, Review.is_published]
