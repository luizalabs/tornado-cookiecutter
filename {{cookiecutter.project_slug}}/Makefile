clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage

install-dev:
	@pip install -r {{cookiecutter.project_slug}}/requirements/development.txt

test:
	@py.test {{cookiecutter.project_slug}}/apps

provision:
	@ansible 

runserver:
	 @python {{cookiecutter.project_slug}}/manage.py runserver

