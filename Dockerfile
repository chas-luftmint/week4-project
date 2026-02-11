FROM python:3.10-alpine

# Set a working directory inside the container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy actual application code
COPY . .

# Expose standard Flask port
EXPOSE 5000

# Command to run when container starts
CMD ["python", "app.py"]
