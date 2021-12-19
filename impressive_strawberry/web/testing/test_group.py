import httpx
import pytest

from impressive_strawberry.database import tables

pytestmark = pytest.mark.asyncio


class TestGroupList:
    async def test_success(self, authenticated_client: httpx.AsyncClient, group: tables.Group):
        response = await authenticated_client.get("/api/application/v1/this/group/v1")
        assert response.status_code == 200

        data = response.json()
        assert len(data) == 1

        obj = data[0]
        assert isinstance(obj, dict)
        assert obj.items() >= {
            "crystal": "test",
        }.items()


class TestGroupRetrieve:
    async def test_success(self, authenticated_client: httpx.AsyncClient, group: tables.Group):
        response = await authenticated_client.get(f"/api/application/v1/this/group/v1/{group.crystal}")
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= {
            "crystal": "test",
        }.items()


class TestGroupCreate:
    async def test_success(self, authenticated_client: httpx.AsyncClient, group: tables.Group):
        body = {
            "crystal": "new",
        }

        response = await authenticated_client.post(f"/api/application/v1/this/group/v1/", json=body)
        assert response.status_code == 201

        data = response.json()
        assert data.items() >= {
            "crystal": "new"
        }.items()


class TestGroupUpdate:
    async def test_success(self, authenticated_client: httpx.AsyncClient, group: tables.Group):
        body = {
            "crystal": "testone",
        }

        response = await authenticated_client.put(f"/api/application/v1/this/group/v1/test", json=body)
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= {
            "crystal": "testone"
        }

        response = await authenticated_client.get(f"/api/application/v1/this/group/v1/testone")
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= {
            "crystal": "testone"
        }


class TestGroupDelete:
    async def test_success(self, authenticated_client: httpx.AsyncClient, group: tables.Group):
        response = await authenticated_client.delete(f"/api/application/v1/this/group/v1/test")
        assert response.status_code == 200

        data = response.json()
        assert data.items() >= {
            "crystal": "test"
        }

        response = await authenticated_client.get(f"/api/application/v1/this/group/v1/test")
        assert response.status_code == 404
