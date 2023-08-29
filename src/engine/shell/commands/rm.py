from engine.core.memory_buffer import MemoryBuffer
from engine.interfaces.command import Command
from engine.core.folder import Folder
from engine.core.file import File
from typing import Optional

class rm(Command):
    """
    Remove a file or folder.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.usage = "rm <file>"
        self.options = {
            "-h": "Display the help message.",
            "-r": "Remove a folder and its content."
        }

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        if not args: return self.sys.io.display.warning("No file or folder specified. Use -h for help.")
        name: str = args.get(0)
        target = self.sys.disk.current.find(name = name)
        if not target: return self.sys.io.display.error(f"File or folder not found: {name}")

        isRecursive: bool = "-r" in options
        if isRecursive: self._rrm(target)
        else: self.sys.disk.current.remove(name = name)

    def _rm(self, target: Folder | File) -> MemoryBuffer:
        """
        Helper Function for rm. Remove a file or folder.
        """
        return target.parent.list().remove(target)

    def _rrm(self, target: Folder | File) -> MemoryBuffer:
        """
        Helper Function for rm. Recursively remove a folder and its content.
        """
        if isinstance(target, File): return target.parent.remove(name = target.name)
        if isinstance(target, Folder):
            if target.isEmpty(): return target.parent.remove(name = target.name)
            for item in target.list(): self._rrm(item)
            return self._rm(target)