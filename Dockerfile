FROM docker.io/library/python:3.11-slim-buster AS base

ARG DEBIAN_FRONTEND=noninteractive

ENV VIRTUAL_ENV=/venv \
    PATH="/venv/bin:${PATH}"

RUN set -eux; env apt-get update; \
    apt-get install -y --no-install-recommends libpq5; \
    rm -rf /var/lib/apt/lists/*

# Stage: build
# ---------------------------------------------------------
FROM base AS build

ARG DEBIAN_FRONTEND=noninteractive
ARG POETRY_VERSION=1.6.1

RUN set -eux; apt-get update; \
    apt-get install -y --no-install-recommends gcc libpq-dev python3-dev; \
    rm -rf /var/lib/apt/lists/*

RUN set -eux; python -m pip install "poetry==${POETRY_VERSION}"; \
    python -m venv /venv

WORKDIR /src

COPY pyproject.toml poetry.lock /src/

RUN poetry install --no-ansi --no-root --only=main

COPY . /src/

RUN poetry build -f wheel --no-ansi \
    && python -m pip install --no-deps dist/*.whl

# Stage: final
# ---------------------------------------------------------
FROM base

COPY --from=build /venv /venv

EXPOSE 8000

CMD [ "python", "-m", "onlysubs" ]