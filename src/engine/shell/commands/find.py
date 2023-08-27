from engine.interfaces.command import Command
from engine.shell.console import console
from engine.core.dotfile import DotFile
from engine.core.folder import Folder
from engine.core.file import File
from typing import Optional

class find(Command):
    """
    Find a file or folder by name.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "find"
        self.usage = "find [options] [path]"
        self.options = {
            "-h": "Display the help message.",
            "-r": "Recursively find a file or folder by name."
        }
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.display.print(self.help())
        if not args: return self.sys.display.warning("No file or folder name specified. Use 'find -h' for help.")
            
        name: str = args.get(0)
        isRecursive: bool = "-r" in options

        if isRecursive: result = self._rfind(self.sys.disk.current, name)
        else: result = self._find(self.sys.disk.current, name)

        if not result: return self.sys.display.error(f"File or folder not found: {name}")
        console.print(
            "{type}\t{addr}\t{path}".format(
                type=result.type,
                addr=result.addr,
                path=result.path()
            ))

    def _find(self, dir: Folder, name: str) -> File | DotFile | Folder | None:
        """
        Helper Function for find. Find a file or folder by name from current directory.
        """
        if dir and dir.name == name and type(dir) != DotFile: return dir
        if isinstance(dir, File): return None

        for item in dir.list():
            if item.name == name: return item
        return None


    def _rfind(self, dir: Folder, name: str) -> File | DotFile | Folder | None:
        """
        Helper Function for find. Recursively find a file or folder by name from a specified directory.
        """
        if dir and dir.name == name and type(dir) != DotFile: return dir
        if isinstance(dir, File): return None

        for item in dir.list():
            result = self._rfind(item, name)
            if result: return result
        return None