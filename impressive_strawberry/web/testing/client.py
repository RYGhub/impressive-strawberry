from fastapi.testclient import TestClient

from impressive_strawberry.web.app import app

client = TestClient(app=app)
