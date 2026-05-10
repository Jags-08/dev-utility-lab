.PHONY: setup test lint mypy run dashboard docker-build docker-run clean

setup:
	pip install -e ".[dashboard]"
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=dev_utils --cov=dashboard

lint:
	ruff check dev_utils/ dashboard/ tests/

mypy:
	mypy dev_utils/ dashboard/ tests/

run:
	dev-utils --help

dashboard:
	FLASK_APP=dashboard.app FLASK_ENV=development flask run

docker-build:
	docker build -t dev-utility-lab:latest .

docker-run:
	docker run -p 5000:5000 dev-utility-lab:latest

clean:
	rm -rf .pytest_cache .coverage .ruff_cache __pycache__ **/__pycache__ build dist *.egg-info
