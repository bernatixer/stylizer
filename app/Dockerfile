FROM python:3.10-slim-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install torch==1.11.0+cpu torchvision==0.12.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY ./ /app
WORKDIR /app/

ENV PYTHONPATH=/app

CMD ["sh", "./prestart.sh"]
