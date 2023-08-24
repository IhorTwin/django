# Set up guide

## Install Docker

`https://docs.docker.com/desktop/install/mac-install/`

## To run project use 

`docker compose up`

## Apply migrations 

In a separate terminal tab run:

`docker ps`

Copy web-1 process hash and run

`docker exec -t -i 16229c7118ca bash`

In bash run commands to apply migrations

`python manage.py migrate`

## Create user to access admin panel 

`python manage.py createsuperuser`
