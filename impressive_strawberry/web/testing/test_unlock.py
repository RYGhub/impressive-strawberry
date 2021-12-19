import httpx
import pytest

from impressive_strawberry.database import tables

pytestmark = pytest.mark.asyncio


class TestUnlockCreate:
    def test_success(self, authenticated_client: httpx.AsyncClient, achievement: tables.Achievement, user: tables.User):
        ...


class TestUnlockDelete:
    def test_success(self, authenticated_client: httpx.AsyncClient):
        ...


class TestDirectUnlockCreate:
    def test_success(self, client: httpx.AsyncClient):
        ...
