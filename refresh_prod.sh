#!/bin/sh

set -e

git pull

docker compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d

docker compose -f docker-compose.prod.yml exec web_prod python manage.py migrate

docker compose -f docker-compose.prod.yml exec web_prod python manage.py collectstatic