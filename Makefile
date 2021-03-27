NAME := jinja_clone
TAG := $(shell git log -1 --pretty=%h)
IMG := ${NAME}:${TAG}
LATEST := ${NAME}:latest
antlr4 := java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:${CLASSPATH}" org.antlr.v4.Tool


antlr_build:
	$(antlr4) -Dlanguage=Python3 -visitor ./grammar/Jinja.g4 -Werror -no-listener

docker_build:
	docker build -t ${IMG} .
	docker tag ${IMG} ${LATEST}

run:
	PYTHONPATH=.. python lang_bin.py  --directory=./test_files/basics --write

docker_run: docker_build
	docker container run ${IMG}
