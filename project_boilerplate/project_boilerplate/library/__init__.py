import os
import json

from library.conf import BASE_DIR


def app_info(attr):
    meta = dict()
    with open(os.path.join(BASE_DIR, 'app.json'), 'r') as content:
        meta = json.load(content)

    info = meta.get(attr)
    if info:
        return info
    else:
        raise ValueError('App info missing attribute {0} '.format(attr))

