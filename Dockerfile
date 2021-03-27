FROM python:3.7-alpine

RUN apk add --no-cache --update \
  musl-dev \
  gcc \
  python3-dev

RUN mkdir -p /app/jinjaClone

ENV PYTHONPATH="/app:${PYTHONPATH}"
WORKDIR /app/

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY test-requirements.txt /app
RUN pip install -r test-requirements.txt

WORKDIR /app/jinjaClone/
COPY . .

ENTRYPOINT ["python", "lang_bin.py"]
