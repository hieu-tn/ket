#!/bin/sh

# Abort on any error (including if wait-for-it fails).
set -e

# Wait for the database to be up, if we know where it is.
if [ -n "$DATABASE_HOST" ]; then
  /usr/src/app/wait-for-it.sh "$DATABASE_HOST:${DATABASE_PORT:-5432}"
fi

echo "Database migrations"
python manage.py makemigrations
python manage.py migrate

#python manage.py runserver 0:8000 --settings=ket.settings.development

# Run the main container command.
exec "$@"
