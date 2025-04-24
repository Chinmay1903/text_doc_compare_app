# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend project
COPY backend/ .

# Expose the port
EXPOSE 8000

# Start Django app using gunicorn
CMD ["gunicorn", "docs_compare_app.wsgi:application", "--bind", "0.0.0.0:8000"]
