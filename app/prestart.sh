#! /usr/bin/env bash

# Let the DB start
python /app/infrastructure/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /app/infrastructure/initial_data.py

exec uvicorn main:app --host 0.0.0.0 --port 80
