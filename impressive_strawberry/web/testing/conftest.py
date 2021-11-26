import dotenv
import pytest
from httpx import AsyncClient

from impressive_strawberry.database.engine import Session
from impressive_strawberry.web.app import app


@pytest.fixture(scope="session", autouse=True)
def load_dotenv_testing():
    dotenv.load_dotenv(".env")
    dotenv.load_dotenv(".env.testing")


@pytest.fixture(scope="session")
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c


@pytest.fixture(scope="session")
def session() -> Session:
    with Session() as s:
        yield s
