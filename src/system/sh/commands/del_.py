from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.core.memory_buffer import MemoryBuffer
from system.core.folder import Folder, DotFolder
from system.core.file import File
from typing import Optional

class del_(Command):
    """
    Remove a file or folder using its address.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.name = "del"
        self.usage = "del <addr>"
        self.options = {
            "-h": "Display the help message.",
            "-r": "Remove a folder and its content."
        }
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        if not args: return self.sys.io.display.warning("No address specified. Use -h for help.")
        try: addr: int = int(args.get(0), 16)
        except ValueError: return self.sys.io.display.warning("Invalid address specified. Use -h for help.")

        if addr is None or addr == 0: return self.sys.io.display.warning("Invalid address specified. Use -h for help.")

        isRecursive: bool = "-r" in options

        if isRecursive: self._rdel(addr = addr)
        else: self._del(addr = addr)

    def _del(self, addr: int) -> MemoryBuffer | None :
        """
        Helper Function for del. Remove a file or folder.
        """
        target = self.shell.commands.find._rfindAddr(
            folder = self.sys.fs.disk.root,
            addr = addr
        )

        if not target: return self.sys.io.display.warning("Address not found.")

        if isinstance(target, File): return target.parent.list().remove(target)
        if isinstance(target, Folder | DotFolder): return self.sys.io.display.warning("Cannot delete a folder using this command. Use the -r option.")

        return target
    
    def _rdel(self, addr: int) -> MemoryBuffer | None:
        """
        Helper Function for del. Recursively remove a folder and its content.
        """
        target = self.shell.commands.find._rfindAddr(
            folder = self.sys.fs.disk.root,
            addr   = addr
        )

        if not target: return self.sys.io.display.warning("Address not found.")

        if isinstance(target, File): return target.parent.list().remove(target)
        if isinstance(target, Folder):
            if target.isEmpty(): return target.parent.list().remove(target)
            for item in target.list(): self._rdel(item.addr)
            return self._rdel(target.addr)

        return target
    
    def _rrm(self, target: Folder | File) -> MemoryBuffer:
        """
        Helper Function for rm. Recursively remove a folder and its content.
        """
        if isinstance(target, File): return target.parent.remove(name = target.name)
        if isinstance(target, Folder):
            if target.isEmpty(): return target.parent.remove(name = target.name)
            for item in target.list(): self._rrm(item)
            return self._rm(target)
