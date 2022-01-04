FROM python:3.10-bullseye AS metadata
LABEL maintainer="Stefano Pigozzi <me@steffo.eu>"
WORKDIR /usr/src/app

FROM metadata AS poetry
RUN pip install "poetry==1.1.12"

FROM poetry AS dependencies
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN poetry install --no-root --no-dev

FROM dependencies AS package
COPY . .
RUN poetry install

FROM package AS environment
ENV PYTHONUNBUFFERED=1

FROM environment AS entrypoint
ENTRYPOINT ["python", "-m", "impressive_strawberry.web"]
