# FROM python:3.8-slim

# WORKDIR /code

# COPY requirements.txt /code/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# RUN pip install torch==1.10.1+cpu torchvision==0.11.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

# COPY ./app /code/app
# COPY .env /code/app/.env

# CMD ["sh", "./app/prestart"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["gunicorn", "app.main:app", "-workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind" "0.0.0.0:80"]


#############################################

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# COPY ./app /app
# COPY .env /app/.env
# COPY requirements.txt requirements.txt

# RUN pip install torch==1.10.1+cpu torchvision==0.11.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
# RUN pip install -r requirements.txt

#############################################

FROM python:3.8-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install torch==1.10.1+cpu torchvision==0.11.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY ./app /app
COPY .env /app/.env
WORKDIR /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
