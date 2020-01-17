all: fmt test build

fmt:
	poetry run isort -y
	poetry run black $(PWD)

test:
	poetry run pytest --black --cov=dashi --flake8 --isort --mypy

build:
	poetry build
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

.PHONY: all fmt test build up down
