#!/bin/sh
docker image rm dev-mysql:1.0 -f  && \
docker build . -t dev-mysql:1.0 && \
docker run --detach --name=dev-mysql --publish 3306:3306 dev-mysql:1.0 && \
docker ps