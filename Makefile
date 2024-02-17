PYTHON_VERSION = 3.11
BIN = .venv/bin
ACTIVATE = . $(BIN)/activate &&
PYTHON = $(ACTIVATE) python
PIP = $(ACTIVATE) uv pip
COMPILE = $(ACTIVATE) uv pip compile

clean:
	@rm -rfv .venv

setup:
	@uv venv -p $(PYTHON_VERSION)

compile:
	@$(COMPILE) requirements/prod.in -o requirements/prod.txt
	@$(COMPILE) requirements/dev.in -o requirements/dev.txt

install:
	@$(PIP) install -r requirements/dev.txt
	@$(PIP) install -r requirements/prod.txt

format:
	@$(ACTIVATE) ruff format fin

lint:
	@$(ACTIVATE) ruff check fin --fix

run:
	@$(PYTHON) run.py
