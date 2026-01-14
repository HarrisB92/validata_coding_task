from flask import Blueprint

banks_bp = Blueprint("banks", __name__)

from . import routes  # noqa: F401
