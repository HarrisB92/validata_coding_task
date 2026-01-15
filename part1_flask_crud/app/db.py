from __future__ import annotations

import logging
from typing import Callable
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .config import AppConfig

logger = logging.getLogger(__name__)


def build_connection_string(config: AppConfig) -> str:
    """Build the SQL Server ODBC connection string from config."""
    driver = "ODBC Driver 18 for SQL Server"
    base = (
        f"Driver={{{driver}}};"
        f"Server={config.db_server};"
        f"Database={config.db_name};"
        f"TrustServerCertificate={'yes' if config.db_trust_server_cert else 'no'};"
    )
    if config.db_auth_mode == "windows":
        return base + "Trusted_Connection=yes;"
    return base + f"UID={config.db_user};PWD={config.db_password};"


def create_session_factory(config: AppConfig) -> Callable[[], Session]:
    """Create a SQLAlchemy session factory for the configured database."""
    conn_str = build_connection_string(config)
    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={quote_plus(conn_str)}",
        pool_pre_ping=True,
        future=True,
    )
    logger.info("Database engine initialized for server '%s'.", config.db_server)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
