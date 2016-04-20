import tornado.web
from tornado import gen
from restless.tnd import TornadoResource


class HomeHandler(TornadoResource):

    @gen.coroutine
    def list(self):
        return []


class HealthcheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Healthcheck")


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test")
