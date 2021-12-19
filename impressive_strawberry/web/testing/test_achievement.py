import httpx
import pytest

from impressive_strawberry.database import tables

pytestmark = pytest.mark.asyncio


class TestAchievementList:
    async def test_success(self, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement):
        response = await authenticated_client.get("/api/application/v1/this/group/v1/test/achievement/v1/")
        assert response.status_code == 200

        data = response.json()
        assert len(data) == 1

        obj = data[0]
        assert obj.items() >= {
            "name": "Test Achievement",
            "description": "Achievement unlocked when testing achievement unlocks.",
            "alloy": "BRONZE",
            "secret": False,
            "icon": None,
            "repeatable": False,
            "crystal": "test",
        }.items()


class TestAchievementRetrieve:
    async def test_success(self, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement):
        response = await authenticated_client.get("/api/application/v1/this/group/v1/test/achievement/v1/test")
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= {
            "name": "Test Achievement",
            "description": "Achievement unlocked when testing achievement unlocks.",
            "alloy": "BRONZE",
            "secret": False,
            "icon": None,
            "repeatable": False,
            "crystal": "test",
        }.items()


class TestAchievementCreate:
    async def test_success(self, authenticated_client: httpx.AsyncClient, group: tables.Group):
        body = {
            "name": "My Little Achievement",
            "description": "A fun little achievement to unlock with friends!",
            "alloy": "SILVER",
            "secret": False,
            "icon": None,
            "repeatable": False,
            "crystal": "mla",
        }

        response = await authenticated_client.post("/api/application/v1/this/group/v1/test/achievement/v1/", json=body)
        assert response.status_code == 201

        data = response.json()
        assert data.items() >= body.items()


class TestAchievementUpdate:
    async def test_success(self, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement):
        body = {
            "name": "Test Achievement",
            "description": "Achievement unlocked when testing achievement unlocks.",
            "alloy": "GOLD",
            "secret": False,
            "icon": None,
            "repeatable": False,
            "crystal": "test",
        }

        response = await authenticated_client.put("/api/application/v1/this/group/v1/test/achievement/v1/test", json=body)
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= body.items()

        response = await authenticated_client.get("/api/application/v1/this/group/v1/test/achievement/v1/test")
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= body.items()


class TestAchievementDelete:
    async def test_success(self, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement):
        response = await authenticated_client.delete("/api/application/v1/this/group/v1/test/achievement/v1/test")
        assert response.status_code == 204

        response = await authenticated_client.get("/api/application/v1/this/group/v1/test/achievement/v1/test")
        assert response.status_code == 404
