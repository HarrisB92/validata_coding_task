from __future__ import annotations

import logging
from typing import Optional

from flask import Flask

from .config import AppConfig
from .db import create_session_factory


def create_app(config_override: Optional[dict] = None) -> Flask:
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO)

    if config_override is None:
        app_config = AppConfig.from_env()
        app.config["DB_SESSION_FACTORY"] = create_session_factory(app_config)
    else:
        app.config.update(config_override)

    # register blueprints
    from .banks import banks_bp  # imported here and not at the top to avoid circular imports
    app.register_blueprint(banks_bp, url_prefix="/banks")
    
    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.get("/health")
    def health():
        return {"status": "ok"}
    
    from flask import redirect, url_for

    @app.get("/")
    def index():
        return redirect(url_for("banks.list_banks"))
    
    return app
