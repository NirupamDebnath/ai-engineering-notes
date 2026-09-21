VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
VENV_MKDOCS := $(VENV)/bin/mkdocs
VENV_JUPYTER := $(VENV)/bin/jupyter

.DEFAULT_GOAL := help

.PHONY: help setup build-docs serve-docs notebook

help:
	@echo "Available commands:"
	@echo "  make setup       Create the virtual environment and install all dependencies"
	@echo "  make build-docs  Build the MkDocs site"
	@echo "  make serve-docs  Run the local MkDocs preview server"
	@echo "  make notebook    Start JupyterLab"

setup:
	@if [ ! -x "$(VENV_PYTHON)" ]; then \
		echo "Creating virtual environment in $(VENV)..."; \
		python3 -m venv "$(VENV)"; \
	fi
	$(VENV_PYTHON) -m pip install --upgrade pip
	$(VENV_PYTHON) -m pip install -r requirements.txt

build-docs: setup
	$(VENV_MKDOCS) build --config-file ai-docs/mkdocs.yml --strict

serve-docs: setup
	$(VENV_MKDOCS) serve --config-file ai-docs/mkdocs.yml

notebook: setup
	$(VENV_JUPYTER) lab
