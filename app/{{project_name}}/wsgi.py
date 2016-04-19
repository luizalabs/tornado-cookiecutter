import lib.server

os.environ['TORNADO_SETTINGS_MODULE'] = 'settings.production'

lib.server.get_server_application()
