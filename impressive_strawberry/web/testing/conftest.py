import uuid

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


@pytest.fixture(scope="session")
def db_schema() -> str:
    uid = uuid.uuid4()
    schema = f"testing_{uid.hex.replace('-', '')}"
    engine.engine.execute(f"""CREATE SCHEMA "{schema}";""")

    # This has side-effects that may break stuff, keep it in mind
    # It also ignores migrations
    for table in tables.Base.metadata.tables.values():
        table.schema = schema
    tables.Base.metadata.create_all()

    yield schema

    engine.engine.execute(f"""DROP SCHEMA "{schema}" CASCADE;""")


@pytest.fixture(scope="session")
def session(db_schema: str) -> sqlalchemy.orm.Session:
    with engine.Session() as s:
        yield s


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def group(session: sqlalchemy.orm.Session, application: tables.Application) -> tables.Group:
    g = tables.Group(
        application=application,
        crystal="test",
    )
    session.add(g)
    session.commit()
    return g


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def user(session: sqlalchemy.orm.Session, application: tables.Application) -> tables.User:
    u = tables.User(
        application=application,
        crystal="test",
    )
    session.add(u)
    session.commit()
    return u
