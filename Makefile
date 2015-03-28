.PHONY: all test

all: test

test:
	@python test_decorators.py

clean: clean-pyc clean-build

clean-build:
	@rm -rf build
	@rm -rf dist
	@rm -rf Flask_Decorators.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

make-docs:
	$(MAKE) -C docs html

develop:
	@pip install --editable .

install:
	@python setup.py install

.PHONY: release clean clean-pyc develop install clean-build
