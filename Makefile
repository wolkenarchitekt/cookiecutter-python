include Makefile.h

EXAMPLE = example

build:  ## Create example from cookiecutter template
	cookiecutter --overwrite-if-exists --no-input --config-file ./sample_config .

# Install act: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
act:
	act

test: test-docker test-virtualenv

test-docker:  ## Test generated example
	$(MAKE) build
	cd $(EXAMPLE) && $(MAKE) docker-build docker-test docker-lint

test-virtualenv:  ## Test generated example
	$(MAKE) build
	cd $(EXAMPLE) && $(MAKE) virtualenv-create virtualenv-test virtualenv-lint virtualenv-autoformat virtualenv-upgrade

upgrade-requirements:  ## Upgrade requirements
	cd $(EXAMPLE) && $(MAKE) virtualenv-upgrade
	cp example/requirements.txt {{cookiecutter.package_name}}/
	cp example/requirements-dev.txt {{cookiecutter.package_name}}/

clean:
	rm -rf $(EXAMPLE)/.venv
	rm -rf $(EXAMPLE)/project.egg-info
	rm -rf $(EXAMPLE)/.pytest_cache
	find $(EXAMPLE) -name "*.pyc" -exec rm {} \;
