.DEFAULT_GOAL := help

.PHONY: run.debug
run.debug:  ## Run the webserver in debug mode.
	poetry run flask --app webserver run --debug

.PHONY: run
run:  ## Run the webserver.
	poetry run flask --app webserver run

.PHONY: lint
lint: flake8 mypy pylint  ## Lint Python source files.

.PHONY: format
format: isort black  ## Format Python source files.

.PHONY: format.check
format.check: isort.check black.check  ## Check if Python sources files should be formatted.

.PHONY: install
install:  ## Install Python dependencies into the virtual environment.
	poetry install

.PHONY: isort
isort:
	poetry run isort webserver/ test/

.PHONY: isort.check
isort.check:
	poetry run isort --check webserver/ test/

.PHONY: black
black:
	poetry run black webserver/ test/

.PHONY: black.check
black.check:
	poetry run black --check webserver/ test/

.PHONY: mypy
mypy:
	poetry run mypy webserver/ test/

.PHONY: pylint
pylint:
	poetry run pylint webserver/ test/

.PHONY: flake8
flake8:
	poetry run flake8 webserver/ test/

# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
