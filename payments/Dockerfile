# Using the "official" Python base image: Debian OS + Python
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app/

# Copying the entire project, except those mentioned in dockerignore
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Default command (dev mode)
CMD ["python", "src/payments/manage.py", "runserver", "0.0.0.0:8000"]
