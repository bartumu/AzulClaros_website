from django.apps import AppConfig


class PortifolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Portifolio'

    def ready(self):
        import Portifolio.signals
