include Makefile.h

# Install act: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
act:
	act

test: docker-build docker-test

autoformat: virtualenv-autoformat

docker-clean:
	-docker stop $(DOCKER_TAG)
	-docker rm -f $(DOCKER_TAG)

docker-build:  ## Build Docker container
	$(DOCKER_BUILD_CMD)

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
