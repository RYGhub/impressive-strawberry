FROM python:3.10-alpine AS system
RUN apk add --update --no-cache build-base python3-dev py-pip musl-dev libffi-dev openssl-dev postgresql-dev
RUN pip install --no-cache-dir "poetry==1.3.1"

FROM system AS workdir
WORKDIR /usr/src/app

FROM workdir AS dependencies
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN poetry install --no-root --no-dev

FROM dependencies AS package
COPY . .
RUN poetry install

FROM package AS entrypoint
ENV PYTHONUNBUFFERED=1
ENV IS_WEB_HOST=0.0.0.0
ENV IS_WEB_PORT=80
ENTRYPOINT ["poetry", "run", "python", "-O", "-m"]
CMD ["impressive_strawberry.web"]

FROM entrypoint AS final
LABEL org.opencontainers.image.title="Impressive Strawberry"
LABEL org.opencontainers.image.description="Achievements-as-a-service"
LABEL org.opencontainers.image.licenses="AGPL-3.0-or-later"
LABEL org.opencontainers.image.url="https://github.com/RYGhub/impressive-strawberry"
LABEL org.opencontainers.image.authors="Stefano Pigozzi <me@steffo.eu>"
