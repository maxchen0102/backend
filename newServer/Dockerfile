# Use the official Python 3.8 image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install -e .

EXPOSE 6543

# Define the command to run your application
CMD ["pserve", "development.ini"]

