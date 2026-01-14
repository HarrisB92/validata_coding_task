import os
import pyodbc

server = os.getenv("DB_SERVER", r".\SQLEXPRESS")
db_name = os.getenv("DB_NAME", "validata")
trust_cert = os.getenv("DB_TRUST_SERVER_CERT", "true").lower() == "true"

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={db_name};"
    "Trusted_Connection=yes;"
    f"TrustServerCertificate={'yes' if trust_cert else 'no'};"
)

with pyodbc.connect(conn_str, timeout=5) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT 1;")
        print("DB connection OK!!!")
