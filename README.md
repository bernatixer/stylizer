<div align="center">
  <img src="https://raw.githubusercontent.com/bernatixer/stylizer/main/assets/logo.png?token=GHSAT0AAAAAABHKMQN7D2LHLOFVZOZFGOZEY3BK62A" alt="Stylizer">
    <a href="https://github.com/bernatixer/stylizer/actions" target="_blank">
        <img src="https://github.com/bernatixer/stylizer/actions/workflows/build-and-deploy.yaml/badge.svg" alt="Deployment">
    </a>
    <a href="http://makeapullrequest.com" target="_blank">
        <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
    </a>
    <br/>
    <i>Boilerplate infrastructure&backend project toapply a given style to an image in real time.</i>
</div>

---

# About

The initial idea behind Stylizer was to have a simple backend application serving a machine learning model to apply a style to a given image. However, the project eventually grew while being a place to learn and test new tools, frameworks, principles...

The new idea behind Stylizer is to be a boilerplate microservices ecosystem project, while keeping the main idea of serving a machine learning model to apply a given style.

Here are some of Stylizer features
- Easily extensible to add new microservices on the ecosystem
- Kubernetes and Helm to define infrastructure
- Secrets management over GitHub Secrets
- Uses GitOps approach for the CI/CD
- Ability to use ArgoCD to deploy any new changes over the code
- Easy to create a new environment (i.e. stage) for the ecosystem
- Observability through external provider (i.e. NewRelic)

# Architecture

I will explain by sections the whole project architecture.

## Infrastructure

As stated before, Stylizer uses Kubernetes to orchestrate the different services.

The ecosystem strategy is built with a Helm chart which you will find in the `/infra` folder. Right now, there are two templates that can be used, _deployment_ and _persistance_.

**Deployment** is what you may want to use to deploy a microservice, in this case, you can specify the number of replicas, public port, docker port and the image to use.

**Persistance** will deploy a PostgreSQL database with the specifications given, in this case the port and the disk space. Having the persistance managed by Kubernetes is an opinionated approach, so I could include everything here, managing persistance layers with Kubernetes might not be scalable, so be warned!

## Services

Right now, Stylizer has two running microservices, `core-service` and `inference-service`.

#### ➤ Core service
This service acts as the lobby, taking the initial requests, performing authentication & authorisation to it and persisting some information.

Concretely,
- Allows to register/login a user
- Generates JWT tokens
- Requires JWT token on endpoints
- Manages currency (tokens) over endpoints calls
- Saves transformations on the DB
- Calls inference service to stylize images

#### ➤ Inference service

This service responsability is mainly to transform an image using a machine learning model.

# Usage

Apart from being able to deploy the whole ecosystem through Kubernetes, there is a docker-compose already defined for development purposes or either simpler deployments.


Format the code using the following command:
```bash
make format
```

> ℹ️ Images are returned in JPG format

### Development

You can develop localy using the docker-compose file. They have an option to detect code changes, so there is no need to rebuild the dockers after code changes.

First build the images:
```bash
make build
```

Then, run the dockers:
```bash
make run
```

Core service starts on port: http://localhost:8000
Inference service starts on port: http://localhost:8001
You can find the docs for the endpoints here: http://localhost:8000/docs

### Deploy

This application has been built using Kubernetes and with a CI/CD pipeline using GitHub Actions and ArgoCD.

<div align="center"><img src="https://github.com/bernatixer/stylizer/blob/main/assets/pipeline.jpg" alt="CI/CD pipeline"></div>

### Database migrations

In order to run database migrations, the way to do it is through Alembic and in the same repository, there is no need to do them directly on the DB.

```bash
cd core-service/app
alembic revision -m "Migration description name"
```

This will create a new migration file under the alembic folder, in which you can detail there the migration.
