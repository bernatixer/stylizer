format:
	isort .
	black .
	flake8 --max-line-length 88

build:
	docker-compose build

run:
	docker-compose up

run-dev:
	cd app && uvicorn main:app --env-file .env.local --reload
