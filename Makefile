DATABASE_CONTAINER := ket_db
SERVER_CONTAINER := ket_server
APP_CONTAINER := ket_app
DOCKER_COMPOSE := docker-compose.yml
APP_DIRECTORY := app

ket.server:
	docker compose -f ${DOCKER_COMPOSE} up --build

ket.down:
	docker compose -f ${DOCKER_COMPOSE} down

ket.ssh:
	docker exec -it ${SERVER_CONTAINER} bash

ket.db.ssh:
	docker exec -it ${DATABASE_CONTAINER} bash

ket.lint:
	docker exec -it ${SERVER_CONTAINER} black . -S --diff --color

ket.tasks:
	docker exec -it ${SERVER_CONTAINER} celery -A ket worker -l INFO

ket.app:
	cd ${APP_DIRECTORY} && npm start
