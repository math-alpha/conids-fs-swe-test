FROM node:16.20.0

WORKDIR /code

COPY . .

COPY package*.json ./
RUN cd /code && npm install

EXPOSE 5173
