# Validata Coding Task

This repository contains the solution to the coding task provided by Validata Group
as part of the interview process for the Senior Data Scientist / Python Developer role.

The project is divided into two independent parts:

- Part 1: Backend development (Flask CRUD application with SQL Server)
- Part 2: Machine Learning (Loan approval prediction)

Each part is self-contained and includes its own README with detailed instructions.

---

## Repository Structure

```
validata_coding_task/
├── part1_flask_crud/        Flask CRUD application (SQL Server)
├── part2_ml/               Machine Learning task (KNN & Decision Tree)
├── .env.example            Environment variables template
├── AGENTS.md               Development / Codex guidance
└── README.md               This file
```
---

## Prerequisites

General requirements:

- Python 3.10+
- Git

Additional requirements per task are documented in the respective subfolders.

---

## Configuration

Configuration is handled via environment variables.

1. Copy the example file:

   cp .env.example .env

2. Edit `.env` to match your local environment.

Important:
- The `.env` file is environment-specific
- It is intentionally NOT committed to the repository

---

## Part 1 — Flask CRUD Application

Part 1 implements a CRUD application for managing banks using:

- Flask
- Microsoft SQL Server
- SQLAlchemy
- REST API and HTML UI
- PyTest for testing

Detailed setup, database initialization, API usage, and testing instructions are
available in:

   part1_flask_crud/README.md

---

## Part 2 — Machine Learning Task

Part 2 focuses on predicting loan approval using:

- K-Nearest Neighbors (KNN)
- Decision Tree classifiers
- Synthetic dataset generation
- Feature preprocessing and evaluation

The task includes:
- Dataset generation
- Model training and evaluation
- Feature importance analysis
- Business insights report

Detailed instructions and findings are available in:

- part2_ml/README.md
- part2_ml/report.md

---

## Notes

- Each task can be reviewed and executed independently.
- The repository is structured to emphasize clarity, reproducibility, and
  professional software and data science practices.
- No secrets or credentials are committed to version control.
