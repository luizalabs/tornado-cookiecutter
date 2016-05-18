import os
import importlib 


# import all settings
settings = importlib.import_module(os.getenv('TORNADO_SETTINGS_MODULE'))
