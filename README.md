# 🖼️ Stylizer

Apply a given style to an image in real time.

## Usage

You can find the docs here: http://localhost:8000/docs

Format the code using the following command:
```bash
make format
```

> ℹ️ Images are returned in JPG format

## Running

### Run the service using Docker

Run the following commands to build the Docker container and run it:

First build the image:
```bash
make build
```

Then, run the docker:
```bash
make run
```

Service starts on port: http://localhost:8000

### Run the service locally

First install the dependencies:
```bash
make install
```

Then, run the service:

Run Postgres

```bash
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=changethis -e POSTGRES_USER=postgres -e POSTGRES_DB=app postgres
```

```bash
make run-dev
```

Service starts on port: http://localhost:8000
