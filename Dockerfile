FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /var/www/ghjk34
WORKDIR /var/www/ghjk34

RUN apt-get update
RUN apt-get install -y libpq-dev
RUN apt-get install -y python3-dev gcc

ADD requirements.txt /var/www/ghjk34/
RUN pip install -r requirements.txt

ADD . /var/www/ghjk34/
ADD .env.docker /var/www/ghjk34/.env


RUN python manage.py collectstatic

CMD python manage.py migrate; gunicorn --bind 0.0.0.0:8000 config.wsgi