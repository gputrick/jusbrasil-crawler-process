FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
COPY .  /var/www/
WORKDIR /var/www/backend
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT python manage.py migrate && python manage.py runserver 0.0.0.0:8000