from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'your_app'  # Make sure this matches your app name

    def ready(self):
        # Import signals when the app is ready
        import your_app.signals  # noqa
