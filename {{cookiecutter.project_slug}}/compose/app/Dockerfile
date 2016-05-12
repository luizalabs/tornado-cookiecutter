FROM python:3.5.1

ENV PYTHONUNBUFFERED 1

COPY ../.../requirements /src/requirements

RUN pip install -r /src/requirements/production.txt

ENTRYPOINT ["entrypoint.sh"]
