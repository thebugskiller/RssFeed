#!/bin/sh

until cd /app/rssfeedproj
do
    echo "Waiting for server volume..."
done

celery -A rssfeedproj worker --loglevel=info --concurrency 1 -E
