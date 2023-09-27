# ![](.media/icon.png) Impressive Strawberry

A web API that allowing applications to manage achievements which can be unlocked by their users

## Links

[![PyPI](https://img.shields.io/pypi/v/impressive-strawberry)](https://pypi.org/project/impressive-strawberry/)
 
[![Website](https://img.shields.io/website?url=https%3A%2F%strawberry.ryg.one%2F)](https://strawberry.ryg.one/)

## Installation

Use the provided Docker image, configuring the following environment variables:

`IS_DB_URI`
: SQLAlchemy engine URL to use to select the database.

`IS_WEB_HOST`
: Host to bind the webserver to.

`IS_WEB_PORT`
: TCP port to bind the webserver to.

`IS_SECRET`
: Secret used for administration tasks.

`CORS_ALLOW_ORIGINS`
: Origins to return in the `Access-Control-Allow-Origins` header.

## Roadmap

The roadmap is published [on GitHub Projects](https://github.com/orgs/RYGhub/projects/1/views/1).
