run_solution:
	poetry run python scripts/run_solution.py

check_solution:
	poetry run pytest tests/check_solution.py::test_check_solution -s -vvv

setup_project:
	pip install poetry
	poetry install
