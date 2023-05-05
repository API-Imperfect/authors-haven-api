from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.search"
    verbose_name = _("Search")
