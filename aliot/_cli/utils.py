from rich.console import Console
from rich.style import Style

console = Console()


def print_success(op_name: str = ""):
    console.print(f"[Success \\(°ω°\\)] {op_name}", style=Style(color="green"))


def print_err(op_name: str = ""):
    console.print(f"[Error (・_・ ?)] {op_name}", style=Style(color="red"), )


def print_fail(op_name: str = ""):
    console.print(f"[Failure (’-_-)] {op_name}", style=Style(color="red"))


def print_warning(op_name: str = ""):
    console.print(f"[Warning (ㆆ_ㆆ)] {op_name}", style=Style(color="yellow"))


def print_info(op_name: str = ""):
    console.print(f"[Info (^ ▽ ^)] {op_name}", style=Style(color="cyan"))