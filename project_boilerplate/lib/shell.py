#!/usr/bin/env python

import os
import readline
from pprint import pprint

def make_shell():
    from lib.server import *

    os.environ['PYTHONINSPECT'] = 'True'

def run():
    print('Loading...')
    make_shell()

if __name__ == '__main__':
    run()
