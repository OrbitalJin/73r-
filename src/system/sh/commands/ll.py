from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.sh.console import console
from typing import Optional

class ll(Command):
    """
    List the contents of the current directory with details.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = "ll [options] [path]"
        self.options = {"-h": "Display the help message."}
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())
        if self.sys.fs.disk.current.count() == 0: return console.print("[italic]Empty")
        self.sys.io.display.info("[bold blue]Parent\tAddr\tType\tName")
        for item in self.sys.fs.disk.current.list():
            self.sys.io.display.print(
                "{parent}\t{addr}\t{type}\t{name}".format(
                    parent = item.parent.name if item.parent else "/",
                    type = item.type,
                    addr = item.hex_addr,
                    name = item.name,
            ))
        
        self.sys.io.display.print(
            "\n{fC} file(s), {dfC} .file(s), {dirC} folder(s).".format(
                fC = self.sys.fs.disk.current.fileCount(),
                dfC = self.sys.fs.disk.current.dotFileCount(),
                dirC = self.sys.fs.disk.current.folderCount()
        ))