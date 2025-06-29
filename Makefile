# use parallel tasks
MAKEFLAGS+="-j 2"

# Variables
VENV_DIR=.venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip

.PHONY: all
all: dev

dev-python:
	FLASK_APP=app:app FLASK_DEBUG=1 $(VENV_DIR)/bin/flask run

dev-vue:
	@npm --prefix static/ run dev 

# run development environment
dev: dev-python dev-vue