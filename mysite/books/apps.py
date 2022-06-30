from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
    verbose_name = 'Книги'


class CategoryConfig(AppConfig):
    name = 'category'
    verbose_name = 'Категории'