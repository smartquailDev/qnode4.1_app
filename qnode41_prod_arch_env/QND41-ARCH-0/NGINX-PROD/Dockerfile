FROM nginx:1.23.0-alpine

COPY ./nginx/* /etc/nginx/
COPY ./nginx/run.sh /run.sh
#COPY ./smartquail.io/* /etc/letsencrypt/live/smartquail.io


ENV LISTEN_PORT=80
ENV NGINX_PROXY=http://qnode41_app:9000
ENV APP_HOST=qnode41_app
ENV APP_PORT=9000

USER root

RUN apk add --no-cache openssl bash
RUN chmod +x /run.sh

RUN mkdir -p /qnode4.1_app/qnode41_app/staticfiles && \
    chmod 755 /qnode4.1_app/qnode41_app/staticfiles && \
    mkdir -p /qnode4.1_app/qnode41_app/mediafiles && \
    chmod 755 /qnode4.1_app/qnode41_app/mediafiles && \
    mkdir -p /qnode4.1_app/qnode41_app/media && \
    chmod 755 /qnode4.1_app/qnode41_app/media 

VOLUME /qnode4.1_app/qnode41_app/staticfiles
VOLUME /qnode4.1_app/qnode41_app/mediafiles
VOLUME /vol/www
VOLUME /vol/proxy
VOLUME /etc/letsencrypt

CMD ["/run.sh"]