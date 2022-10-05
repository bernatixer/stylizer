#! /usr/bin/env bash

exec uvicorn main:app --host 0.0.0.0 --port 80 --reload
# gunicorn main:app -workers 4 --worker-class uvicorn.workers.UvicornWorker --bind" "0.0.0.0:80
