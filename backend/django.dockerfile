FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
COPY .  /var/www/
WORKDIR /var/www/backend 
RUN pip install -r requirements.txt
ENTRYPOINT python manage.py runserver 0.0.0.0:8000