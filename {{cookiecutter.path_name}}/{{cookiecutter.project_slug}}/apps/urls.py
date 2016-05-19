from tornado import web
from tornado.web import URLSpec as url

from contrib.urls import include

from settings import settings

from apps.core.views import HomeHandler
from apps.core.views import DocsHandler


urls = [
    url(r"/", HomeHandler),
    url(r"/docs", DocsHandler),
    url(r"/docs/version/(.*)", web.StaticFileHandler,
        {"path": settings.DOCS_ROOT}),
    url(r"/static/(.*)", web.StaticFileHandler,
        {"path": settings.STATIC_ROOT})
]

urls += include(r"/healthcheck", "apps.core.urls")
urls += include(r"/customers", "apps.customers.urls")
