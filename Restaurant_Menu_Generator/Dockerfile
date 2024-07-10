# Use the official Python image from the Docker Hub as the base image
# This ensures we have a consistent Python environment for our application
FROM python:3.11-slim

# Set the working directory in the container to /app
# All subsequent instructions will be run from this directory
WORKDIR /app

# Copy the requirements file into the container at /app
# This step is isolated to leverage Docker's caching mechanism,
# ensuring that the requirements are only re-installed if the requirements.txt file changes
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
# The --no-cache-dir option prevents the caching of package index files
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
# This includes your Streamlit app and any other necessary files
COPY . /app/

# Copy the .env file from the parent directory into the container at /app
COPY .env /app/

# Make port 8501 available to the world outside this container
# Streamlit by default runs on port 8501
EXPOSE 8501

# Run the Streamlit application
# The command specifies the script to run (main.py), 
# sets the server port to 8501, and makes the server accessible from any network interface
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
