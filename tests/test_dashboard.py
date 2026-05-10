import pytest
from typing import Generator
from flask.testing import FlaskClient
from dashboard.app import create_app

@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app = create_app()
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
    assert b"Overview & Analytics" in rv.data

def test_benchmarks_route(client: FlaskClient) -> None:
    rv = client.get("/benchmarks")
    assert rv.status_code == 200
    assert b"Execution Benchmarks" in rv.data

def test_api_run_tool(client: FlaskClient) -> None:
    rv = client.post("/api/run-tool", json={
        "tool_id": "math/add",
        "payload": {"a": 10, "b": 5}
    })
    assert rv.status_code == 200
    assert rv.json is not None
    assert rv.json["success"] is True
    assert rv.json["result"] == 15

def test_api_run_tool_invalid(client: FlaskClient) -> None:
    rv = client.post("/api/run-tool", json={
        "tool_id": "invalid_tool",
        "payload": {}
    })
    assert rv.status_code == 400
    assert rv.json is not None
    assert rv.json["success"] is False
