from server.db.db import get_connection

def check_database_connection():
    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT 1;")
                result = cur.fetchone()
                print(f"Database connection successful: {result[0]}")
            except Exception as e:
                print(f"Database connection failed: {e}")