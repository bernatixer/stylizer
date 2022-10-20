FROM python:3.10-slim-buster

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --no-cache-dir newrelic

COPY ./ /app
WORKDIR /app/

ENV PYTHONPATH=/app

CMD ["NEW_RELIC_CONFIG_FILE=newrelic.ini", "newrelic-admin", "run-program", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# ENTRYPOINT ["newrelic-admin", "run-program"]
# CMD ["sh", "./prestart.sh"]
