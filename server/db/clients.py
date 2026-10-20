from server.db.db import get_connection

def create_client(name):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO clients (name) VALUES (%s) RETURNING id;", (name,))

        row = cur.fetchone()

        if row is None:
            raise RuntimeError("The client creation didn't return an ID.")

        client_id = row[0]

        conn.commit()

        return client_id

def get_all_clients():
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name FROM clients;")
        rows = cur.fetchall()

        return rows