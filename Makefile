.PHONY: run.debug
run.debug:
	poetry run flask --app webserver run --debug

.PHONY: run
run:
	poetry run flask --app webserver run

.PHONY: lint
lint: flake8 mypy pylint

.PHONY: format
format: isort black

.PHONY: format.check
format.check: isort.check black.check

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

.PHONY: lint.check
lint.check:
