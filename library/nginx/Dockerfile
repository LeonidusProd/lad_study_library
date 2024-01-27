FROM nginx:alpine

WORKDIR /app

RUN rm /etc/nginx/conf.d/default.conf
COPY django.conf /etc/nginx/conf.d