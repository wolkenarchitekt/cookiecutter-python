MAKEFLAGS=--warn-undefined-variables
.PHONY: help
.DEFAULT_GOAL := help
CONTAINER  = {{ cookiecutter.docker_container_name }}
VENV = {{ cookiecutter.virtualenv_dir }}
VENV_BIN = $(VENV)/bin
VOLUMES = -v $$(pwd):/code

# Allow running pytest with TTY, if present (disable on CI)
INTERACTIVE:=$(shell [ -t 0 ] && echo 1)
ifdef INTERACTIVE
DOCKER_RUN = docker run --rm -it $(VOLUMES) $(CONTAINER)
else
DOCKER_RUN = docker run --rm $(VOLUMES) $(CONTAINER)
endif

# Extract MAJOR.MINOR python version
PYTHON_VERSION := $(shell cat $(PWD)/.python-version | awk -F \. {'print $$1"."$$2'})


help: ## Display this help section
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean:
	rm -rf .mypy_cache .pytest_cache *.egg-info .pytest_cache

# Install act: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
act:
	act

test: docker-build docker-test

autoformat: virtualenv-autoformat

docker-clean:
	-docker stop $(CONTAINER)
	-docker rm -f $(CONTAINER)

docker-build:  ## Build Docker container
	docker build -t $(CONTAINER) .

docker-run:  ## Run Docker container
	$(DOCKER_RUN)

docker-shell:  ## Run Docker shell
	$(DOCKER_RUN) bash

docker-test:
	$(DOCKER_RUN) pytest

docker-ipython:
	$(DOCKER_RUN) ipython

docker-lint:
	$(DOCKER_RUN) flake8 {{cookiecutter.module_name}}
	$(DOCKER_RUN) mypy {{cookiecutter.module_name}}


$(VENV): requirements.txt requirements-dev.txt setup.py
	python$(PYTHON_VERSION) -m venv $(VENV)
	$(VENV_BIN)/pip install --upgrade pip setuptools && \
	$(VENV_BIN)/pip install -r requirements.txt && \
	$(VENV_BIN)/pip install -r requirements-dev.txt && \
	$(VENV_BIN)/pip install -e .
	touch $(VENV)

virtualenv-create:
	rm -rf $(VENV)
	$(MAKE) $(VENV)

virtualenv-autoformat:
	$(VENV_BIN)/autoformat {{cookiecutter.module_name}}

virtualenv-shell:
	$(VENV_BIN)/ipython

virtualenv-test:
	$(VENV_BIN)/pytest

virtualenv-lint:
	$(VENV_BIN)/flake8 {{cookiecutter.module_name}}
	$(VENV_BIN)/mypy {{cookiecutter.module_name}}

virtualenv-upgrade:
	$(VENV_BIN)/pur -r requirements.txt
	$(VENV_BIN)/pur -r requirements-dev.txt


readme-convert-markdown-rst:
	# Needs pandoc to be installed on host
	pandoc --from=markdown --to=rst --output=README.rst README.md

pypi-upload:
	rm -rf dist
	$(VENV_BIN)/python setup.py sdist
	$(VENV_BIN)/twine upload dist/*

bumpversion-patch:
	$(VENV_BIN)/bump2version patch

bumpversion-minor:
	$(VENV_BIN)/bump2version minor

bumpversion-major:
	$(VENV_BIN)/bump2version major
