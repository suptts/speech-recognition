install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

test:
	##python -m pytest -vv test_hello.py
	pytest -vv --cov-report term-missing --cov=app test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C main

all: install format lint 
