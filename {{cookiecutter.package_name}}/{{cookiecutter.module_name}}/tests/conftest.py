import logging
import os
from typing import Any, Generator

import alembic
import pytest
from alembic.config import Config
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typer.testing import CliRunner

from {{cookiecutter.module_name}}.database import get_db
from {{cookiecutter.module_name}}.database.models import Base
from {{cookiecutter.module_name}}.settings import Settings

logging.getLogger("faker.factory").setLevel(logging.WARN)


@pytest.fixture(autouse=True)
def app() -> Generator[FastAPI, Any, None]:import logging
import os
from typing import Any, Generator

import alembic
import pytest
from alembic.config import Config
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typer.testing import CliRunner

from {{cookiecutter.module_name}}.database import get_db
from {{cookiecutter.module_name}}.database.models import Base

logging.getLogger("faker.factory").setLevel(logging.WARN)


@pytest.fixture(autouse=True)
def app() -> Generator[FastAPI, Any, None]:
    from {{cookiecutter.module_name}}.api import get_application

    _app = get_application()
    yield _app


@pytest.fixture(scope="session")
def engine():
    settings = Settings()
    return create_engine(settings.database_url)


@pytest.fixture(scope="session")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture(scope="function")
def apply_migrations(engine):
    """
    Need to manually drop tables and re-create afterwards
    to not interfer with pytest-session-based db-session
    """
    Base.metadata.drop_all(engine)
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")
    Base.metadata.create_all(engine)


@pytest.fixture
def cli_runner(engine):
    """
    CLI runner DB session runs outside of pytest, so we cannot cleanup transactions using db_session.
    Workaround by manually creating tables, dropping and re-reacting afterwards so that
    non-CLI tests can use a clean session-scoped db-session
    """
    Base.metadata.create_all(engine)
    yield CliRunner()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.fixture
def api_client(app: FastAPI, db_session: Session):
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client

    from {{cookiecutter.module_name}}.api import get_application

    _app = get_application()
    yield _app


@pytest.fixture(scope="session")
def engine():
    settings = Settings()
    return create_engine(settings.database_url)


@pytest.fixture(scope="session")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture(scope="function")
def apply_migrations(engine):
    """
    Need to manually drop tables and re-create afterwards
    to not interfer with pytest-session-based db-session
    """
    Base.metadata.drop_all(engine)
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")
    Base.metadata.create_all(engine)


@pytest.fixture
def cli_runner(engine):
    """
    CLI runner DB session runs outside of pytest, so we cannot cleanup transactions using db_session.
    Workaround by manually creating tables, dropping and re-reacting afterwards so that
    non-CLI tests can use a clean session-scoped db-session
    """
    Base.metadata.create_all(engine)
    yield CliRunner()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@pytest.fixture
def api_client(app: FastAPI, db_session: Session):
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
