import socket

import app

from restless.tnd import TornadoResource as RestlessResource
from restless.exceptions import MethodNotImplemented


class PaginationMixin(object):
    limit = 20
    offset = 1

    def __init__(self):
        self.limit = int(self.request.args.get('limit', self.limit))
        self.offset = int(self.request.args.get('offset', self.offset))

    def get_queryset(self):
        return MethodNotImplemented()

    def list(self):
        qs = self.get_queryset()
        self.paginate(qs)
        return self.objects

    def paginate(self, qs):
        self.objects = qs.paginate(self.limit, self.offset)

    def links(self):
        return {'next': 1}

    def wrap_list_response(self, data):
        response = super(PaginationMixin, self).wrap_list_response(data)
        response['links'] = self.links()

        return response


class MetaMixin(object):

    def meta_context(self, data):
        # if data is object count always be 1
        count = len(data) if isinstance(data, list) else 1
        meta = {
            'name': app.app_info('name'),
            'server': socket.gethostbyname(socket.gethostname()),
            'version': app.app_info('version'),
            'record_count': count
        }
        return meta

    def wrap_list_response(self, data):
        response = super(MetaMixin, self).wrap_list_response(data)

        response['meta'] = self.meta_context(data)
        return response

    def wrap_object_response(self, data):
        response = {
            'object': data,
            'meta': self.meta_context(data)
        }
        return response


class RestHandler(MetaMixin, RestlessResource):

    def wrap_object_response(self, data):
        response = super(RestHandler, self).wrap_object_response(data)
        return response

    def serialize_detail(self, data):
        serialize = super(RestHandler, self).serialize_detail(data)

        final_data = self.serializer.deserialize(serialize)
        return self.wrap_object_response(final_data)
