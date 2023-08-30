#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 1
    done
    sleep 3
    echo "PostgreSQL started"
fi

# python manage.py dumpdata > fixtures.json # сохранение фикстур
python manage.py migrate
# python manage.py flush --no-input
python manage.py loaddata fixtures.json --skip-checks

exec "$@"