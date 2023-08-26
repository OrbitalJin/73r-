from engine.interfaces.command import Command
from engine.shell.console import console
from engine.core.dotfile import DotFile
from engine.core.folder import Folder
from engine.core.file import File

class find(Command):
    """
    Find a file or folder by name. find <options> <name>
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "find"
        self.description = "Find a file or folder in the current directory."
        self.usage = "find [options] [path]"
        self.options = {
            "-h": "Display the help message.",
            "-r": "Recursively find a file or folder by name."
        }
    
    def execute(
            self,
            args: dict | None = None,
            options: dict | None = None
        ) -> None:
        
        if not args: return self.sys.display.warning("No file or folder name specified.")
        name: str = args.get(0)
        result = self._find(self.sys.disk.current, name)
        if not result: return print(f"File or folder not found: {name}")
        console.print(
            "{type}\t{addr}\t{path}".format(
                type = result.type,
                addr = result.addr,
                path = result.path()
        ))

    def _find(self, dir: Folder, name: str) -> File | DotFile | Folder | None:
        """
        Helper Function for find.
        """
        if dir and dir.name == name and type(dir) != DotFile: return dir
        if isinstance(dir, File): return None

        for item in dir.list():
            result = self._find(item, name)
            if result: return result
        return None