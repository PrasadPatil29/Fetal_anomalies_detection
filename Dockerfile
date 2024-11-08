# Use the official Python 3.10 slim base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask application code to the container
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 5000

# Run the Flask app using Gunicorn for better performance
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
