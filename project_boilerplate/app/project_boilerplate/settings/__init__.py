import os
from .base import * 


# import settings based at TORNADO_MODULE_SETTINGS
__import__(
    '{module}'.format(module=os.getenv('TORNADO_SETTINGS_MODULE')),
    'settings'
)

