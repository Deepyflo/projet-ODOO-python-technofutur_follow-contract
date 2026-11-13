import psycopg
from rich import print as rprint
from rich.prompt import Prompt
from simple_term_menu import TerminalMenu

from models.plan import Plan
from models.Tools import Tools
from server.db.plans import create_plan, get_all_plans
from ui.display import display_header, display_Plans
from ui.helpers import pause


def plan_menu():
    Tools.clear()
    display_header()

    result_plans = get_all_plans()
    plans = []

    for plan in result_plans:
        plans.append(Plan(plan[0], plan[1], plan[2], plan[3]))

    display_Plans(plans)

    while True:
        choice = TerminalMenu(
            [
                "Create plan",
                "Back",
            ],
            title="📋 Plan Management",
        ).show()

        if choice == 0:
            create_plan_menu()
        else:
            break

def create_plan_menu():
    Tools.clear()
    display_header()

    name = Prompt.ask("plan name").strip()

    if not name:
        rprint("[bold red]✗ plan name cannot be empty.[/bold red]")
        pause()
        return
    
    price = Prompt.ask("plan price").strip()

    if not price:
        rprint("[bold red]✗ plan price cannot be empty.[/bold red]")
        pause()
        return
    
    quota = Prompt.ask("plan quota").strip()

    if not quota:
        rprint("[bold red]✗ plan quota cannot be empty.[/bold red]")
        pause()
        return

    rprint(f"\n[green]Creating plan '{name}'...[/green]")

    try:
        plan_id = create_plan(name, price, quota)

    except psycopg.Error as e:
        rprint(
            f"[bold red]✗ Failed to create plan '{name}':[/bold red] {e}"
        )
        pause()
        return

    rprint(
        f"[bold green]✓ Plan '{name}' created "
        f"with ID [cyan]{plan_id}[/cyan][/bold green]"
    )

    pause()