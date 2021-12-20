import httpx
import pytest
import pytest_mock

from impressive_strawberry.database import tables

pytestmark = pytest.mark.asyncio


class TestUnlockCreate:
    async def test_success(self, mocker: pytest_mock.MockerFixture, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement,
                           user: tables.User):
        true_post = authenticated_client.post
        mocker.patch("httpx.AsyncClient.post")

        response = await true_post(
            f"/api/unlock/v1/", params={
                "group": achievement.group.crystal,
                "achievement": achievement.crystal,
                "user": user.crystal,
            })
        assert response.status_code == 201

        data = response.json()
        assert data.items() >= {
            "achievement_id": str(achievement.id),
            "user_id": str(user.id),
        }.items()
        assert "id" in data
        assert "timestamp" in data


class TestUnlockDelete:
    async def test_success(self, authenticated_client: httpx.AsyncClient, unlock: tables.Unlock):
        response = await authenticated_client.delete(f"/api/unlock/v1/{unlock.id}", )
        assert response.status_code == 204


class TestDirectUnlockCreate:
    async def test_success(self, mocker: pytest_mock.MockerFixture, client: httpx.AsyncClient, achievement: tables.Achievement, user: tables.User):
        true_post = client.post
        mocker.patch("httpx.AsyncClient.post")

        response = await true_post(f"/api/unlock-direct/v1", params={
            "token": achievement.token,
            "user": user.crystal,
        })
        assert response.status_code == 201

        data = response.json()
        assert data.items() >= {
            "achievement_id": str(achievement.id),
            "user_id": str(user.id),
        }.items()
        assert "id" in data
        assert "timestamp" in data
