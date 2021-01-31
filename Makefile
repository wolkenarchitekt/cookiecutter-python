EXAMPLE = example

build:  ## Create example from cookiecutter template
	cookiecutter --overwrite-if-exists --no-input --config-file ./sample_config .

test:  ## Test generated example
	$(MAKE) build
	cd $(EXAMPLE) && $(MAKE) docker-build docker-test virtualenv-create virtualenv-test

clean:
	rm -rf $(EXAMPLE)/.venv
	rm -rf $(EXAMPLE)/project.egg-info
	rm -rf $(EXAMPLE)/.pytest_cache
	find $(EXAMPLE) -name "*.pyc" -exec rm {} \;
