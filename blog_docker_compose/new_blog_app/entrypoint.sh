#!/bin/bash

echo "==== migrate ===="
pipenv run python manage.py migrate
echo "==== runserver ===="
pipenv run python manage.py runserver 0.0.0.0:1213
