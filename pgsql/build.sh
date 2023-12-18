#!/bin/sh
docker image rm dev-pgsql:1.0 -f && \
docker build . -t dev-pgsql:1.0 && \
docker run --detach --name=dev-pgsql --publish 5432:5432 dev-pgsql:1.0 && \
docker ps