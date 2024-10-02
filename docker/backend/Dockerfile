# pull official base image
FROM python:3.12-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./rssfeedproj/requirements.txt /app/
RUN pip install -r requirements.txt
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    curl

ADD ./rssfeedproj /app/rssfeedproj
ADD ./docker /app/docker

RUN chmod +x /app/docker/backend/server-entrypoint.sh
RUN chmod +x /app/docker/backend/worker-entrypoint.sh
RUN chmod +x /app/docker/backend/beat-entrypoint.sh
