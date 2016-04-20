from tornado.web import URLSpec as url
from .views import HealthcheckHandler

urls = [
    url(r"healthcheck", HealthcheckHandler),
]
