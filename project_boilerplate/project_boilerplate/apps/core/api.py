from tornado import gen
from library.handlers import RestHandler 
from restless.preparers import FieldsPreparer


class HealthcheckHandler(RestHandler):
    preparer = FieldsPreparer(fields={
        'message': 'message'
    })

    @gen.coroutine
    def list(self):
        return [{'message': 'Believe I\'m a human'} ] 

