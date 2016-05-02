from tornado import web
from tornado.web import URLSpec as url
from contrib.urls import include

from project_boilerplate.settings import settings

from project_boilerplate.core.views import HomeHandler

urls = [
    url(r"/", HomeHandler),
    url(r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
]

urls += include(r"/", "project_boilerplate.core.urls")

