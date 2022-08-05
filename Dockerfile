FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

COPY ./app /app
COPY .env /app/.env
COPY requirements.txt requirements.txt

RUN pip install torch==1.10.1+cpu torchvision==0.11.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt

# FROM python3.8-slim

# WORKDIR /

# COPY requirements.txt requirements.txt

# RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN pip install torch==1.10.1+cpu torchvision==0.11.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

# COPY ./app /app
# COPY .env /app/.env

# CMD ["sh", "./app/prestart"]
# CMD ["gunicorn", "app.main:app", "-workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind" "0.0.0.0:80"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
