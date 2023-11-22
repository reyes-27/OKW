from django.apps import AppConfig
from django.core.signals import setting_changed

class MembershipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.membership'

    def ready(self):
        from . import signals