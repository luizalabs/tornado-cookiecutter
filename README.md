Tornado Cookiecutter
===================

This is a quick cookiecutter to start building apps with Tornado.
It has an almost similar organization of a Django project, as most people are
familar with it. This is how it looks -

    .
    ├── Makefile
    ├── Procfile
    ├── Vagrantfile
    ├── ansible
    │   ├── inventory
    │   │   ├── production
    │   │   └── staging
    │   ├── production.yml
    │   ├── roles
    │   │   ├── app
    │   │   │   └── tasks
    │   │   │       └── main.yml
    │   │   ├── common
    │   │   │   └── tasks
    │   │   │       └── main.yml
    │   │   ├── nginx
    │   │   │   ├── tasks
    │   │   │   │   └── main.yml
    │   │   │   └── templates
    │   │   │       └── nginx.cnf.j2
    │   │   ├── python
    │   │   │   └── tasks
    │   │   │       └── main.yml
    │   │   └── supervisor
    │   │       ├── tasks
    │   │       │   └── main.yml
    │   │       └── templates
    │   │           └── supervisord.cnf.j2
    │   ├── staging.yml
    │   └── vars
    │       ├── development.yml
    │       ├── main.yml
    │       ├── production.yml
    │       └── sandbox.yml
    ├── app.json
    ├── compose
    │   ├── app
    │   │   ├── Dockerfile
    │   │   └── entrypoint.sh
    │   └── nginx
    │       ├── Dockerfile
    │       └── entrypoint.sh
    ├── docker-compose.yml
    ├── requirements
    │   ├── base.txt
    │   ├── development.txt
    │   └── production.txt
    ├── requirements.apt
    ├── requirements.txt
    ├── runtime.txt
    ├── tsuru.yml
    └── {{cookiecutter.project_slug}}
        ├── __init__.py
        ├── apps
        │   ├── __init__\ .py
        │   ├── core
        │   │   ├── __init__.py
        │   │   ├── api.py
        │   │   ├── models.py
        │   │   ├── tests
        │   │   │   ├── __init__.py
        │   │   │   └── test_handlers.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── customers
        │   │   ├── __init__.py
        │   │   ├── api.py
        │   │   ├── models.py
        │   │   ├── tests
        │   │   │   ├── __init__.py
        │   │   │   └── test_api.py
        │   │   ├── urls.py
        │   │   └── views.py
        │   ├── server.py
        │   ├── settings.py
        │   └── urls.py
        ├── conftest.py
        ├── contrib
        │   ├── __init__.py
        │   ├── app.py
        │   ├── db.py
        │   ├── execute_from_command_line.py
        │   ├── handlers
        │   │   ├── __init__.py
        │   │   ├── exceptions.py
        │   │   └── rest.py
        │   ├── logging.py
        │   ├── server.py
        │   ├── shell.py
        │   ├── test.py
        │   ├── tests
        │   │   ├── __init__.py
        │   │   └── db_test.py
        │   └── urls.py
        ├── manage.py
        ├── pytest.ini
        ├── rename-as.env
        ├── static
        │   └── style.css
        └── templates
            ├── base.html
        └── home.html

## Create project ##

Before create your project please install cookiecutter
```sh
pip install cookiecutter
```

With cookiecutter installed make your project
```sh
$ cookiecutter https://github.com/luizalabs/tornado-cookiecutter.git
Cloning into 'tornado-cookiecutter'...
remote: Counting objects: 467, done.
remote: Compressing objects: 100% (214/214), done.
remote: Total 467 (delta 192), reused 467 (delta 192), pack-reused 0
Receiving objects: 100% (467/467), 53.39 KiB | 0 bytes/s, done.
Resolving deltas: 100% (192/192), done.
Checking connectivity... done.
project_name []:
project_slug []: # this field is not required, because it is generate based at a project_name
short_description []:
description []: # short description to your project
version [0.1.0]:
author []:
repo []:
travis_url [luizalabs/]:
```

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

    (venv) ~/Works/tornado-cookiecutter$ make shell
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

    (venv) ~/Works/tornado-cookiecutter$ make runserver
    Listening server at http://127.0.0.1:8888
    ^C
    Stopping server.
=======

## TODO

- [] logging
- [] sentry
- [] swagger
