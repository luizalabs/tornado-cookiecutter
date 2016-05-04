clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage

install-dev:
	@pip install -r app/requirements/development.txt

test:
	@py.test app

provision:
	@ansible 

runserver:
	 @python app/manage.py runserver

