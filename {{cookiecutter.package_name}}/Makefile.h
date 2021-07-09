# Universal Python/Docker development Makefile header, version 0.1

# Convert .env-file to makefile format and export all variables
# to be accessible within make and shell commands
# Variable precedence order:
#   1) Environment variables
#   2) .env.local
#   3) .env
$(shell rm -f /tmp/.make_env)
ifneq ("$(wildcard .env.local)","")
	output := $(shell sed "s/=/ ?= /" .env.local > /tmp/.make_env)
endif
$(shell sed "s/=/ ?= /" .env >> /tmp/.make_env)

# Export variables from merged .env files
include /tmp/.make_env
export

# Pass .env.local to Docker (overwriting variables from .env) if exists
ENV_FILES=--env-file=.env
ifneq ("$(wildcard .env.local)","")
	ENV_FILES=--env-file=.env --env-file=.env.local
endif

MAKEFLAGS=--warn-undefined-variables
.DEFAULT_GOAL := help
DOCKER_TAG  = {{ cookiecutter.docker_container_name }}
VENV = {{ cookiecutter.virtualenv_dir }}
VENV_BIN = $(VENV)/bin
VOLUMES = -v $$(pwd):/code

# Use Dockerfile according to STAGE environment
ifeq ($(STAGE), production)
	DOCKER_BUILD_CMD = docker build -f Dockerfile . -t $(DOCKER_TAG)
endif
ifeq ($(STAGE), development)
	DOCKER_TAG := $(DOCKER_TAG)-dev
	DOCKER_BUILD_CMD = docker build -f Dockerfile.dev . -t $(DOCKER_TAG)
endif
ifeq ($(STAGE), testing)
	DOCKER_TAG := $(DOCKER_TAG)-test
	DOCKER_BUILD_CMD = docker build -f Dockerfile.test . -t $(DOCKER_TAG)
endif

# Allow running pytest with TTY, if present (disabled on CI)
INTERACTIVE:=$(shell [ -t 0 ] && echo 1)
ifdef INTERACTIVE
DOCKER_RUN = docker run --rm -it $(VOLUMES) $(DOCKER_TAG)
else
DOCKER_RUN = docker run --rm $(VOLUMES) $(DOCKER_TAG)
endif

# Extract MAJOR.MINOR python version
PYTHON_VERSION := $(shell cat $(PWD)/.python-version | awk -F \. {'print $$1"."$$2'})

.PHONY: help
help: ## Display this help section
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-38s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean:
	rm -rf .mypy_cache .pytest_cache *.egg-info .pytest_cache

.PHONY: config
config:  ## Show calculated config
	@echo "STAGE: $(STAGE)"
	@echo "Using Docker command: $(DOCKER_CMD)"
	@echo "Using Docker RUN command: $(DOCKER_RUN)"
	@echo "Using Docker container name: $(DOCKER_TAG)"
