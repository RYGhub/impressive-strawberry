import httpx
import pytest

from impressive_strawberry.database import tables

pytestmark = pytest.mark.asyncio


class TestApplicationCreate:
    async def test_success(self, client: httpx.AsyncClient):
        body = {
            "name": "Closure Industries Bot",
            "description": "A bot for achievements in a warpgate-based game.",
            "webhook_url": "https://example.org/closure",
            "webhook_type": "STRAWBERRY",
        }

        response = await client.post("/api/application/v1/", json=body)
        assert response.status_code == 201

        data = response.json()
        assert data.items() >= body.items()
        assert "id" in data
        assert "token" in data
        assert data["groups"] == []
        assert data["users"] == []

    async def test_missing_body(self, client: httpx.AsyncClient):
        response = await client.post("/api/application/v1/")
        assert response.status_code == 422

    async def test_invalid_body(self, client: httpx.AsyncClient):
        body = {
            "name": "Failure App",
        }

        response = await client.post("/api/application/v1/", json=body)
        assert response.status_code == 422


class TestApplicationThisRetrieve:
    async def test_success(self, authenticated_client: httpx.AsyncClient, application: tables.Application):
        response = await authenticated_client.get("/api/application/v1/this")
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= {
            "name": application.name,
            "description": application.description,
            "token": application.token,
            "webhook_url": application.webhook_url,
            "webhook_type": application.webhook_type,
        }.items()

    async def test_missing_auth(self, client: httpx.AsyncClient):
        response = await client.get("/api/application/v1/this")
        assert response.status_code == 401

    async def test_invalid_auth(self, client: httpx.AsyncClient):
        response = await client.get("/api/application/v1/this", headers={
            "Authorization": "Bearer INVALID",
        })
        assert response.status_code == 401


class TestApplicationThisUpdate:
    async def test_success(self, authenticated_client: httpx.AsyncClient, application: tables.Application):
        body = {
            "name": application.name,
            "description": application.description,
            "webhook_url": application.webhook_url,
            "webhook_type": "DISCORD",
        }

        response = await authenticated_client.put("/api/application/v1/this", json=body)
        assert response.status_code == 200

        data = response.json()
        assert data["webhook_type"] == "DISCORD"


class TestApplicationThisDelete:
    async def test_success(self, authenticated_client: httpx.AsyncClient, application: tables.Application):
        response = await authenticated_client.delete("/api/application/v1/this")
        assert response.status_code == 204

        response = await authenticated_client.get("/api/application/v1/this")
        assert response.status_code == 401


class TestApplicationThisRevoke:
    async def test_success(self, authenticated_client: httpx.AsyncClient, application: tables.Application):
        previous_token = application.token

        response = await authenticated_client.patch("/api/application/v1/this/revoke")
        assert response.status_code == 200

        data = response.json()
        assert "token" in data
        assert previous_token != data["token"]

        response = await authenticated_client.get("/api/application/v1/this")
        assert response.status_code == 401
