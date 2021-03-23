from flask import json
import pytest
from src.entrypoints.server import Config, make_app

config = Config()


@pytest.fixture
def client():
    app = make_app(config)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_ping(client):
    rv = client.get("/ping")
    assert json.loads(rv.data) == "pong!"
