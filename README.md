<div align="center">
  <img src="https://github.com/bernatixer/stylizer/blob/main/assets/logo.png" alt="Stylizer">
    <a href="https://github.com/bernatixer/stylizer/actions" target="_blank">
        <img src="https://github.com/bernatixer/stylizer/actions/workflows/deploy.yaml/badge.svg" alt="Deployment">
    </a>
    <br/>
    <i>Apply a given style to an image in real time.</i>
    <br/><br/>
    <i><b>NOTE:</b> This application served as a learning project, so beexpect overengineering or not necessary complex solutions such as Kubernetes.</i>
</div>

---

## Usage

You can find the docs here: http://localhost:8000/docs

Format the code using the following command:
```bash
make format
```

> ℹ️ Images are returned in JPG format

## Run stylizer locally

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

## Deploy

This application has been built using Kubernetes and with a CI/CD pipeline using GitHub Actions and ArgoCD.

<div align="center"><img src="https://github.com/bernatixer/stylizer/blob/main/assets/pipeline.jpg" alt="CI/CD pipeline"></div>

## Database migrations

In order to run database migrations, the way to do it is through Alembic.

```bash
cd app
alembic revision -m "Migration description name"
```

This will create a new migration file under the alembic folder, in which you can set there the migration.
