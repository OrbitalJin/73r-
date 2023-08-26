from typing import Optional
from engine.interfaces.command import Command
from engine.shell.console import console
from engine.core.folder import Folder
from engine.core.file import File

class ls(Command):
    """
    List files and folders in the current directory.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "ls"
        self.description = "List files and folders in the current directory."
        self.usage = "ls [options] [path]"
        self.options = {
            "-l": "Display the long format listing.",
            "-a": "Display all files and folders.",
            "-h": "Display the help message."
        }
    
    def execute(
            self,
            args: Optional[dict] = None,
            options: Optional[dict] = None
        ) -> None:

        if self.shell.sys.disk.current.count() == 0: return console.print("[italic]Empty")

        for item in self.shell.sys.disk.current.list():
            if type(item) == Folder: console.print(f"[bold blue]{item.name}[/]", end = " ")
            if type(item) == File: console.print(f"[green]{item.name}[/]", end = " ")
        console.print(
            "\n\n{fC} file(s), {dirC} folder(s).".format(
                fC = self.shell.sys.disk.current.fileCount(),
                dirC = self.shell.sys.disk.current.folderCount()
        ))