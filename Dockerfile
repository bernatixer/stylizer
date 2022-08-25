FROM python:3.10-slim-buster

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install torch==1.10.1+cpu torchvision==0.11.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY ./app /app
COPY .env /app/.env
WORKDIR /app/

ENV PYTHONPATH=/app

CMD ["sh", "./prestart.sh"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["gunicorn", "main:app", "-workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind" "0.0.0.0:80"]
