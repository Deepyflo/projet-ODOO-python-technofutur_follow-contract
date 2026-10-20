import psycopg
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from simple_term_menu import TerminalMenu

from models.client import Client
from models.Tools import Tools
from server.db.check import check_database_connection
from server.db.clients import create_client, get_all_clients


console = Console()


def display_header():
    console.print(
        Panel(
            "[bold yellow]🍟 CHIPS[/bold yellow]\n"
            "[dim]Clients • Hours • Invoices • Plans & Subscriptions[/dim]",
            expand=False,
        )
    )


def display_clients(res_clients):
    table = Table(title="Clients", show_header=True)

    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Name", style="blue")

    for client_id, name in res_clients:
        table.add_row(str(client_id), name)

    console.print(table)
    console.print(
        f"[dim]{len(res_clients)} client(s) registered[/dim]\n"
    )


def pause():
    Prompt.ask("[dim]Press Enter to continue[/dim]", default="")


def client_menu():
    while True:
        choice = TerminalMenu(
            [
                "Create client",
                "Back",
            ],
            title="👤 Client Management",
        ).show()

        if choice == 0:
            create_client_menu()

        else:
            break


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


def coming_soon(feature):
    Tools.clear()
    display_header()

    console.print(
        Panel(
            f"[yellow]🚧 {feature}[/yellow]\n\n"
            "[dim]This feature is coming soon...[/dim]",
            expand=False,
        )
    )

    pause()


def main_menu():
    while True:
        Tools.clear()
        display_header()

        res_clients = get_all_clients()
        display_clients(res_clients)

        choice = TerminalMenu(
            [
                "👤 Clients",
                "🚪 Exit",
            ],
            title="Main Menu",
        ).show()

        if choice == 0:
            client_menu()

        else:
            break


def main():
    check_database_connection()
    main_menu()


if __name__ == "__main__":
    main()