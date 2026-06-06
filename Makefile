PIP = pip
PYTHON = python3
FLAKE8 = flake8
MYPY = mypy
VENV := $(shell $(PYTHON) -c "import os; print(os.getenv('VIRTUAL_ENV') if os.getenv('VIRTUAL_ENV') else '')")
EXCLUDE := $(if $(VENV),--exclude $(VENV),)
CONF_FILE = config.txt
MAIN_FILE = a_maze_ing.py
MLX_WHEEL = mlx-2.2-py3-none-any.whl

all: run

install:
	$(PIP) install $(FLAKE8) $(MYPY)
	$(PIP) install $(MLX_WHEEL)

run: install
	$(PYTHON) $(MAIN_FILE) $(CONF_FILE)

debug:
	$(PYTHON) -m pdb $(MAIN_FILE) $(CONF_FILE)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	
lint: install
	$(PYTHON) -m $(FLAKE8) . $(EXCLUDE)
	$(PYTHON) -m $(MYPY) . \
	--ignore-missing-imports \
	--warn-return-any \
	--warn-unused-ignores \
	--disallow-untyped-defs \
	--check-untyped-defs

.PHONY: install run debug clean lint lint-strict