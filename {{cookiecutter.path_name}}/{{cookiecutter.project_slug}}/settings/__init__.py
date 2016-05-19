import os
import importlib 

from dotenv import load_dotenv


# Load environment variables
ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(ENV_PATH)

# import all settings
settings = importlib.import_module(os.getenv('TORNADO_SETTINGS_MODULE'))
