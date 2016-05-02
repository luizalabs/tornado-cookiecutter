from tornado.web import URLSpec as url
from .api import HealthcheckHandler

urls = [
    url(r'healthcheck', HealthcheckHandler.as_list()),
    url(r'healthcheck/(?P<pk>[\w]+)', HealthcheckHandler.as_detail()),
]
