from sqladmin import ModelView

from src.models import (
    SocialLink,
    Contact,
    Review,
    Profession,
    Section,
    SectionImage,
    Client,
)

# Admin panels for models, it is used in the admin.py file, add models to list to add them to the admin panel


class SocialLinkAdmin(ModelView, model=SocialLink):
    """Admin panel for Social Links"""

    name = "Социальная сеть"
    name_plural = "Социальные сети"
    page_size = 100
    column_list = [SocialLink.name, SocialLink.is_published]
    column_details_list = [
        SocialLink.name,
        SocialLink.url,
        SocialLink.icon,
        SocialLink.is_published,
    ]


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
    column_details_list = [
        Review.name,
        Review.profession,
        Review.image,
        Review.is_published,
    ]


class ProfessionAdmin(ModelView, model=Profession):
    """Admin panel for Professions"""

    name = "Профессия"
    name_plural = "Профессии"
    page_size = 100
    column_list = [Profession.name, Profession.is_published]
    column_details_list = [
        Profession.name,
        Profession.is_published,
        Profession.image,
        Profession.description,
    ]


class SectionAdmin(ModelView, model=Section):
    """Admin panel for content sections"""

    name = "Контент"
    name_plural = "Контент"
    page_size = 100
    column_list = [Section.name, Section.title, Section.is_published]
    column_details_list = [
        Section.name,
        Section.title,
        Section.is_published,
        Section.content,
        Section.images,
    ]


class SectionImageAdmin(ModelView, model=SectionImage):
    """Admin panel for content sections"""

    name = "Изображение для секции контента"
    name_plural = "Изображения"
    page_size = 100
    column_list = [SectionImage.image, SectionImage.is_published]
    column_details_list = [
        SectionImage.image,
        SectionImage.is_published,
        SectionImage.section_id,
    ]


class ClientAdmin(ModelView, model=Client):
    """Admin panel for Clients"""

    name = "Клиент"
    name_plural = "Клиенты"
    page_size = 100
    column_list = [Client.name, Client.phone, Client.message]
    column_details_list = [Client.name, Client.phone, Client.message]
