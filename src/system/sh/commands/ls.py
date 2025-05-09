from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.sh.console import console
from system.core import Folder
from system.core import File
from typing import Optional

class ls(Command):
    """
    List files and folders in the current directory.
    """
    def __init__(self, shell: sh.Shell) -> None:
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