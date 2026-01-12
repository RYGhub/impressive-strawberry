<div align="center">
<img alt="" src="https://forge.steffo.eu/ryg/impressive-strawberry/raw/branch/main/.media/icon-512.png" height="128" style="border-radius: 100%;">
<hgroup>
<h1>Impressive Strawberry</h1>
<p>Achievement-as-a-service</p>
</hgroup>
</div>

## Links

### Tools

<a href="https://www.python.org/">
	<img alt="Written in Python" title="Written in Python" src="https://img.shields.io/badge/language-python-3775a9" height="30px">
</a>
&hairsp;
<a href="https://fastapi.tiangolo.com/">
	<img alt="Using the FastAPI framework" title="Using the FastAPI framework" src="https://img.shields.io/badge/framework-fastapi-009485" height="30px">
</a>
&hairsp;
<a href="https://docs.pytest.org/en/stable/">
	<img alt="Testing with pytest" title="Testing with pytest" src="https://img.shields.io/badge/testing-pytest-00a0e4" height="30px">
</a>

### Packaging

<a href="https://pypi.org/project/impressive-strawberry">
	<img alt="Available on PyPI" title="Available on PyPI" src="https://img.shields.io/pypi/v/impressive-strawberry?label=pypi&color=ffd242" height="30px">
</a>

### Documentation

<a href="https://www.gnu.org/licenses/agpl-3.0">
	<img alt="Licensed under AGPL-3.0-or-later" title="Licensed under AGPL-3.0-or-later" src="https://img.shields.io/badge/license-AGPL--3.0-663366" height="30px">
</a>

### Development

<a href="https://github.com/RYGhub/impressive-strawberry">
	<img alt="GitHub mirror" title="GitHub mirror" src="https://img.shields.io/github/last-commit/RYGhub/impressive-strawberry?color=f0f6fc&style=flat" height="30px">
</a>
&hairsp;
<a href="https://github.com/RYGhub/impressive-strawberry/releases">
	<img alt="Releases" title="Releases" src="https://img.shields.io/github/v/release/RYGhub/impressive-strawberry?color=f0f6fc&style=flat&label=last+release" height="30px">
</a>
&hairsp;
<a href="https://github.com/RYGhub/impressive-strawberry/issues">
	<img alt="Issues" title="Issues" src="https://img.shields.io/github/issues/RYGhub/impressive-strawberry?color=f0f6fc" height="30px">
</a>
&hairsp;
<a href="https://github.com/RYGhub/impressive-strawberry/pulls">
	<img alt="Pull requests" title="Pull requests" src="https://img.shields.io/github/issues-pr/RYGhub/impressive-strawberry?color=f0f6fc" height="30px">
</a>
&hairsp;
<a href="https://github.com/RYGhub/impressive-strawberry/stargazers">
	<img alt="Stars" title="Stars" src="https://img.shields.io/github/stars/RYGhub/impressive-strawberry?color=f0f6fc&style=flat" height="30px">
</a>
&hairsp;
<a href="https://github.com/RYGhub/impressive-strawberry/network">
	<img alt="Forks" title="Forks" src="https://img.shields.io/github/forks/RYGhub/impressive-strawberry?color=f0f6fc&style=flat" height="30px">
</a>

## Installation

Use the provided Docker image, configuring the following environment variables:

| Variable | Description |
|----------|-------------|
| `IS_DB_URI` | SQLAlchemy engine URL to use to select the database. |
| `IS_WEB_HOST` | Host to bind the webserver to. |
| `IS_WEB_PORT` | TCP port to bind the webserver to. |
| `IS_SECRET` | Secret used for administration tasks. |
| `CORS_ALLOW_ORIGINS` | Origins to return in the `Access-Control-Allow-Origins` header. |

## Roadmap

The roadmap is published [on GitHub Projects](https://github.com/orgs/RYGhub/projects/1/views/1).
