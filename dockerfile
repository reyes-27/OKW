FROM python:3.12-slim-bullseye

# Set the working directory in docker
WORKDIR /app

ENV PYTHONUNBUFFERED=1
# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]