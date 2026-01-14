# Part 1 Flask CRUD

## Setup

1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Install Microsoft ODBC Driver 18 for SQL Server.
   - Windows download: https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server

3. Create the database and table using `db/init.sql`.

4. Configure environment variables (see `.env.example`). Example:

```
DB_SERVER=.\SQLEXPRESS
DB_NAME=validata
DB_AUTH_MODE=windows
DB_USER=your_db_user_here
DB_PASSWORD=your_db_password_here
DB_TRUST_SERVER_CERT=true
```

5. Run the app:

```powershell
python run.py
```

## Endpoints

- REST API: `http://127.0.0.1:5000/api/banks`
- HTML UI: `http://127.0.0.1:5000/banks/`

## API client

```powershell
python scripts/api_client.py
```
