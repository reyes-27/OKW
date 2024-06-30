# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12.4-slim-bullseye

EXPOSE 8000 8080
WORKDIR /usr/src/app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


COPY . /usr/src/app

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x ./entrypoint.sh