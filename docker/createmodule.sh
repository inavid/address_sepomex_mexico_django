#!/usr/bin/env bash
docker-compose exec web mkdir src/modules/$@
docker-compose exec web python manage.py startapp $@ src/modules/$@