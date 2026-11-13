from server.db.db import get_connection


def create_plan(name, price, quota):
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO plans (name, price, quota) VALUES (%s, %s, %s) RETURNING id;", (name, price, quota))

        row = cur.fetchone()

        if row is None:
            raise RuntimeError("The plan creation didn't return an ID.")

        plan_id = row[0]

        conn.commit()

        return plan_id

def get_all_plans():
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name, price, quota FROM plans;")
        rows = cur.fetchall()

        return rows