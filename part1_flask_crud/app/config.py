from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
load_dotenv()

@dataclass(frozen=True)
class AppConfig:
    """Application configuration loaded from environment variables."""

    db_server: str
    db_name: str
    db_auth_mode: str
    db_user: Optional[str]
    db_password: Optional[str]
    db_trust_server_cert: bool

    @classmethod
    def from_env(cls) -> "AppConfig":
        """Load configuration from environment variables with validation."""
        db_server = os.getenv("DB_SERVER", "").strip()
        db_name = os.getenv("DB_NAME", "").strip()
        db_auth_mode = os.getenv("DB_AUTH_MODE", "windows").strip().lower()
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_trust_server_cert = os.getenv("DB_TRUST_SERVER_CERT", "true").strip().lower() == "true"

        if not db_server:
            raise ValueError("DB_SERVER is required.")
        if not db_name:
            raise ValueError("DB_NAME is required.")
        if db_auth_mode not in {"windows", "sql"}:
            raise ValueError("DB_AUTH_MODE must be 'windows' or 'sql'.")
        if db_auth_mode == "sql":
            if not (db_user and db_user.strip()):
                raise ValueError("DB_USER is required when DB_AUTH_MODE=sql.")
            if not (db_password and db_password.strip()):
                raise ValueError("DB_PASSWORD is required when DB_AUTH_MODE=sql.")

        return cls(
            db_server=db_server,
            db_name=db_name,
            db_auth_mode=db_auth_mode,
            db_user=db_user,
            db_password=db_password,
            db_trust_server_cert=db_trust_server_cert,
        )
