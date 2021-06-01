# Cookiecutter for simple Python application

Cookiecutter scaffold to create minimal Python application.
Features:

* proper module setup with setup.py and requirements.txt
* Prepared for usage with virtualenv and Docker
* Makefile for quick access to all development commands
* bumpversion integration
* preconfigured linting (flake8, mypy)
* preconfigured autoformatter
* Sample Typer CLI module
* preconfigured pytest setup

## Installation

Install cookiecutter:
```
# Globally:
pip install cookiecutter

# Via pipsi (https://github.com/mitsuhiko/pipsi):
pipsi install cookiecutter
```

Create project from template:
```
cookiecutter -o $PROJECT_HOME .
```

## Test

To generate the example - thereby testing the scaffold, run:
```
make build test
```
