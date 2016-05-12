import tornado.ioloop
import tornado.web

from apps.settings import settings
from apps.urls import urls


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)


def make_app():
    app = Application()
    return app


if __name__ == '__main__':
    make_app()
