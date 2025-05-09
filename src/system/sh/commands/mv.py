from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.core.folder import Folder, DotFolder
from typing import Optional

class mv(Command):
    """
    Move a file or folder.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = "mv <src> <dst>"
        self.options = {"-h": "Display the help message."}
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        if not args: return self.sys.io.display.warning("No source or destination specified. Use -h for help.")
        if len(args) < 2: return self.sys.io.display.warning("No destination specified.")
        src_, dest_ = args.get(0), args.get(1)

        src = self.sys.fs.disk.current.find(name = src_)
        if not src: return self.sys.io.display.error(f"File or folder not found: {src_}")
        
        if dest_ == "..": dest = self.sys.fs.disk.current.parent
        else: dest = self.sys.fs.disk.current.find(name = dest_)
        
        if not dest: return self.sys.io.display.error(f"Destination not found: {dest_}")
        
        # Check if destination contains a file with the same name as the source.
        exists: bool = dest.find(name = src.name) is not None
        if exists: return self.sys.io.display.error(f"Destination already contains a file or directory with the same name: {src.name}")

        if not isinstance(dest, Folder | DotFolder): return self.sys.io.display.error(f"Destination is not a folder: {dest_}")

        src.parent.list().remove(src)
        dest.add(src)