import os

os.setdefault['TORNADO_SETTINGS_MODULE'] = 'settings.production'

import app

app.get_server_application()
