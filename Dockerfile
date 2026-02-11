FROM python:3.10-alpine
# Set a working directory inside the container
WORKDIR .

# Copy actual application code
COPY . /app

# Expose standard Flask port (default is 5000) which declares that the container is listening on port 5000, but doesn't make it public
EXPOSE 5000

# Command to run when container starts, runs when you start container from this image. 
CMD ["python", "app.py"]