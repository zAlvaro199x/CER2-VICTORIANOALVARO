from django.apps import AppConfig


# establece el tipo de campo ID por defecto
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
