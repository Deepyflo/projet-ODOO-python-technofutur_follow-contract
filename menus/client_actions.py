import psycopg
from rich import print as rprint
from rich.prompt import Prompt

from models.Tools import Tools
from server.db.clients import create_client
from ui.display import display_header
from ui.helpers import pause


def create_client_menu():
    Tools.clear()
    display_header()

    name = Prompt.ask("Client name").strip()

    if not name:
        rprint("[bold red]✗ Client name cannot be empty.[/bold red]")
        pause()
        return

    rprint(f"\n[green]Creating client '{name}'...[/green]")

    try:
        client_id = create_client(name)

    except psycopg.Error as e:
        rprint(
            f"[bold red]✗ Failed to create client '{name}':[/bold red] {e}"
        )
        pause()
        return

    rprint(
        f"[bold green]✓ Client '{name}' created "
        f"with ID [cyan]{client_id}[/cyan][/bold green]"
    )

    pause()