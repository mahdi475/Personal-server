import os
import tempfile

# Tests use their own throwaway SQLite database, never the real PostgreSQL one.
# These must be set before the app is imported.
_test_db = os.path.join(tempfile.mkdtemp(), "test.db")
os.environ["DATABASE_URL"] = f"sqlite+pysqlite:///{_test_db}"
os.environ["SECRET_KEY"] = "test-secret-key-only-used-in-tests-0123456789"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from database import Base, engine  # noqa: E402
from main import app  # noqa: E402


@pytest.fixture
def client():
    """A test client with an empty database for every test."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def login(client):
    """Registers a user, logs in, and returns the auth header."""

    def _login(username="mahdi", password="supersecret123"):
        client.post("/auth/register", json={"username": username, "password": password})
        response = client.post(
            "/auth/login", data={"username": username, "password": password}
        )
        token = response.json()["access_token"]
        return {"Authorization": f"Bearer {token}"}

    return _login
