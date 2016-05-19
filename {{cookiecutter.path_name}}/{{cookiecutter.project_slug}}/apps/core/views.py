import tornado.web


class HomeHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello world")


class DocsHandler(tornado.web.RequestHandler):

    def get(self):
        version = "{}://{}/docs/version/v1.yml".format(self.request.protocol,
                                                       self.request.host)
        self.render("swagger/index.html", version=version)
