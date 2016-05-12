import os

os.setdefault['TORNADO_SETTINGS_MODULE'] = 'apps.settings'

from contrib import server

server.get_server_application()
