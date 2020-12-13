format:
	isort .
	black .
	flake8 --max-line-length 88

install:
	pip install -r requirements.txt

build:
	docker build -t stylize .

run-dev:
	cd app && uvicorn main:app --reload

run:
	docker run -p 8000:8000 -e PORT="8000" stylize
