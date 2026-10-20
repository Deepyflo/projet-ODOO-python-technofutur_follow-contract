import psycopg

from server.db.db import get_connection


def check_database_connection():
    with get_connection() as conn, conn.cursor() as cur:
        try:
            cur.execute("SELECT 1;")
            result = cur.fetchone()
            print(f"Database connection successful: {result[0]}")
        except psycopg.Error as e:
            print(f"Database connection failed: {e}")