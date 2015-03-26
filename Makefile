.PHONY: all test

all: test

test:
	@python test_decorators.py

clean: clean-pyc

clean-pyc:
	@find . -name '*.pyc' -exec rm {} \;
	@find . -name '__pycache__' -type d | xargs rm -rf

make-docs:
	$(MAKE) -C docs html

develop:
	@pip install --editable .

.PHONY: test release all clean clean-pyc develop
