import os
import json

import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import options
from tornado.options import define

from apps.urls import urls

from settings import settings


class Application(tornado.web.Application):
    settings = {
        'debug': bool(settings.DEBUG),
        'gzip': settings.GZIP,
        'cookie_secret': settings.SECRET_KEY,
        'xsrf_cookies': True,
        'autoescape': "xhtml_escape",
        'template_path': settings.TEMPLATE_ROOT,
        'static_path': settings.STATIC_ROOT,
        'static_url_prefix': settings.STATIC_URL,
    }

    def __init__(self):
        tornado.web.Application.__init__(self, urls, **self.settings)


def make_app():
    app = Application()
    return app


# define host and port
# define("host", default='127.0.0.1', help="run on the given host", type=str)
# define("port", default=8888, help="run on the given port", type=int)
# tornado.options.parse_command_line()


def run():
    os.environ.setdefault('TORNADO_SETTINGS_MODULE', 'settings.development')

    app = make_app()
    app.listen(options.port)
    message = "Listening server at http://{0}:{1}"
    print(message.format(options.host, options.port))

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStopping server.")


def get_server_application():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(int(os.getenv('PORT', 8888)))
    server.start(0)
    IOLoop.current().start()


if __name__ == '__main__':
    run()
