import os

import tornado.httpserver
import tornado.options

from tornado.options import options
from tornado.options import define 

from dotenv import load_dotenv


# load .env keys
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# define host and port
define("host", default='127.0.0.1', help="run on the given host", type=str)
define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()


def main():
    import app

    server = tornado.httpserver.HTTPServer(app.make_app())
    server.listen(options.port)
    message = "Listening server at http://{0}:{1}"
    print(message.format(options.host, options.port))

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStopping server.")


if __name__ == '__main__':
    main()
