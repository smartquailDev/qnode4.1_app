FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="smartquail.io"

#COPY ./ssl/qnode41_app.crt /etc/nginx/ssl/qnode0_app.crt
#COPY ./ssl/qnode0_app.key /etc/nginx/ssl/qnode0_app.key
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh


ENV LISTEN_PORT=80
ENV NGINX_PROXY=http://qnode41_app:9000
ENV APP_HOST=qnode41_app
ENV APP_PORT=9000

USER root

RUN mkdir -p /qnode4.1_app/qnode41_app/staticfiles && \
    chmod 755 /qnode4.1_app/qnode41_app/staticfiles && \
    mkdir -p /qnode4.1_app/qnode41_app/media && \
    chmod 755 /qnode4.1_app/qnode41_app/media && \

    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /qnode4.1_app/qnode41_app/staticfiles
VOLUME /qnode4.1_app/qnode41_app/mediafiles

USER nginx
#ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["/run.sh"]