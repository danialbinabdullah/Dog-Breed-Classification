# Use an official Python runtime as a parent image
FROM python:3.11.4-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy all content from the current directory into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask application
EXPOSE 5000

# Command to run the Flask application and export the model
CMD ["python", "-c", "import dog_breed_identification; dog_breed_identification.export_model(); import app; app.run(host='0.0.0.0', port=5000)"]s