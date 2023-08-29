from engine.interfaces.command import Command
from engine.shell.console import console
from typing import Optional

class ll(Command):
    """
    List the contents of the current directory with details.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.usage = "ll [options] [path]"
        self.options = {"-h": "Display the help message."}
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        console.print("[bold blue]Parent\tAddr\tType\tName")
        for item in self.sys.disk.current.list():
            self.sys.io.display.print(
                "{parent}\t{addr}\t{type}\t{name}".format(
                    parent = item.parent.name if item.parent else "/",
                    type = item.type,
                    addr = item.hex_addr,
                    name = item.name,
            ))
        
        self.sys.io.display.print(
            "\n{fC} file(s), {dfC} .file(s), {dirC} folder(s).".format(
                fC = self.sys.disk.current.fileCount(),
                dfC = self.sys.disk.current.dotFileCount(),
                dirC = self.sys.disk.current.folderCount()
        ))