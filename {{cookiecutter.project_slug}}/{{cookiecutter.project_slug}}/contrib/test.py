import os

import tornado.testing


def run():
    os.environ.setdefault("TORNADO_SETTINGS_MODULE", "config.settings.test")
    tornado.testing.main() 

if __name__ == '__main__':
    run()
