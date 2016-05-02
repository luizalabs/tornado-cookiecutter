import os
import json

from ..settings import BASE_DIR


app = None
with open(os.path.join(BASE_DIR, 'app.json'), 'r') as content:
    app = json.load(content)

