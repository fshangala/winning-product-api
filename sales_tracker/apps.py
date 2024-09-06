from django.apps import AppConfig
from django.db.models.signals import post_save


class SalesTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales_tracker'