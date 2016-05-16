from tornado import gen

from restless.preparers import FieldsPreparer

from contrib.handlers import RestHandler

from .models import Customer


class CustomerHandler(RestHandler):
    model = Customer
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at'
    })

    @gen.coroutine
    def list(self):
        customers = self.model.query.slice(0, 10)
        return customers

    @gen.coroutine
    def detail(self, id):
        customer = self.model.get_or_404(id)
        return customer
