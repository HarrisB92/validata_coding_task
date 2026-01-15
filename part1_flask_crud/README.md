PART 1 – FLASK CRUD APPLICATION
==============================

This project implements a simple Flask application with:

- HTML UI routes
- REST API routes
- SQLAlchemy ORM
- Automated tests using pytest

The application manages banks with full CRUD functionality.


------------------------------------------------------------
SETUP
------------------------------------------------------------

1. Create and activate a virtual environment (commands in PowerShell)

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2. Install dependencies (from inside the part1_flask_crud\ directory)

   pip install -r requirements.txt


------------------------------------------------------------
DATABASE CONFIGURATION
------------------------------------------------------------

The application is designed to work with Microsoft SQL Server
in normal (non-test) usage.

Requirements:
- Microsoft ODBC Driver 18 for SQL Server

Windows download:
https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server


Environment variables:

Create a .env file (see .env.example) and configure:

   DB_SERVER=.\SQLEXPRESS
   DB_NAME=validata
   DB_AUTH_MODE=windows
   DB_USER=your_db_user_here
   DB_PASSWORD=your_db_password_here
   DB_TRUST_SERVER_CERT=true

Note:
The .env file is used only for local development and is NOT
committed to version control.


------------------------------------------------------------
RUN THE APPLICATION
------------------------------------------------------------

From the part1_flask_crud directory:

   python run.py


Available endpoints:

REST API:
   http://127.0.0.1:5000/api/banks

HTML UI:
   http://127.0.0.1:5000/banks

Health check:
   http://127.0.0.1:5000/health


------------------------------------------------------------
RUN TESTS (RECOMMENDED)
------------------------------------------------------------

Tests use an in-memory SQLite database and do NOT require
SQL Server.

From the part1_flask_crud directory:

   python -m pytest -q

All tests should pass.


------------------------------------------------------------
API CLIENT (OPTIONAL)
------------------------------------------------------------

A small API client script is included:

   python scripts/api_client.py


------------------------------------------------------------
NOTES
------------------------------------------------------------

- The application uses the Flask application factory pattern
- Database sessions are injected via configuration
- Tests are isolated and reset database state between runs
- SQL Server is required only for running the app, not for tests