# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install s3cmd
RUN apt-get update && \
    apt-get install -y s3cmd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your Python script from localhost to the container
COPY arvan.py /app/
COPY s3cfg /app/

# Run your Python script when the container starts
CMD ["python3", "listObjects.py"]