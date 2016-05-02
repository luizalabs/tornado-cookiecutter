from tornado import gen
from contrib.handlers import RestHandler 
from restless.preparers import FieldsPreparer


class HealthcheckHandler(RestHandler):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'message': 'message'
    })

    @gen.coroutine
    def list(self):
        return [
            { 'id': 1, 'message': 'Hey homosapiens, I\'m alive.' },
            { 'id': 2, 'message': 'Hey homosapiens, I\'m alive.' }
        ]

    @gen.coroutine
    def detail(self, pk):
        return {
            'id': pk,
            'message': 'Matheus'
        }

