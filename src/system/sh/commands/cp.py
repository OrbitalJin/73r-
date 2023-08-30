from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.core.folder import Folder, DotFolder
from system.core.file import File
from typing import  Optional

class cp(Command):
    """
    Copy a file or directory.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = f"Usage: {self.name} <file> <destination>"
        self.options = {
                "-h": "Show this help message.",
                "-r": "Copy a directory."
            }
        
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: self.sys.io.display.print(self.help)

        if not args: return self.sys.io.display.warning("No source or destination specified. Use -h for help.")
        if len(args) < 2: return self.sys.io.display.warning("No destination specified.")
        src_, dest_ = args.get(0), args.get(1)

        src = self.sys.fs.disk.current.find(name = src_)
        if not src: return self.sys.io.display.error(f"File or folder not found: {src_}")

        if dest_ == "..": dest = self.sys.fs.disk.current.parent
        else: dest = self.sys.fs.disk.current.find(name = dest_)

        if not dest: return self.sys.io.display.error(f"Destination not found: {dest_}")
        if not isinstance(dest, Folder | DotFolder): return self.sys.io.display.error(f"Destination is not a folder: {dest_}")

        if isinstance(src, Folder | DotFolder) and not options and "-r" not in options:
            return self.sys.io.display.warning(f"Source is a directory. Use -r to copy directories.")
        
        # Check if destination contains a file with the same name as the source.
        exists: bool = dest.find(name = src.name) is not None
        if exists: return self.sys.io.display.error(f"Destination already contains a file or directory with the same name: {src.name}")

        if isinstance(src, Folder | DotFolder) and "-r" in options: dest.add(self._rcp(src))
        else: dest.add(self._cp(src))

    
    def _cp(self, src: Folder | DotFolder | File) -> Folder | DotFolder | File:
        """
        Helper function for copying a file or folder.
        """
        if isinstance(src, Folder | DotFolder):
            dest = Folder(addr = self.sys.malloc(), name = src.name)
            for f in src.list(): dest.add(self._cp(f))

        else: dest = File(
                addr = self.sys.malloc(),
                name = src.name,
                content = src.content
            )
        return dest
    
    def _rcp(self, src: Folder | DotFolder) -> Folder | DotFolder:
        """
        Helper function for recursively copying a folder.
        """
        dest = Folder(addr = self.sys.malloc(), name = src.name)
        for f in src.list(): dest.add(self._cp(f))
        return dest
