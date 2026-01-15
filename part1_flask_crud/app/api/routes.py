from __future__ import annotations

from typing import Any, Dict

from flask import current_app, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ..models import Bank
from . import api_bp


def _get_session() -> Session:
    """Return a new database session from the app config."""
    session_factory = current_app.config["DB_SESSION_FACTORY"]
    return session_factory()


def _serialize_bank(bank: Bank) -> Dict[str, Any]:
    """Serialize a Bank model for JSON responses."""
    return {"id": bank.id, "name": bank.name, "location": bank.location}


@api_bp.get("/banks")
def list_banks():
    """List all banks ordered by ID."""
    session = _get_session()
    try:
        banks = session.query(Bank).order_by(Bank.id).all()
        return jsonify([_serialize_bank(bank) for bank in banks]), 200
    finally:
        session.close()


@api_bp.post("/banks")
def create_bank():
    """Create a new bank from the request payload."""
    payload = request.get_json(silent=True) or {}
    name = (payload.get("name") or "").strip()
    location = (payload.get("location") or "").strip()
    if not name or not location:
        return jsonify({"error": "name and location are required."}), 400

    session = _get_session()
    try:
        bank = Bank(name=name, location=location)
        session.add(bank)
        session.commit()
        session.refresh(bank)
        return jsonify(_serialize_bank(bank)), 201
    except SQLAlchemyError:
        session.rollback()
        return jsonify({"error": "Failed to create bank."}), 400
    finally:
        session.close()


@api_bp.get("/banks/<int:bank_id>")
def get_bank(bank_id: int):
    """Return a single bank by ID."""
    session = _get_session()
    try:
        bank = session.get(Bank, bank_id)
        if not bank:
            return jsonify({"error": "Bank not found."}), 404
        return jsonify(_serialize_bank(bank)), 200
    finally:
        session.close()


@api_bp.put("/banks/<int:bank_id>")
def update_bank(bank_id: int):
    """Update an existing bank by ID."""
    payload = request.get_json(silent=True) or {}
    name = (payload.get("name") or "").strip()
    location = (payload.get("location") or "").strip()
    if not name or not location:
        return jsonify({"error": "name and location are required."}), 400

    session = _get_session()
    try:
        bank = session.get(Bank, bank_id)
        if not bank:
            return jsonify({"error": "Bank not found."}), 404
        bank.name = name
        bank.location = location
        session.commit()
        return jsonify(_serialize_bank(bank)), 200
    except SQLAlchemyError:
        session.rollback()
        return jsonify({"error": "Failed to update bank."}), 400
    finally:
        session.close()


@api_bp.delete("/banks/<int:bank_id>")
def delete_bank(bank_id: int):
    """Delete a bank by ID."""
    session = _get_session()
    try:
        bank = session.get(Bank, bank_id)
        if not bank:
            return jsonify({"error": "Bank not found."}), 404
        session.delete(bank)
        session.commit()
        return "", 204
    finally:
        session.close()
