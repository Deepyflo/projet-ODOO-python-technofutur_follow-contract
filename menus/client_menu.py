from simple_term_menu import TerminalMenu

from menus.client_actions import (
    create_client_menu,
    delete_client_menu,
    update_client_menu,
)
from models.client import Client
from models.Tools import Tools
from server.db.clients import get_all_clients
from ui.display import display_clients, display_header


def client_menu():
    while True:
        Tools.clear()
        display_header()

        # Display all clients in a table
        result_clients = get_all_clients()
        clients = []

        for client in result_clients:
            clients.append(Client(client[0], client[1]))

        display_clients(clients)

        choice = TerminalMenu(
            [
                "Create client",
                "Update client",
                "Delete client",
                "Back",
            ],
            title="👤 Client Management",
        ).show()

        if choice == 0:
            create_client_menu()
        elif choice == 1:
            if not clients:
                print("No clients available to update.")
                input("Press Enter to continue...")
                continue

            client_ids = [str(client.id) for client in clients]
            client_choice = TerminalMenu(
                client_ids,
                title="Select a client to update",
            ).show()

            if client_choice is not None:
                selected_client_id = clients[client_choice].id
                update_client_menu(selected_client_id)
        elif choice == 2:
            if not clients:
                print("No clients available to delete.")
                input("Press Enter to continue...")
                continue

            client_ids = [str(client.id) for client in clients]
            client_choice = TerminalMenu(
                client_ids,
                title="Select a client to delete",
            ).show()

            if client_choice is not None:
                selected_client_id = clients[client_choice].id
                delete_client_menu(selected_client_id)
        else:
            break