FROM python:3.10-slim-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --no-cache-dir newrelic

COPY ./ /app
WORKDIR /app/

ENV PYTHONPATH=/app
ENV NEW_RELIC_CONFIG_FILE=./newrelic.ini

ENTRYPOINT ["newrelic-admin", "run-program"]

CMD ["sh", "./prestart.sh"]
