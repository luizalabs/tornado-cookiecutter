Tornado Cookiecutter
===================

This is a quick cookiecutter to start building apps with Tornado.

## Features

* Tornado 4
* RESTful handler with Restless
* SQLAlchemy ORM pre-configured
* Run tests with pytest
* API documentattion with Swagger
* 12factor based settings via python-dotenv
* Project README template
* Resource provioning with a ansible
* Docker support using docker-compose for development and production
* Procfile and tsuru.yaml dor deploy at Tsuru (Heroku compatible)
* Work with python 3.4.1+
* Apps based at Django apps

## Optional Integrations

* Integration with Sentry for error logging

## Create project ##

Let's pretend you want to create a Tornado Project called "maguire".
First, get Cookiecutter. It's aewsome.

```sh
pip install cookiecutter
```

Now run it against this repo:

**Warning:** project_slug, path_name must be a valid names of our pattern.

Answer the prompts with yout own desired options. For example:
```sh
$ cookiecutter https://github.com/luizalabs/tornado-cookiecutter.git
Cloning into 'tornado-cookiecutter'...
remote: Counting objects: 467, done.
remote: Compressing objects: 100% (214/214), done.
remote: Total 467 (delta 192), reused 467 (delta 192), pack-reused 0
Receiving objects: 100% (467/467), 53.39 KiB | 0 bytes/s, done.
Resolving deltas: 100% (192/192), done.
Checking connectivity... done.
project_name []: maguire
project_slug []: maguire# this field is not required, because it is generate based at a project_name
short_description []: A host description of project README
description []: Description of project. Use at project README
version [0.1.0]:
author []: Matheus Oliveira
repo []:
travis_url [luizalabs/maguire]:
```
Enter the project and take a look around:

```sh
cd maguire
ls
```

Create a git repo and push ir here:

```sh
git init
git add .
git commit -m "first commit"
git remote add origin git@github.com:luizalabs/cookiecutter.git 
git push -u origin master
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

- [ ] logging
- [ ] ansible
- [ ] docker
