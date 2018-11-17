from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdvancedFiltersConfig(AppConfig):
    name = 'advanced_filters'
    verbose_name = _('Advanced Filters')
