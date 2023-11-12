from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.restaurants"

    def ready(self):
        from src.restaurants.templatetags import custom_tags
