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

def update_client(client_id, name):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("UPDATE clients SET name = %s WHERE id = %s;", (name, client_id))

        if cur.rowcount == 0:
            raise RuntimeError(f"No client found with ID {client_id}.")

        conn.commit()

def delete_client(client_id):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM clients WHERE id = %s;", (client_id,))

        if cur.rowcount == 0:
            raise RuntimeError(f"No client found with ID {client_id}.")

        conn.commit()

def get_all_clients():
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name FROM clients;")
        rows = cur.fetchall()

        return rows