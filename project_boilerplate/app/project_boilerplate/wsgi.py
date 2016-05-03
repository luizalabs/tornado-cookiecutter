import os
import lib.server

os.environ['TORNADO_SETTINGS_MODULE'] = 'project_boilerplate.settings.production'

lib.server.get_server_application()
