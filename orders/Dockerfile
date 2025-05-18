# Using the "official" Python base image: Debian OS + Python
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# We hard-code the Internal Ip of the Payment Service
ENV PAYMENTS_CONTAINER_IP=172.17.0.2
ENV PAYMENTS_CONTAINER_PORT=8000

# Set working directory
WORKDIR /app/

# Copying the entire project except those mentioned in the .dockerignore
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

# [Optional]: Expose Port 8000, stating Django Server will listen on the port 8000 of the container namespace
EXPOSE 8000

# Default command (dev mode)
CMD ["python", "src/orders/manage.py", "runserver", "0.0.0.0:8000"]