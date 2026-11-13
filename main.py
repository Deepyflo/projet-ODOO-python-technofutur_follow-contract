from server.db.check import check_database_connection
from menus.main_menu import main_menu


def main():
    check_database_connection()
    main_menu()


if __name__ == "__main__":
    main()