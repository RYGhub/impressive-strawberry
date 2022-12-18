FROM python:3.10-bullseye AS metadata
LABEL maintainer="Stefano Pigozzi <me@steffo.eu>"
WORKDIR /usr/src/app

FROM metadata AS poetry
RUN pip install "poetry==1.3.1"

FROM poetry AS dependencies
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock
RUN poetry install --no-root --no-dev

FROM dependencies AS package
COPY . .
RUN poetry install

FROM package AS environment
ENV PYTHONUNBUFFERED=1
ENV IS_WEB_HOST=0.0.0.0
ENV IS_WEB_PORT=80

FROM environment AS entrypoint
ENTRYPOINT ["poetry", "run", "python", "-m", "impressive_strawberry.web"]
