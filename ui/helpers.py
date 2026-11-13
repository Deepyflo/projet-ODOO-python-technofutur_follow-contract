from rich.prompt import Prompt

def pause():
    Prompt.ask("[dim]Press Enter to continue[/dim]", default="")