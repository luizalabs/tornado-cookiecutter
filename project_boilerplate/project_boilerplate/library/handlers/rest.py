import socket

from library import app_info

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

    @property
    def links(self):
        pass


class MetaMixin(object):
    meta = True

    def meta_context(self, data):
        # if data is object count always be 1
        count = len(data) if isinstance(data, list) else 1
        meta = {
            'name': app_info('name'),
            'server': socket.gethostbyname(socket.gethostname()),
            'version': app_info('version'),
            'recordCount': count 
        }
        return meta


class RestHandler(MetaMixin, RestlessResource):
    links = None

    def initialize(self):
        print(self.headers)

    def default_return(self, data):
        """ Default object return
        """
        response = {}

        if isinstance(data, list): 
            response['objects'] = data
        else:
            response['object'] = self.preparer.prepare(data)

        if self.meta:
            response['meta'] = self.meta_context(data)

        if self.links and isinstance(links, dict):
            response['links'] = self.links

        return response

    def wrap_list_response(self, data):
        return self.default_return(data)

    def serialize_detail(self, data):
        return self.default_return(data)


