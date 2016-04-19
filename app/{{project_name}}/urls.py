from tornado import web
from tornado.web import URLSpec as url
from lib.utils import include

from {{project_name}}.settings import settings

from {{project_name}}.core.views import HomeHandler

urls = [
    url(r"/", HomeHandler.as_list()),
    url(r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
]
urls += include(r"/", "{{project_name}}.core.urls")
