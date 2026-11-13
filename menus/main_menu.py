from simple_term_menu import TerminalMenu

from menus.client_menu import client_menu
from menus.plan_menu import plan_menu
from models.Tools import Tools
from ui.display import display_header


def main_menu():
    while True:
        Tools.clear()
        display_header()

        choice = TerminalMenu(
            [
                "👤 Clients",
                "📋 Plans",
                "🚪 Exit",
            ],
            title="Main Menu",
        ).show()

        if choice == 0:
            client_menu()

        elif choice == 1:
            plan_menu()

        else:
            break