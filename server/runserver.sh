#!/bin/bash

python manage.py makemigrations
python manage.py migrate

supervisord -n
