import psycopg
from rich import print as rprint
from rich import prompt as rprompt
from simple_term_menu import TerminalMenu

from models.client import Client
from models.Tools import Tools
from server.db.check import check_database_connection
from server.db.clients import create_client

def main():
    check_database_connection()
    clients = {}

    while True:
        Tools.clear()
        rprint("[bold green]CHIPS: Clients, Hours, Invoices, Plans & Subscriptions![/bold green]")
        menu = TerminalMenu(["Client", "Exit"], title="Main Menu")
        choice = menu.show()

        if choice == 0:
            rprint("[bold green]Client[/bold green]")
            client_menu = TerminalMenu(["Create", "Cancel"], title="Client Menu")
            client_choice = client_menu.show()

            if client_choice == 0:
                name = rprompt.Prompt.ask("Enter client name")

                if not name.strip():
                    rprint("[bold red]Client name cannot be empty.[/bold red]")
                    rprompt.Prompt.ask("Press Enter to return to the main menu...")
                    continue

                rprint(f"[bold green]Creating client '{name}'...[/bold green]")
                try:
                    client_id = create_client(name)
                except psycopg.Error as e:
                    client_id = None
                    rprint(f"[bold red]Failed to create client '{name}': {e}[/bold red]")

                if client_id is not None:
                    clients[client_id] = Client(client_id, name)
                    rprint(f"[bold green]Client '{name}' created with ID: {client_id}[/bold green]")

                rprompt.Prompt.ask("Press Enter to return to the main menu...")
        elif choice == 1 or choice is None:
            break

if __name__ == "__main__":
    main()