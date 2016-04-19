Tornado Boilerplate
===================

This is a quick boilerplate to start building apps with Tornado.
It has an almost similar organization of a Django project, as most people are
familar with it. This is how it looks -

    .
    ├── server.py
    ├── {{project_name}}
    │   ├── __init__.py
    │   └── core
    │       ├── __init__.py
    │       ├── urls.py
    │       └── views.py
    ├── __init__.py
    ├── settings.py
    ├── static
    │   └── style.css
    ├── templates
    │   ├── base.html
    │   └── home.html
    └── urls.py


## Settings ##
Settings as a dictionary, with full reference

    settings = {
        # debug: If True the application runs in debug mode
        'debug': True,

        ...
    }

***
## Shell ##
Added shell to play with the system

    (venv) ~/Works/tornado-boilerplate/project$ python shell.py
    >>> import tornado.web
    >>>

***
## Apps ##
Added apps folder to separate logic in modules

***
## Importing urls ##
Enabled importing/including urls from different apps, coretaing pattern

    from tornado.web import URLSpec as url

    urls = [
        url(r"/", HomeHandler),
        url(r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
    ]
    # this will include patterns from urls.py inside `core` app.
    urls += include(r"/core/", "{{project_name}}.core.urls")

`/{{project_name}}/core/urls.py`

    from tornado.web import URLSpec as url

    urls = [
        url(r"test/", TestHandler),  # This is `/core/test/`
    ]

***
## Server start/stop message ##
Showing message when starting and stoping the server

    (venv) ~/Works/tornado-boilerplate/project$ python server.py
    Starting server on http://127.0.0.1:8888
    ^C
    Stopping server.
