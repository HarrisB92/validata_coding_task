# Part 1 — Flask CRUD Application (Microsoft SQL Server)

This part implements a full CRUD application for managing banks using:

- Flask
- Microsoft SQL Server
- SQLAlchemy
- REST API + HTML user interface

The application supports both:
- human interaction via HTML forms
- programmatic interaction via a RESTful API

---

## Database Setup

### Requirements
- Microsoft SQL Server (Express or Developer edition)
- SQL Server Management Studio (SSMS)
- Microsoft ODBC Driver 18 for SQL Server

### Initialize the Database
1. Open SQL Server Management Studio (SSMS)
2. Connect to your local SQL Server instance
3. Execute the following script:

   db/init.sql

This script creates:
- Database: `validata`
- Table: `banks` with columns:
  - id (primary key)
  - name
  - location

Note:
The database schema is intentionally provided as SQL so the reviewers
can recreate and connect the database in their own environment.

---

## Python Environment Setup

From the repository root, create and activate a virtual environment:

   python -m venv .venv
   source .venv/Scripts/activate   (Windows / Git Bash)

Install dependencies:

   pip install -r part1_flask_crud/requirements.txt

---

## Configuration

Configuration is handled via environment variables.

1. Copy the example configuration file:

   cp .env.example .env

2. Edit `.env` to match your SQL Server instance.

Important:
- `.env` contains environment-specific configuration
- it is intentionally NOT committed to the repository

---

## Running the Application

From the repository root:

   python part1_flask_crud/run.py

Then open in your browser:

- UI (HTML):  http://127.0.0.1:5000/
- API base:   http://127.0.0.1:5000/api/banks

---

## Application Features

### HTML User Interface
- List all banks
- View bank details
- Create a new bank
- Edit an existing bank
- Delete a bank

### REST API Endpoints

Method   Endpoint                  Description
GET      /api/banks               List banks
POST     /api/banks               Create bank
GET      /api/banks/<id>           Get bank by id
PUT      /api/banks/<id>           Update bank
DELETE   /api/banks/<id>           Delete bank

---

## API Client (Requests)

A standalone Python script demonstrates interaction with the REST API
using the `requests` library.

Run:

   python part1_flask_crud/scripts/api_client.py

The script performs:
- Create
- List
- Get
- Update
- Delete

This satisfies the requirement for a Python program interacting with
a RESTful API.

---

## Testing

Unit tests are written using **pytest**.

To ensure tests are:
- fast
- deterministic
- independent of external infrastructure

an **in-memory SQLite database** is used during testing.

The same SQLAlchemy models and routes are exercised, but without relying
on a live SQL Server instance.

Run tests:

   pytest -q part1_flask_crud/tests

---

## Notes

- UI routes use HTML forms (POST) for update/delete operations
- REST API uses proper HTTP verbs (GET, POST, PUT, DELETE)
- Configuration is externalized via environment variables
- No secrets or credentials are committed to the repository
