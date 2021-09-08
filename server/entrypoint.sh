#!/bin/bash

# Abort on any error (including if wait-for-it fails).
set -e

# Wait for the database to be up, if we know where it is.
if [ -n "$DATABASE_HOST" ]; then
  /wait-for-it.sh "$DATABASE_HOST:${DATABASE_PORT:-5432}"
fi

echo "Database migrations"
python manage.py makemigrations users
python manage.py makemigrations
python manage.py migrate


declare -a commands=("create_user_group")
# now loop through the above array
for cmd in "${commands[@]}"; do
  python manage.py "${cmd}"
done


# Run the main container command.
exec "$@"
