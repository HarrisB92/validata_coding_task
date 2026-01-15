"""
Pytest configuration and fixtures.

For unit tests, an in-memory SQLite database is used instead of the SQL Server
to ensure tests are fast, deterministic, and do not depend on external
infrastructure. The same SQLAlchemy models and session logic are reused,
so application behavior is still validated correctly.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app import create_app
from app.models import Base, Bank


@pytest.fixture(scope="session")
def session_factory():
    engine = create_engine(
        "sqlite+pysqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


@pytest.fixture()
def app(session_factory):
    app = create_app({"DB_SESSION_FACTORY": session_factory, "TESTING": True})
    return app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def cleanup_db(session_factory):
    session = session_factory()
    try:
        session.query(Bank).delete()
        session.commit()
        yield
    finally:
        session.close()
