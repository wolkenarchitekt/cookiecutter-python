import pytest


def test_api(api_client):
    response = api_client.get("/api/hello/")
    assert response.status_code == 200
    assert response.text == '"Hello"'
