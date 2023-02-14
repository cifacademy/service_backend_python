FROM python:3.9.14-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget git libgl1 libglib2.0-0 curl unzip iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Set the working directory
WORKDIR /app

# Set the default command for run the application
CMD ["bash"]
