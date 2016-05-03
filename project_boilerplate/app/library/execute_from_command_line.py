import library.server
# import library.shell
import library.test

from tornado.options import define
from tornado.options import options


COMMANDS = ['runserver', 'test', 'shell']


class BaseCommands(object):

    def __init__(self, *commands):
        self.command_arg = commands[0]
        self.options = commands[1::]

        self.command = self.get_command()

    def execute(self):
        self.command()

    def get_command(self):
        return getattr(self, self.command_arg)

    def runserver(self):
        library.server.run()

    # def shell(self):
    #     library.shell.run()

    def test(self):
        library.test.run()


class Management(object):

    def __init__(self, commands):
        self.command = commands[0]
        self.params = commands[1::]

        self.command = self.commands()

    def commands(self):
        return BaseCommands(self.command, self.params)

    def execute(self):
        self.command.execute()


def execute_from_command_line(args):
    utility = Management(args[1::])
    utility.execute()
