#!/bin/sh

until cd /app/rssfeedproj
do
    echo "Waiting for server volume..."
done

celery -A rssfeedproj beat -l info
