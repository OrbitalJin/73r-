# To prevent running into circular imports when annotating, we use the __future__ module
from __future__ import annotations
import system.system as sys

from system.sh.console import console

class Display:
    """
    Write/Output messages to the user.
    """
    def __init__(self, sys: sys.System) -> None:
        self.sys = sys

    def print(self, message: str) -> None:
        """
        Print a message to the console.
        """
        console.print(message)
    
    def printLn(self, message: str) -> None:
        """
        Print a message to the console with a new line.
        """
        console.print(f"{message}\n")

    def log(self, message: str) -> None:
        """
        Log a message to the console.
        """
        console.log(message)

    def warning(self, message: str, bold: bool = False) -> None:
        """
        Print a warning message to the console.
        """
        match bold:
            case True: self.print(f"[bold yellow]{message}[/]")
            case False: self.print(f"[yellow]{message}[/]")

    def error(self, message: str, bold: bool = False) -> None:
        """
        Print an error message to the console.
        """
        match bold:
            case True: self.print(f"[bold red]{message}[/]")
            case False: self.print(f"[red]{message}[/]")
        
    def success(self, message: str, bold: bool = False) -> None:
        """
        Print a success message to the console.
        """
        match bold:
            case True: self.print(f"[bold green]{message}[/]")
            case False: self.print(f"[green]{message}[/]")
        
    def info(self, message: str, bold: bool = False) -> None:
        """
        Print an info message to the console.
        """
        match bold:
            case True: self.print(f"[bold blue]{message}[/]")
            case False: self.print(f"[cyan]{message}[/]")

    def header(self) -> None:
        """
        Print the system header.
        """
        console.rule(f"[bold green] {self.sys.name} [/]", style = "bold green")

    def editorHeader(self, filename: str) -> None:
        """
        Print the editor header.
        """
        console.print(
                f"[bold](*) bim[/] - Editing [underline]{filename}[/] | Press [red]Enter[/red] to save and exit.\n",
                justify = "center"
            )
