install-dev:
	@pip install -r requirements.txt

runserver:
	@python app/manage.py runserver
