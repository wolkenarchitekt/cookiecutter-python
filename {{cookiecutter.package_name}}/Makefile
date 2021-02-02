.PHONY: help
.DEFAULT_GOAL := help
CONTAINER  = {{ cookiecutter.docker_container_name }}
VIRTUALENV_DIR = {{ cookiecutter.virtualenv_dir }}
VOLUMES = -v $$(pwd):/code
DOCKER_RUN = docker run --rm -it $(VOLUMES) $(CONTAINER)

# Extract MAJOR.MINOR python version 
PYTHON_VERSION := $(shell cat $(PWD)/.python-version | awk -F \. {'print $$1"."$$2'})


# Print help by extracting ##-comments per target
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


act:
	act


docker-clean:
	-docker stop $(CONTAINER)
	-docker rm -f $(CONTAINER)

docker-build:  ## Build Docker container
	docker build -t $(CONTAINER) .

docker-run:  ## Run Docker container
	$(DOCKER_RUN)

docker-shell:  ## Run Docker shell
	$(DOCKER_RUN) bash

docker-test test:
	$(DOCKER_RUN) pytest

docker-ipython:
	$(DOCKER_RUN) ipython

docker-lint:
	$(DOCKER_RUN) flake8 {{cookiecutter.package_name}}


virtualenv-create:
	python$(PYTHON_VERSION) -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		pip install --upgrade pip setuptools && \
		pip install -r requirements.txt && \
		pip install -r requirements-dev.txt && \
		pip install -e .
	@echo "Activate virtualenv:\n. $(VIRTUALENV_DIR)/bin/activate"

virtualenv-autoformat:
	. $(VIRTUALENV_DIR)/bin/activate && ./autoformat.sh $$(find {{cookiecutter.package_name}}/ -name "*.py" -printf "%p ")

virtualenv-shell:
	. $(VIRTUALENV_DIR)/bin/activate && ipython

virtualenv-test:
	. $(VIRTUALENV_DIR)/bin/activate && pytest

virtualenv-lint:
	. $(VIRTUALENV_DIR)/bin/activate && \
		flake8 {{cookiecutter.package_name}} && \
		mypy {{cookiecutter.package_name}}


readme-convert-markdown-rst:
	. $(VIRTUALENV_DIR)/bin/activate && pandoc --from=markdown --to=rst --output=README.rst README.md
