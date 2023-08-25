from engine.shell.console import console

class Display:
    def __init__(self, sys) -> None:
        self.sys = sys

    def print(self, message: str) -> None:
        console.print(message)

    def log(self, message: str) -> None:
        console.log(message)

    def header(self) -> None:
        console.rule(f"[bold green] {self.sys.name} [/]", style = "bold green")

    def editorHeader(self, filename: str) -> None:
        console.print(
                f"[bold](*) bim[/] - Editing [underline]{filename}[/] | Press [red]Enter[/red] to save and exit.\n",
                justify = "center"
            )

    def warning(self, message: str, bold: bool = False) -> None:
        match bold:
            case True: self.print(f"[bold yellow]{message}[/]")
            case False: self.print(f"[yellow]{message}[/]")

    def error(self, message: str, bold: bool = False) -> None:
        match bold:
            case True: self.print(f"[bold red]{message}[/]")
            case False: self.print(f"[red]{message}[/]")
        
    def success(self, message: str, bold: bool = False) -> None:
        match bold:
            case True: self.print(f"[bold green]{message}[/]")
            case False: self.print(f"[green]{message}[/]")
        
    def info(self, message: str, bold: bool = False) -> None:
        match bold:
            case True: self.print(f"[bold blue]{message}[/]")
            case False: self.print(f"[cyan]{message}[/]")


