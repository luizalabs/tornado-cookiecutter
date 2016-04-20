import os
from .base import settings

# import settings bases at TORNADO_MODULE_SETTINGS
__import__(
    'project_boilerplate.settings.{}'.format('development'),
    'settings'
)
