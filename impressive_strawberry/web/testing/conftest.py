import pytest
from httpx import AsyncClient

from impressive_strawberry.web.app import app


@pytest.fixture(scope="session")
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test"):
        yield client
