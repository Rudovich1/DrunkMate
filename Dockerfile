# pull official base image
FROM python:3.10.8-slim-buster

# set working directory
WORKDIR /usr/src/drunkMate

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ALGORITHM HS256
ENV SECRET_KEY 5d2ffd99e383e08cff1c93ce88e36ffb88633dcd0950b8fb887b1c4588ad3564

# install system dependencies
RUN apt-get update && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-root

# add app
COPY . .
