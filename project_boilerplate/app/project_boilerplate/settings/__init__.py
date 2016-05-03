import os
from .base import * 

from dotenv import load_dotenv 

# load environment
dotenv_path = os.path.join(os.path.dirname(BASE_DIR), '.env')
load_dotenv(dotenv_path)


# import settings based at TORNADO_MODULE_SETTINGS
__import__(
    '{module}'.format(module=os.getenv('TORNADO_SETTINGS_MODULE')),
    'settings'
)

