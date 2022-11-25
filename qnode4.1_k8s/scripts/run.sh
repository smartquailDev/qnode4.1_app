#!/bin/sh

set -e
neofetch --ascii qnode_art.txt --ascii_colors 2 222 3 2 2 -L, --logo && \
#go get github.com/mailhog/mhsendmail && \
#cp /root/go/bin/mhsendmail /usr/bin/mhsendmail && \
#echo 'sendmail_path = /usr/bin/mhsendmail --smtp-addr mailhog:1025' > /usr/local/etc/php/php.ini

APP_PORT=${PORT:-9000}
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"smartquail.info@gmail.com"}


python manage.py migrate --noinput
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
python manage.py collectstatic --noinput 
#python manage.py makemessages
#python django-admin makemessages --all
#python django-admin compilemessages 


uwsgi --http 0.0.0.0:9000 --workers 9 --master --enable-threads --module qnode41_app.wsgi --ini uwsgi_prod.ini

#python manage.py listen_port25 --noinput

#gunicorn --worker-tmp-dir /dev/shm  --bind "0.0.0.0:${APP_PORT}"  qnode0_app.wsgi:application 