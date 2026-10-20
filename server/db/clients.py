from rich import print as rprint
from server.db.db import get_connection

def create_client(name):
    rprint(f"[bold green]Creating client '{name}'...[/bold green]")

    with get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO clients (name) VALUES (%s) RETURNING id;", (name,))

                client_id = cur.fetchone()[0]

                conn.commit()

                return client_id
            except Exception as e:
                rprint(f"[bold red]Failed to create client '{name}': {e}[/bold red]")
                return None