from tornado import gen
from contrib.handlers import RestHandler 
from restless.preparers import FieldsPreparer

from .models import Customer 


class CustomerHandler(RestHandler):
    model = Customer 
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name'
    })

    @gen.coroutine
    def list(self):
        customers = self.model.query.slice(0, 10)
        return customers 

    @gen.coroutine
    def detail(self, pk):
        customer = self.model.get_or_404(pk)
        return customer

