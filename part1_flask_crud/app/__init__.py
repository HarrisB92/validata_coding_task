from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    # register blueprints
    from .banks import banks_bp  # imported here and not at the top to avoid circular imports
    app.register_blueprint(banks_bp, url_prefix="/banks")

    @app.get("/health")
    def health():
        return {"status": "ok"}
    
    return app
