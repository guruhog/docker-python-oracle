#!/usr/bin/env bash
#docker run -it --rm -p 80:5000 --name web -v /repos/docker/docker-python-oracle/api:/opt/
#docker run -it --rm -d -p 80:5000 --name web -v /Users/guruhog/docker/docker-python-oracle/api:/opt/data/api web
docker run -it --rm -p 80:5000 --name web -v /Users/guruhog/docker/docker-python-oracle/api:/opt/data/api web bash