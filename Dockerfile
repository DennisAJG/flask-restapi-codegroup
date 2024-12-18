# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code and requirements
COPY app/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask application port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
