FROM python:3.5.1

ENV PYTHONUNBUFFERED 1

COPY ../.../app/requirements /app/requirements

RUN pip install -r /app/requirements/production.txt

ENTRYPOINT ["entrypoint.sh"]
