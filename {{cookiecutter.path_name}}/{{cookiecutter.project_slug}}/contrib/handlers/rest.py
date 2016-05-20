import socket

import app

from restless.tnd import TornadoResource as RestlessResource
from restless.exceptions import MethodNotImplemented

from raven import Client

from settings import settings


class PaginationMixin(object):
    limit = 20
    offset = 1

    def get_queryset(self):
        return MethodNotImplemented()

    def list(self):
        qs = self.get_queryset()
        self.paginate(qs)
        return self.objects

    def paginate(self, qs):
        self.objects = qs.limit(self.limit).offset(self.offset)

    def links(self):
        links = {}
        return links

    def wrap_list_response(self, data):
        response = super(PaginationMixin, self).wrap_list_response(data)
        response['links'] = self.links()

        return response


class MetaSchemaMixin(object):

    def hostname(self, use_hostname=False):
        hostname = socket.gethostname()

        if use_hostname:
            return hostname

        return socket.gethostbyname(hostname)

    def data_count(self, data):
        count = 0

        if isinstance(data, list):
            count = len(data)
        else:
            count = 1
        return count

    def meta_schema(self, data):
        schema = {
            'name': app.info('name'),
            'server': self.hostname(),
            'version': app.info('version'),
            'record_count': self.data_count(data)
        }
        return schema


class MetaHandlerMixin(MetaSchemaMixin):

    def set_meta(self, data):
        return self.meta_schema(data)

    def wrap_list_response(self, data):
        response = super(MetaHandlerMixin, self).wrap_list_response(data)

        response['meta'] = self.set_meta(data)
        return response

    def wrap_object_response(self, data):
        response = {
            'meta': self.set_meta(data)
        }
        return response


class SentryRestlessMixin(object):
    sentry_client = Client(settings.SENTRY_DSN)

    def handle_error(self, err):
        self.sentry_client.captureException()
        return super(SentryRestlessMixin, self).handle_error(err)


class BaseHandlerMixin(MetaHandlerMixin, SentryRestlessMixin, PaginationMixin):
    pass


class RestHandler(BaseHandlerMixin, RestlessResource):
    """
    Rest resource handler
    """
    def is_authenticated(self):
        return True

    def wrap_object_response(self, data):
        response = super(RestHandler, self).wrap_object_response(data)

        response['object'] = data
        return response

    def serialize_detail(self, data):
        serialize = super(RestHandler, self).serialize_detail(data)

        final_data = self.serializer.deserialize(serialize)
        return self.wrap_object_response(final_data)
