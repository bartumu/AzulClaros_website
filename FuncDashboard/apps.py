from django.apps import AppConfig


class FuncdashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FuncDashboard'

    def ready(self):
        import FuncDashboard.signals