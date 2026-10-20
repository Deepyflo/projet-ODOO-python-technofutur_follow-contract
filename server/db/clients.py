from server.db.db import get_connection


def create_client(name):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO clients (name) VALUES (%s) RETURNING id;", (name,))

        client_id = cur.fetchone()[0]

        conn.commit()

        return client_id