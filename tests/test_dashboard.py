import pytest
from typing import Any, Generator
from flask.testing import FlaskClient
from dashboard.app import app

@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_api(client: FlaskClient) -> None:
    rv = client.get("/api/health")
    assert rv.status_code == 200
    assert rv.json is not None
    assert rv.json["status"] == "ok"

def test_index_route(client: FlaskClient) -> None:
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Project Overview" in rv.data

def test_benchmarks_route(client: FlaskClient) -> None:
    rv = client.get("/benchmarks")
    assert rv.status_code == 200
    assert b"Benchmark Results" in rv.data
