#!/bin/bash

clear_docker(){
    docker-compose down

    docker rm -f $(docker ps -a -q)
    docker image rm $(docker image ls -q)
    docker volume rm $(docker volume ls -q)

    docker image ls
    docker volume ls
    docker container ls
    docker network ls
}

clear_docker
