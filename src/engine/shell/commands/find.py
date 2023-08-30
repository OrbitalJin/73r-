from engine.core.memory_buffer import MemoryBuffer
from engine.core.folder import Folder, DotFolder
from engine.core.file import File, DotFile

from engine.interfaces.command import Command
from typing import Optional

class find(Command):
    """
    Find a file or folder by name within a directory.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "find"
        self.usage = "find [options] [path]"
        self.options = {
            "-h": "Display the help message.",
            "-r": "Recursively find a file or folder by name starting from the current directory."
        }
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())
        if not args: return self.sys.io.display.warning("No file or folder name specified. Use 'find -h' for help.")
            
        name: str = args.get(0)
        isRecursive: bool = "-r" in options

        if isRecursive: result = self._rfind(self.sys.disk.current, name)
        else: result = self._find(self.sys.disk.current, name)

        if not result: return self.sys.io.display.error(f"File or folder not found: {name}")

        self.sys.io.display.print("[blue bold]Type\tAddr\tPath")
        self.sys.io.display.print(
            "{type}\t{addr}\t{path}".format(
                type = result.type,
                addr = result.addr,
                path = result.path()
            ))

    def _find(self, folder: Folder, name: str) -> File | Folder | None:
        """
        Helper Function for find. Find a file or folder by name from current directory.
        """
        for item in folder.list():
            if not isinstance(item, DotFile | DotFolder):
                if item.name == name: return item
        return None

    def _rfind(self, folder: MemoryBuffer, name: str) -> File | Folder | None:
        """
        Helper Function for find. Recursively find a file or folder by name from a specified directory.
        """
        if isinstance(folder, DotFolder | DotFile): return None
        if folder.name == name: return folder
        
        if not isinstance(folder, File):
            for item in folder.list():
                result = self._rfind(item, name)
                if result: return result
        return None
    
    def _findAddr(self, folder: Folder, addr: int) -> File | Folder | None:
        """
        Helper Function for find. Find a file or folder by address from current directory.
        """
        for item in folder.list():
            if not isinstance(item, DotFile | DotFolder):
                if item.addr == addr: return item
        return None
    
    def _rfindAddr(self, folder: MemoryBuffer, addr: int) -> File | Folder | None:
        """
        Helper Function for find. Recursively find a file or folder by address from a specified directory.
        """
        if isinstance(folder, DotFolder | DotFile): return None
        if folder.addr == addr: return folder
        
        if not isinstance(folder, File):
            for item in folder.list():
                result = self._rfindAddr(item, addr)
                if result: return result
        return None