#! /usr/bin/env bash

# Let the DB start
python /app/scripts/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /app/scripts/initial_data.py

exec uvicorn main:app --host 0.0.0.0 --port 80 --reload
# gunicorn main:app -workers 4 --worker-class uvicorn.workers.UvicornWorker --bind" "0.0.0.0:80
