import httpx
import pytest
import pytest_mock

from impressive_strawberry.database import tables

pytestmark = pytest.mark.asyncio


class TestGroupUnlockList:
    async def test_success(self, authenticated_client: httpx.AsyncClient, group: tables.Group, user: tables.User, achievement: tables.Achievement,
                           unlock: tables.Unlock):
        response = await authenticated_client.get("/api/unlock-group/v1/", params={
            "group": group.id,
            "user": user.id,
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        obj = data[0]
        assert "timestamp" in obj
        assert obj["achievement_id"] == str(achievement.id)
        assert obj["user_id"] == str(user.id)


class TestUnlockCreate:
    async def test_success(self, mocker: pytest_mock.MockerFixture, authenticated_client: httpx.AsyncClient, application: tables.Application,
                           achievement: tables.Achievement, user: tables.User, webhook: tables.Webhook):
        true_post = authenticated_client.post
        webhook_post = mocker.AsyncMock()
        mocker.patch("httpx.AsyncClient.post", webhook_post)

        response = await true_post(
            f"/api/unlock/v1/", params={
                "group": achievement.group.crystal,
                "achievement": achievement.crystal,
                "user": user.crystal,
            })
        assert response.status_code == 201
        assert webhook_post.call_count == 1
        assert webhook_post.call_args.args[0] == webhook.url  # ?
        assert webhook_post.call_args.kwargs["json"].items() >= {
            "achievement_id": achievement.id,
            "user_id": user.id,
        }.items()

        data = response.json()
        assert data.items() >= {
            "achievement_id": str(achievement.id),
            "user_id": str(user.id),
        }.items()
        assert "id" in data
        assert "timestamp" in data
    
    async def test_failure_not_unlockable(self, mocker: pytest_mock.MockerFixture, authenticated_client: httpx.AsyncClient, application: tables.Application,
                           achievement_not_unlockable: tables.Achievement, user: tables.User, webhook: tables.Webhook):
        true_post = authenticated_client.post
        webhook_post = mocker.AsyncMock()
        mocker.patch("httpx.AsyncClient.post", webhook_post)

        response = await true_post(
            "/api/unlock/v1/", params={
                "group": achievement_not_unlockable.group.crystal,
                "achievement": achievement_not_unlockable.crystal,
                "user": user.crystal,
            })
        assert response.status_code == 406
        assert webhook_post.call_count == 0

        data = response.json()
        assert data.items() >= {
            "error_code": "NOT_UNLOCKABLE"
        }.items()
        assert "reason" in data


class TestUnlockDelete:
    async def test_success(self, authenticated_client: httpx.AsyncClient, unlock: tables.Unlock):
        response = await authenticated_client.delete(f"/api/unlock/v1/{unlock.id}", )
        assert response.status_code == 204


class TestDirectUnlockCreate:
    async def test_success(self, mocker: pytest_mock.MockerFixture, client: httpx.AsyncClient, application: tables.Application, achievement: tables.Achievement,
                           user: tables.User, webhook: tables.Webhook):
        true_post = client.post
        webhook_post = mocker.AsyncMock()
        mocker.patch("httpx.AsyncClient.post", webhook_post)

        response = await true_post(f"/api/unlock-direct/v1", params={
            "token": achievement.token,
            "user": user.crystal,
        })
        assert response.status_code == 201
        assert webhook_post.call_count == 1
        assert webhook_post.call_args.args[0] == webhook.url  # ?
        assert webhook_post.call_args.kwargs["json"].items() >= {
            "achievement_id": achievement.id,
            "user_id": user.id,
        }.items()

        data = response.json()
        assert data.items() >= {
            "achievement_id": str(achievement.id),
            "user_id": str(user.id),
        }.items()
        assert "id" in data
        assert "timestamp" in data
    
    async def test_failure_not_unlockable(self, mocker: pytest_mock.MockerFixture, authenticated_client: httpx.AsyncClient, application: tables.Application,
                           achievement_not_unlockable: tables.Achievement, user: tables.User, webhook: tables.Webhook):
        true_post = authenticated_client.post
        webhook_post = mocker.AsyncMock()
        mocker.patch("httpx.AsyncClient.post", webhook_post)

        response = await true_post("/api/unlock-direct/v1/", params={
            "token": achievement_not_unlockable.token,
            "user": user.crystal,
        })
        assert response.status_code == 406
        assert webhook_post.call_count == 0

        data = response.json()
        assert data.items() >= {
            "error_code": "NOT_UNLOCKABLE"
        }.items()
        assert "reason" in data
