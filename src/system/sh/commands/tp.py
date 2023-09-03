from __future__ import annotations
import system.sh.shell as sh

from system.core.folder import Folder, DotFolder
from system.core.file import File

from system.core.interfaces.command import Command
from typing import Optional

class tp(Command):
    """
    'Teleport' a buffer from one address to another.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = "tp <source_addr> <dest_addr>"
        self.options = {
            "-h": "Display the help message."
        }

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        if not args: return self.sys.io.display.warning("No address specified. Use -h for help.")

        try: source_addr: int = int(args.get(0), 16)
        except ValueError: return self.sys.io.display.warning("Invalid source address.")

        try: dest_addr: int = int(args.get(1), 16)
        except ValueError: return self.sys.io.display.warning("Invalid destination address.")

        src: Folder | File = self.sys.shell.commands.find._rfindAddr(
            folder = self.sys.fs.disk.root,
            addr = source_addr
        ) if source_addr != 0 else None

        if src is None: return self.sys.io.display.warning("Source address not found.")
        
        dest: Folder | File = self.sys.shell.commands.find._rfindAddr(
            folder = self.sys.fs.disk.root,
            addr = dest_addr
        ) if dest_addr != 0 else self.sys.fs.disk.root

        if dest is None: return self.sys.io.display.warning("Destination address not found.")

        if not isinstance(dest, Folder | DotFolder): return self.sys.io.display.warning("Cannot teleport source into a file.")

        src.parent.list().remove(src)
        dest.add(src)