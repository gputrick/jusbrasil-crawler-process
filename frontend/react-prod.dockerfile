FROM node:12.2.0-alpine
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
RUN npm install -g serve
ENTRYPOINT serve -s build