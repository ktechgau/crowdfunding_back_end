#!/usr/bin/env bash
python3 manage.py migrate
python3 manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 crowdfunding.wsgi