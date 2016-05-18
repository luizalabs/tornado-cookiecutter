# Tree view

Overview architecture

    .
    ├── README.md
    ├── cookiecutter.json
    ├── docs
    │   └── tree.md
    └── {{cookiecutter.path_name}}
        ├── Makefile
        ├── Procfile
        ├── README.md
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
        ├── header.png
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
            ├── __pycache__
            │   └── app.cpython-35.pyc
            ├── app.py
            ├── apps
            │   ├── __init__\ .py
            │   ├── __init__.py
            │   ├── __pycache__
            │   │   ├── __init__.cpython-35.pyc
            │   │   └── urls.cpython-35.pyc
            │   ├── core
            │   │   ├── __init__.py
            │   │   ├── __pycache__
            │   │   │   ├── __init__.cpython-35.pyc
            │   │   │   ├── api.cpython-35.pyc
            │   │   │   ├── urls.cpython-35.pyc
            │   │   │   └── views.cpython-35.pyc
            │   │   ├── api.py
            │   │   ├── models.py
            │   │   ├── tests
            │   │   │   ├── __init__.py
            │   │   │   └── test_handlers.py
            │   │   ├── urls.py
            │   │   └── views.py
            │   ├── customers
            │   │   ├── __init__.py
            │   │   ├── __pycache__
            │   │   │   ├── __init__.cpython-35.pyc
            │   │   │   ├── api.cpython-35.pyc
            │   │   │   ├── models.cpython-35.pyc
            │   │   │   └── urls.cpython-35.pyc
            │   │   ├── api.py
            │   │   ├── models.py
            │   │   ├── tests
            │   │   │   ├── __init__.py
            │   │   │   ├── test_api.py
            │   │   │   └── test_models.py
            │   │   ├── urls.py
            │   │   └── views.py
            │   └── urls.py
            ├── conftest.py
            ├── contrib
            │   ├── __init__.py
            │   ├── __pycache__
            │   │   ├── __init__.cpython-35.pyc
            │   │   ├── db.cpython-35.pyc
            │   │   └── urls.cpython-35.pyc
            │   ├── db.py
            │   ├── execute_from_command_line.py
            │   ├── handlers
            │   │   ├── __init__.py
            │   │   ├── __pycache__
            │   │   │   ├── __init__.cpython-35.pyc
            │   │   │   └── rest.cpython-35.pyc
            │   │   ├── exceptions.py
            │   │   └── rest.py
            │   ├── logging.py
            │   ├── shell.py
            │   ├── tests
            │   │   ├── __init__.py
            │   │   └── db_test.py
            │   └── urls.py
            ├── pytest.ini
            ├── rename-as.env
            ├── server.py
            ├── settings
            │   ├── __init__.py
            │   ├── __pycache__
            │   │   ├── __init__.cpython-35.pyc
            │   │   ├── base.cpython-35.pyc
            │   │   └── development.cpython-35.pyc
            │   ├── base.py
            │   ├── development.py
            │   ├── production.py
            │   └── test.py
            ├── shell.py
            ├── static
            │   └── style.css
            └── templates
                ├── base.html
                └── home.html
    
