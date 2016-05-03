from tornado.web import URLSpec as url
from .api import CustomerHandler


urls = [
    url(r'', CustomerHandler.as_list()),
    url(r'\/(?P<pk>[\d]+)', CustomerHandler.as_detail()),
]

