# README #
Microservice made with python handle to give an standar address service using sepomex

This service has a admin / backoffice active to handle / work with the address data

## How to install
1.- Go to docker folder and exec

```sh
cp .envexample .env
docker-compose up --build -d
./migrations.sh
./manage.sh createsuperuser
./manage.sh seed_sepomex
```

The last one is going to read a txt file and dump it into the database so... it will take some minutes, maybe you should grab a cup of coffe ;)

### Run project ###
1. Go to docker path
2. Execute docker-compose up --build

### Using manage.py ###
1. Go to docker path
2. Find and execute manage.sh {command}, i.e. ./manage.sh createsuperuser

### Manage migrations ###
1. Go to docker path
2. Find and execute migrations.sh

### Create new module ###
1. Go to docker path
2. Find and execute createmodule.sh {name} i.e. ./createmodule.sh address