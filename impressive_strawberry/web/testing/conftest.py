import httpx
import pytest
import sqlalchemy.orm

from impressive_strawberry.database import engine
from impressive_strawberry.database import tables
from impressive_strawberry.web.app import app


@pytest.fixture(scope="function")
async def client() -> httpx.AsyncClient:
    async with httpx.AsyncClient(app=app, base_url="http://test", follow_redirects=True) as c:
        yield c


@pytest.fixture(scope="function")
def session() -> sqlalchemy.orm.Session:
    with engine.Session() as s:
        yield s


@pytest.fixture(scope="function")
def application(session: sqlalchemy.orm.Session) -> tables.Application:
    a = tables.Application(
        name="Test Application",
        description="An application used to perform tests.",
        token="TEST-123",
        webhook_url="",
        webhook_type="STRAWBERRY",
    )
    session.add(a)
    session.commit()
    return a


@pytest.fixture(scope="function")
def group(session: sqlalchemy.orm.Session, application: tables.Application) -> tables.Group:
    g = tables.Group(
        application=application,
        crystal="test",
    )
    session.add(g)
    session.commit()
    return g


@pytest.fixture(scope="function")
def achievement(session: sqlalchemy.orm.Session, group: tables.Group) -> tables.Achievement:
    a = tables.Achievement(
        name="Test Achievement",
        description="Achievement unlocked when testing achievement unlocks.",
        alloy=tables.Alloy.BRONZE,
        secret=False,
        icon=None,
        repeatable=False,
        group=group,
        crystal="test",
    )
    session.add(a)
    session.commit()
    return a


@pytest.fixture(scope="function")
def user(session: sqlalchemy.orm.Session, application: tables.Application) -> tables.User:
    u = tables.User(
        application=application,
        crystal="test",
    )
    session.add(u)
    session.commit()
    return u
