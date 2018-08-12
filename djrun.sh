#!/bin/sh
# Shell script to run shell command in django container
docker-compose -f local.yml run --rm django $@
