from simple_term_menu import TerminalMenu
from models.Tools import Tools
from ui.display import display_header
from menus.client_actions import create_client_menu
from server.db.clients import get_all_clients
from ui.display import display_clients
from models.client import Client

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
                "Back",
            ],
            title="👤 Client Management",
        ).show()

        if choice == 0:
            create_client_menu()
        else:
            break