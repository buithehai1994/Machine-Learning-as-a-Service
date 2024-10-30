# Use Python 3.9-slim as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt from the root of the project to the working directory
COPY ../../requirements.txt ./  # Adjusted path to navigate to the root

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app directory (excluding the Dockerfile itself)
COPY ../../app ./  # Copying the app folder from the root

# Expose the port the app runs on
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
