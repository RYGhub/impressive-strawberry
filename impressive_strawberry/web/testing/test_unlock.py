import httpx
import pytest

from impressive_strawberry.database import tables

pytestmark = pytest.mark.asyncio


class TestUnlockCreate:
    async def test_success(self, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement, user: tables.User):
        response = await authenticated_client.post(
            f"/api/application/v1/this/group/v1/{achievement.group.crystal}/achievement/v1/{achievement.crystal}/unlock/v1", params={
                "user": user.crystal,
            })
        assert response.status_code == 201

        data = response.json()
        assert data.items() <= {
            "achievement_id": achievement.id,
            "user_id": user.id,
        }.items()
        assert "id" in data
        assert "timestamp" in data


class TestUnlockDelete:
    async def test_success(self, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement, unlock: tables.Unlock):
        response = await authenticated_client.delete(
            f"/api/application/v1/this/group/v1/{achievement.group.crystal}/achievement/v1/{achievement.crystal}/unlock/v1/{unlock.id}")
        assert response.status_code == 204


class TestDirectUnlockCreate:
    async def test_success(self, client: httpx.AsyncClient, achievement: tables.Achievement, user: tables.User):
        response = await client.post(f"/api/direct-unlock/v1", params={
            "achievement": achievement.token,
        })
        assert response.status_code == 201

        data = response.json()
        assert data.items() <= {
            "achievement_id": achievement.id,
            "user_id": user.id,
        }.items()
        assert "id" in data
        assert "timestamp" in data
