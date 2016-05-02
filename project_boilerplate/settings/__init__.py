import os
from .base import * 

# import settings based at TORNADO_MODULE_SETTINGS
__import__(
    'project_boilerplate.settings.{}'.format('development'),
    'settings'
)

