.PHONY: test

test:
	pytest -v

.PHONY: build

build:
	docker build . -t convert-unit:latest

.PHONY: run

run:
	docker run --rm -it -p 5000:5000 convert-unit:latest

.PHONY: drun

drun:
	docker run --rm -d -p 5000:5000 convert-unit:latest
	