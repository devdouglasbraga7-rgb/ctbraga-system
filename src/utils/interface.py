from rich.console import Console
from rich.panel import Panel

console = Console()

def titulo(texto):
    console.print(
        Panel.fit(
            f"[bold white]{texto}[/]",
            border_style="red",
            width=100
        )
    )

def menu(titulo_menu, opcoes):
    texto = "\n".join(opcoes)
    
    console.print(
        Panel(
            texto,
            title=titulo_menu,
            border_style="red",
            width=30
        )
    )