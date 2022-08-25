<div align="center">
  <img src="https://github.com/bernatixer/stylizer/blob/main/app/static/logo.png" alt="Stylizer">
    ![Deployment](https://github.com/bernatixer/stylizer/actions/workflows/deploy.yaml/badge.svg)
    <i>Apply a given style to an image in real time.</i>
</div>

---

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

## Deploy

A good way to deploy this application on a single server would be to use Dokku.

In order to make the logs be accessible from the Docker volume to the host machine, the following option must be run after setting up the Dokku instalation.

```bash
dokku docker-options:add stylizer deploy,run "-v /home/dokku/logs/stylizer:/var/log"
```

## Database migrations

In order to run database migrations, the way to do it is through Alembic.

```bash
cd app
alembic revision -m "Migration description name"
```

This will create a new migration file under the alembic folder, in which you can set there the migration.
