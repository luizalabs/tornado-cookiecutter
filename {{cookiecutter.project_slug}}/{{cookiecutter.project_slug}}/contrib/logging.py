import os
import logging


class LoggingHandler(object):

    def __init__(self, handler=None, template=None):
        self.handler = handler
        self.template = self.init_template(template)

        if not os.getenv('DEBUG'):
            self.load()

    def load(self):
        """ Config logging """

    def init_template(self, template):
        return getattr(self, '{0}_handler'.format(template), 'file')

    def file_hander(self):
        return ''

    def logentries_hander(self):
        return ''
