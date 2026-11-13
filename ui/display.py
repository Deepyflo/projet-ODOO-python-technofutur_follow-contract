from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def display_header():
    console.print(
        Panel(
            "[bold yellow]🍟 CHIPS[/bold yellow]\n"
            "[dim]Clients • Hours • Invoices • Plans & Subscriptions[/dim]",
            expand=False,
        )
    )

def display_clients(clients):
    table = Table(title="Clients", show_header=True)

    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Name", style="blue")

    for client in clients:
        table.add_row(
            str(client.id),
            client.name,
        )

    console.print(table)

def display_Plans(plans):
    table = Table(title="Plans", show_header=True)

    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Name", style="blue")
    table.add_column("Price", style="green")
    table.add_column("Quota", style="yellow")

    for plan in plans:
        table.add_row(
            str(plan.id),
            plan.name,
            f"€{plan.price:.2f}",
            f"{plan.quota/60:.2f} hours",
        )

    console.print(table)