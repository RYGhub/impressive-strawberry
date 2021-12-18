import httpx
import pytest

pytestmark = pytest.mark.asyncio


class TestApplicationCreate:
    async def test_success(self, client: httpx.AsyncClient):
        body = {
            "name": "Closure Industries Bot",
            "description": "A bot for achievements in a warpgate-based game.",
            "webhook_url": "https://example.org/closure",
            "webhook_type": "STRAWBERRY",
        }

        response = await client.post("/api/application/v1", json=body)
        assert response.status_code == 201

        data = response.json()
        assert data.items() >= body.items()
        assert "id" in data
        assert "token" in data
        assert data["groups"] == []
        assert data["users"] == []
