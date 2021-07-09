from typing import Any, Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def app() -> Generator[FastAPI, Any, None]:
    from {{cookiecutter.module_name}}.api import get_application

    _app = get_application()
    yield _app


@pytest.fixture
def api_client(app: FastAPI):
    with TestClient(app) as client:
        yield client
