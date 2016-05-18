#!/usr/bin/env python

import os
import readline
from pprint import pprint

os.environ.setdefault('TORNADO_MODULE_SETTINGS', 'settings.development')

from app import *
from server import *


def make_shell():
    os.environ['PYTHONINSPECT'] = 'True'


def main():
    print('Loading shell...')
    make_shell()

if __name__ == '__main__':
    main()
