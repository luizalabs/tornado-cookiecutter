import os
import tornado.options

from tornado.ioloop import IOLoop

from tornado.options import options
from tornado.options import define

from .app import make_app


# define port
define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()


def run():
    app = make_app()
    app.listen(options.port)
    print("Starting server on http://127.0.0.1:%s" % options.port)

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
