# Instructions for Codex

Goal: produce professional, secure, testable code for a take-home task.

Repo layout:
- Part 1 Flask CRUD: part1_flask_crud/
- Part 2 ML: part2_ml/

Target environment:
- OS: Windows
- Database: Microsoft SQL Server (local Windows)
- Part 1 DB access: SQLAlchemy + pyodbc
- Provide README instructions for required SQL Server ODBC driver and configuration

Standards:
- Type hints, docstrings, small functions
- No secrets in code: use environment variables for configuration (DB host/user/password, etc.)
- Include a `.env.example` (safe placeholder values). Do not commit real secrets; keep `.env` ignored.
- Use Python `logging` instead of `print`
- Add comments explaining non-obvious steps (avoid obvious/comment spam)

Testing:
- Use pytest
- Tests must be deterministic and run locally (no reliance on external network calls)
