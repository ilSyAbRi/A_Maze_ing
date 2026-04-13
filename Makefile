PIP = pip

PYTHON = python3



install:
	$(PIP) install 

run:
	$(PYTHON) a_maze_ing.py config.txt

debug:
	$(PYTHON) -m pdb a_maze_ing.py config.txt

clean:
	find . -type f -name "*.pyc" 

.PHONY: install run debug
