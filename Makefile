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

install-fe:
	@npm --prefix static/ install

install-be:
	@python3 -m venv $(VENV_DIR)
	@$(PIP) install -r requirements.txt
	FLASK_APP=app:app FLASK_DEBUG=1 $(VENV_DIR)/bin/flask db:migrate

# run development environment
dev: dev-python dev-vue

# install both front-end and back-end dependencies
install: install-fe install-be