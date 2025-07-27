# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create input and output folders inside the container
RUN mkdir -p input output

# Command to run your app
CMD ["python", "app.py"]
