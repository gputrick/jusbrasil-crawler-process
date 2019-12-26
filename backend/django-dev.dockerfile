FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]