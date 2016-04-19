install-dev:
    @pip install -r app/requirements/requirements.txt

runserver:
    @python app/manage.py runserver
