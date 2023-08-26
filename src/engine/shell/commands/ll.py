from engine.interfaces.command import Command
from engine.shell.console import console


class ll(Command):
    """
    List the contents of the current directory with details.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "ll"
        self.description = "List files and folders in the current directory."
        self.usage = "ll [options] [path]"
        self.options = {
            "-l": "Display the long format listing.",
            "-a": "Display all files and folders.",
            "-h": "Display the help message."
        }
    
    def execute(
            self,
            args: dict = None,
            options: dict = None
        ) -> None:
        console.print("[bold blue]Parent\tAddr\tType\tName")
        for item in self.sys.disk.current.list():
            console.print(
                "{parent}\t{addr}\t{type}\t{name}".format(
                    parent = item.parent.name if item.parent else "/",
                    type = item.type,
                    addr = item.addr,
                    name = item.name,
            ))
        
        console.print(
            "\n{fC} file(s), {dfC} .file(s), {dirC} folder(s).".format(
                fC = self.sys.disk.current.fileCount(),
                dfC = self.sys.disk.current.dotFileCount(),
                dirC = self.sys.disk.current.folderCount()
        ))