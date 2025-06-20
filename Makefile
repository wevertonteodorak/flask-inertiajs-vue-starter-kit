# use parallel tasks
MAKEFLAGS+="-j 2"

# Variables
VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip

.PHONY: all
all: dev

# run Flask app in development mode
dev-python:
    FLASK_APP=app:app FLASK_DEBUG=1 flask run

# build Vue app in development mode with hot-reload
# this build will be covered in the client-side part
dev-vue:
    @npm --prefix static/ run build:dev

# run development environment
dev: dev-python dev-vue