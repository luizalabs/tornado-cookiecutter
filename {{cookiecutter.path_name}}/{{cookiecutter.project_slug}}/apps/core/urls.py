from tornado.web import URLSpec as url

from .api import HealthcheckHandler

urls = [
    url(r'', HealthcheckHandler.as_list())
]
