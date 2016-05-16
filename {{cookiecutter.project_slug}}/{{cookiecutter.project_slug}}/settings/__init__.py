import os
import importlib 

print(os.getenv('TORNADO_SETTINGS_MOULE'))

# import all settings
settings = importlib.import_module(os.getenv('TORNADO_SETTINGS_MODULE'))
