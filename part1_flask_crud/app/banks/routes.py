from __future__ import annotations

from flask import current_app, redirect, render_template, request, url_for
from sqlalchemy.orm import Session
from flask import abort

from ..models import Bank
from . import banks_bp


def _get_session() -> Session:
    session_factory = current_app.config["DB_SESSION_FACTORY"]
    return session_factory()


@banks_bp.get("/")
def list_banks():
    session = _get_session()
    try:
        banks = session.query(Bank).order_by(Bank.id).all()
        return render_template("banks_list.html", banks=banks)
    finally:
        session.close()


@banks_bp.get("/new")
def new_bank_form():
    return render_template("bank_form.html")


@banks_bp.post("/new")
def create_bank():
    name = (request.form.get("name") or "").strip()
    location = (request.form.get("location") or "").strip()
    if not name or not location:
        return render_template("bank_form.html", error="Name and location are required.")

    session = _get_session()
    try:
        bank = Bank(name=name, location=location)
        session.add(bank)
        session.commit()
        return redirect(url_for("banks.list_banks"))
    finally:
        session.close()


@banks_bp.get("/<int:bank_id>")
def bank_detail(bank_id: int):
    session = _get_session()
    try:
        bank = session.get(Bank, bank_id)
        if not bank:
            return render_template("bank_detail.html", bank=None), 404
        return render_template("bank_detail.html", bank=bank)
    finally:
        session.close()


@banks_bp.post("/<int:bank_id>/delete")
def delete_bank(bank_id: int):
    session = _get_session()
    try:
        bank = session.get(Bank, bank_id)
        if not bank:
            abort(404)
        session.delete(bank)
        session.commit()
        return redirect(url_for("banks.list_banks"))
    finally:
        session.close()
