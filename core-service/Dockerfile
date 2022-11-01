FROM python:3.10-slim-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --no-cache-dir newrelic

COPY ./ /app
WORKDIR /app/

ENV PYTHONPATH=/app
ENV NEW_RELIC_CONFIG_FILE=newrelic.ini

ARG ENV_SECRETS
RUN echo $ENV_SECRETS >> .env

CMD ["newrelic-admin", "run-program", "sh", "./prestart.sh"]
