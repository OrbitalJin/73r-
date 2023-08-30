from typing import Optional
from engine.interfaces.command import Command
from engine.sh.console import console
from engine.core import Folder
from engine.core import File

class ls(Command):
    """
    List files and folders in the current directory.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.usage = "ls [options] [path]"
        self.options = {"-h": "Display the help message."}
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.display.print(self.help())
        if self.shell.sys.fs.disk.current.count() == 0: return console.print("[italic]Empty")

        for item in self.shell.sys.fs.disk.current.list():
            if type(item) == Folder: console.print(f"[bold blue]{item.name}[/]", end = " ")
            if type(item) == File: console.print(f"[green]{item.name}[/]", end = " ")
        console.print(
            "\n\n{fC} file(s), {dirC} folder(s).".format(
                fC = self.shell.sys.fs.disk.current.fileCount(),
                dirC = self.shell.sys.fs.disk.current.folderCount()
        ))