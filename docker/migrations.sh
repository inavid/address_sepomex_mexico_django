#!/usr/bin/env bash
./manage.sh makemigrations
./manage.sh migrate
#./manage.sh createsuperuser