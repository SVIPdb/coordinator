#!/usr/bin/env bash

docker-compose -f docker-compose.yml -f compose_configs/harvester.yml "$@"
