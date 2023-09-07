# Use the base Python image
FROM python:3.9-slim

# Update and install additional OS packages if needed
RUN apt-get update && apt-get -y install --no-install-recommends \
   gcc

# Create a non-root user (optional but recommended)
ARG USER="ashley"
RUN useradd -m -s /bin/bash ${USER}

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY requirements.txt Makefile ./
COPY ./hugohu_pandas_package /app/hugohu_pandas_package
COPY ./data /app/data

# Install dependencies
# Do not care about the warning message as this is running in the docker container
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

# Switch to the non-root user (optional but recommended)
USER ${USER}

# Specify the command to run your application
CMD ["python", "-m", "hugohu_pandas_package"]
