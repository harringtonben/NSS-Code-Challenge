run_solution:
	python3 scripts/run_solution.py

setup_project:
	python -m venv nss-code-challenge && source nss-code-challenge/bin/activate && pip install -r requirements.txt && pip install -e .
