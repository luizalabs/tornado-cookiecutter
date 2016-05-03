import os
import sys


if __name__ == '__main__':
    os.environ.setdefault("TORNADO_SETTINGS_MODULE", "project_boilerplate.settings.development")

    from library.execute_from_command_line import execute_from_command_line

    execute_from_command_line(sys.argv)
