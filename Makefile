all: fmt test

fmt:
	poetry run isort -y
	poetry run black $(PWD)

test:
	poetry run pytest --black --cov=dashi --isort --mypy

.PHONY: all fmt test
