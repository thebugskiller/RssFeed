#!/bin/sh

# Wait for the server volume to be ready
until cd /app/rssfeedproj
do
    echo "Waiting for server volume..."
    sleep 2
done

# Wait for the database to be ready and apply migrations
until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

# Run test cases using pytest
echo "Running pytest..."
pytest
TEST_RESULT=$?

# Check if tests passed (exit code 0 means success)
if [ $TEST_RESULT -ne 0 ]; then
    echo "Tests failed. Exiting container."
    exit 1  # Exit with a non-zero status to stop the container
fi

# Collect static files
# python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn rssfeedproj.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4

# The following line is commented out as we're using Gunicorn instead
# python manage.py runserver 0.0.0.0:8000