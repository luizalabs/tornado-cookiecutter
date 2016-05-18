from tornado import gen

from restless.preparers import FieldsPreparer

from contrib.handlers import RestHandler


class HealthcheckHandler(RestHandler):
    preparer = FieldsPreparer(fields={
        'message': 'message'
    })

    @gen.coroutine
    def list(self):
        return [{'message': 'Believe I\'m a human'}]
