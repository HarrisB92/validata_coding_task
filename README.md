# Validata Coding Task

This repository contains two coding tasks completed as part of the
Senior Data Scientist / Python Developer interview process at Validata Group.

The project is structured to be reproducible, testable, and easy to review.

---

## Project Structure

```
validata_coding_task/
├── part1_flask_crud/     # Flask + SQL Server CRUD application
├── part2_ml/             # Machine Learning task
├── .env.example          # Environment variables template
├── AGENTS.md             # Development / Codex instructions
└── README.md             # This file
```            

---

## Prerequisites

- Python 3.10+
- Git
- Microsoft SQL Server (Express or Developer edition)
- SQL Server Management Studio (SSMS)
- Microsoft ODBC Driver 18 for SQL Server

---

## Configuration

All configuration is provided via environment variables.

1. Copy the example file:

   cp .env.example .env

2. Adjust values in `.env` to match your local SQL Server instance.

Note:
The `.env` file is intentionally NOT committed to the repository.

---

## Part 1 — Flask CRUD Application

See `part1_flask_crud/README.md` for:

- Database initialization
- Running the Flask application
- REST API usage
- Running tests

---

## Part 2 — Machine Learning Task

See `part2_ml/README.md` and `part2_ml/report.md` for:

- Dataset description
- Preprocessing steps
- Model training and evaluation
- Findings and insights
