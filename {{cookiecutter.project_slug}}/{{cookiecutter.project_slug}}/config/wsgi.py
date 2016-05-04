import os
import contrib.server

os.environ['TORNADO_SETTINGS_MODULE'] = 'settings.production'

contrib.server.get_server_application()
