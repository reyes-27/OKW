# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim



# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Install pip requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app

# ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]