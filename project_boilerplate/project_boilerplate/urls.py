from tornado import web
from tornado.web import URLSpec as url
from lib.urls import include

from project_boilerplate.settings import settings

from project_boilerplate.core.views import HomeHandler

urls = [
    url(r"/", HomeHandler.as_list()),
    url(r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
]
urls += include(r"/", "project_boilerplate.core.urls")
