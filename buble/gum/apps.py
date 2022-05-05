from tabnanny import verbose
from django.apps import AppConfig


class GumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gum'
    
    verbose_name = 'Жвачки'