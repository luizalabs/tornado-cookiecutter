import os
import json

from project_boilerplate.settings import BASE_DIR


app = None
with open(os.path.join(os.path.dirname(BASE_DIR), 'app.json'), 'r') as content:
    app = json.load(content)

