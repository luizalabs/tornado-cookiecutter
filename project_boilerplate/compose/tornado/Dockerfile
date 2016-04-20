FROM python:3.5

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["entrypoint.sh"]
