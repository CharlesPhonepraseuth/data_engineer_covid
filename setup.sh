#!/bin/bash

build(){
    docker-compose build --no-cache
}

init-es(){
    docker-compose up elasticsearch es-init-indexer es-init-seeder kibana
}

init-pg(){
    docker-compose up postgres pgadmin pg-init-seeder
}

airflow(){
    docker-compose up postgres-airflow redis airflow-webserver airflow-scheduler airflow-worker airflow-init flower
}

app(){
    docker-compose up notebook dashboard fastapi
}

# the next line calls the function passed as the first parameter to the script.
# the remaining script arguments can be passed to this function.

$1
