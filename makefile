.PHONY: help install test lint format docker-build docker-run clean

help:
	@echo "Project Chimera - Make Commands"
	@echo "install    - Install dependencies"
	@echo "test       - Run tests"
	@echo "lint       - Run linter"
	@echo "format     - Format code"
	@echo "docker-build - Build Docker image"
	@echo "docker-run  - Run Docker container"
	@echo "clean      - Clean up"

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

test-coverage:
	python -m pytest tests/ --cov=research --cov-report=html

lint:
	flake8 research/ tests/ --max-line-length=88

format:
	black research/ tests/

docker-build:
	docker build -t project-chimera .

docker-run:
	docker run -p 8000:8000 project-chimera

clean:
	rm -rf __pycache__ .pytest_cache htmlcov .coverage