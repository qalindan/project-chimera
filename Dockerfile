FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run tests on build (optional but good practice)
RUN python -m pytest tests/ -v

# Expose port if your app has an API
EXPOSE 8000

# Default command to run tests
CMD ["python", "-m", "pytest", "tests/", "-v"]