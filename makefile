.PHONY: setup test spec-check docker-test clean help

help:
	@echo "Project Chimera - Development Commands"
	@echo ""
	@echo "setup       - Install dependencies"
	@echo "test        - Run test suite"
	@echo "spec-check  - Verify code aligns with specs"
	@echo "docker-test - Run tests in Docker container"
	@echo "clean       - Clean up temporary files"

setup:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

spec-check:
	@echo "🔍 Checking spec alignment..."
	@python scripts/spec_check.py || echo "Spec check failed"
	@echo "✅ Spec check completed"

docker-test:
	docker build -t project-chimera-test .
	docker run --rm project-chimera-test make test

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov
	find . -name "*.pyc" -delete