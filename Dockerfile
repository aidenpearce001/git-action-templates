# Use an official Python runtime as a parent image
FROM 3.12.1-slim-bookworm

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY service /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
