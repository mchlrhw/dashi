all: fmt test build

fmt:
	poetry run isort -y
	poetry run black $(PWD)

test:
	poetry run pytest --black --cov=dashi --isort --mypy

build:
	poetry build
	docker-compose build

.PHONY: all fmt test build
