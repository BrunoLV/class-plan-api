# syntax=docker/dockerfile:1

FROM python:3.9.7-slim AS build_image

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

WORKDIR /build

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY src .
COPY pyproject.toml .
COPY setup.cfg .

RUN pip install -U .

FROM python:3.9.7-slim

WORKDIR /app

COPY --from=build_image /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
COPY . .
EXPOSE 8080
CMD ./scripts/startup.sh

