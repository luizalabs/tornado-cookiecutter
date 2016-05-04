clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage

install-dev:
	@pip install -r project_boilerplate/requirements/development.txt

test:
	@py.test project_boilerplate

provision:
	@ansible 

runserver:
	 @python project_boilerplate/manage.py runserver

