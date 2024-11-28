# Use a slim Python base image for smaller size
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker caching
COPY requirements.txt ./

# Install Python dependencies with no cache for smaller image size
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the application code
COPY . .

# Add certificates if necessary (modify path as needed)
COPY certs/rootCA.crt /usr/local/share/ca-certificates/rootCA.crt
RUN chmod 644 /usr/local/share/ca-certificates/rootCA.crt && \
    update-ca-certificates

# Configure environment variables for certificate handling
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# Avoid setting sensitive environment variables directly in the Dockerfile
# Instead, use a .env file and pass it during runtime for secrets like API keys

# Use unbuffered output for better logging in Docker
CMD ["python", "-u", "server.py"]
