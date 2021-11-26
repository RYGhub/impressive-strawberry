import uuid

import pytest
import sqlalchemy.sql as ss

from impressive_strawberry.database import tables


@pytest.mark.asyncio
async def test_application_create(client, session):
    r = await client.post("/api/application/v1", json={
        "name": "Test App",
        "description": "An app that performs unit testing.",
        "webhook": "https://example.org/",
    })
    assert r.status_code == 201

    data = r.json()
    assert isinstance(data, dict)
    assert data["name"] == "Test App"
    assert data["description"] == "An app that performs unit testing."
    assert data["webhook"] == "https://example.org/"
    assert "token" in data
    assert len(data["groups"]) == 0
    assert len(data["users"]) == 0

    id_ = uuid.UUID(data["id"])
    assert id_

    app = session.execute(
        ss.select(tables.Application).where(tables.Application.id == id_)
    ).one()

    assert app.name == "Test App"
    assert app.description == "An app that performs unit testing."
    assert app.webhook == "https://example.org/"
    assert app.token is not None
    assert len(app.groups) == 0
    assert len(app.users) == 0
