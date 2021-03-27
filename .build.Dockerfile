FROM python:3.7-alpine

RUN apk add --no-cache --update \
  musl-dev \
  postgresql-dev \
  gcc \
  python3-dev \
  curl

RUN apk --update add openjdk7-jre

RUN "/usr/bin/java -version"

RUN cd /usr/local/lib && curl -O https://www.antlr.org/download/antlr-4.7.1-complete.jar

ENV CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"

ENV ENV="/root/.ashrc"

RUN echo "alias antlr4='java -Xmx500M -cp \"/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH\" org.antlr.v4.Tool'" >> "$ENV"

# testing the installation
RUN "java org.antlr.v4.Tool"
RUN "antlr4"



COPY requirements.txt /
RUN pip install -r requirements.txt
COPY test-requirements.txt /
RUN pip install -r test-requirements.txt

RUN mkdir -p /jinjaClone

COPY . /jinjaClone/
WORKDIR /jinjaClone
