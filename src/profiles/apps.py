from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.profiles"

    def ready(self):
        import src.profiles.signals
