# Use python:3.9-alpine as the base image
FROM python:3.9-alpine

# Install system dependencies required for psycopg2-binary
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libpq \
    python3-dev \
    libc-dev

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port 5000 for Flask application
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
