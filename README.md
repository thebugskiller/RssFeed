# RSS Feed Project

This project consists of a Django backend and a React frontend for an RSS feed application.

## Directory Structure

```
Main Folder
├── rssapp (frontend)
└── rssfeedproj (backend Django project)
    └── rssfeed (Django app)
```

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

## Running the Project

There are two ways to run the project:

### 1. Using Docker

a. Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)

b. Open a terminal, navigate to the main directory, and run:

```bash
docker compose up
```

The frontend will run on http://localhost:3000/ and the backend endpoints will be available at http://localhost:8000.

### 2. Manual Setup

#### Backend Setup

a. Install Redis: [Redis Installation Guide](https://redis.io/docs/getting-started/installation/)

b. Install Postgres: [Postgres Installation Guide](https://www.postgresql.org/download/)

c. Navigate to the backend directory:

```bash
cd rssfeedproj
```

d. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

e. Install dependencies:

```bash
pip install -r requirements.txt
```

f. Run Celery worker:

```bash
celery -A rssfeedproj worker -l info
```

g. In a new terminal, run Celery beat:

```bash
celery -A rssfeedproj beat -l info
```

h. In a new terminal, Run the Django server:

```bash
python manage.py runserver
```

i. You can run test cases using this command in 'rssfeedproj' directory:

```bash
pytest
```

j. Verify that the backend is running by accessing these URLs:
- http://localhost:8000/api/rss-feed/esp/
- http://localhost:8000/api/rss-feed/en/

#### Frontend Setup

a. Navigate to the frontend directory:

```bash
cd rssapp
```

b. Install dependencies:

```bash
npm install
```

c. Start the frontend server:

```bash
npm start
```

d. Verify that the frontend is running by accessing:
- http://localhost:3000/

