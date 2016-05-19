UNAME := $(uname -s)

ifeq ($(UNAME), Linux)
	OPEN_CMD ?= xdg-open
endif
ifeq ($(UNAME), Darwin)
	OPEN_CMD ?= open
endif

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage

install-dev:
	@pip install -r requirements/development.txt

test:
	@py.test -x -s -v {{cookiecutter.project_slug}}/apps/

test-coverage:
	@py.test -x -s -v --cov={{cookiecutter.project_slug}}/apps/ --cov-config=.coveragerc --cov-report=term --cov-report=html --cov-report=xml

open-coverage:
	$(OPEN_CMD) htmlcov/index.html

provision:
	@ansible

linter:
	@flake8 --show-source .

shell:
	@python {{cookiecutter.project_slug}}/shell.py

runserver:
	@python {{cookiecutter.project_slug}}/server.py

deploy-sandbox: Realiza deploy no tsuru-nuvemluiza
	@tsuru app-deploy . -a {{ cookiecutter.path_name }}
