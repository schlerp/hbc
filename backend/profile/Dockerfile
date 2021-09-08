FROM python:alpine

ARG MAINTAINER=scherpderpson@gmail.com
ARG VERSION=1.0.0

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m venv /venv
RUN . /venv/bin/activate && python -m pip install -r requirements.txt

COPY profile /app/profile

CMD ["/venv/bin/python", "-m", "profile"]
