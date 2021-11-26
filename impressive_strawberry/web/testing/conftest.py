import pytest
from httpx import AsyncClient

from impressive_strawberry.database.engine import Session
from impressive_strawberry.web.app import app


@pytest.fixture(scope="function")
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test", follow_redirects=True) as c:
        yield c


@pytest.fixture(scope="function")
def session() -> Session:
    with Session() as s:
        yield s
