FROM node:12.2.0-alpine
COPY .  /var/www
WORKDIR /var/www/frontend
RUN npm install
ENTRYPOINT npm start