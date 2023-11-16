#!/bin/bash

echo "==== we run entrypoint ===="
pipenv run python manage.py runserver 0.0.0.0:1213
