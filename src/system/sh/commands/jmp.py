from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.core.folder import Folder
from typing import Optional

class jmp(Command):
    """
    Jump to a specific address in virtual memory.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = "jmp <addr>"
        self.options = {
            "-h": "Display the help message."
        }

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        if not args: return self.sys.io.display.warning("No address specified. Use -h for help.")
        try: addr: int = int(args.get(0), 16)
        except ValueError: return self.sys.io.display.warning("Invalid address specified. Use -h for help.")

        if addr is None: return self.sys.io.display.warning("Invalid address specified. Use -h for help.")
        self._jpm(addr = addr)

    def _jpm(self, addr: int) -> Folder | None:
        target = self.shell.commands.find._rfindAddr(
            folder = self.sys.fs.disk.root,
            addr = addr
        )

        if not target: return self.sys.io.display.warning("Address not found.")
        if not isinstance(target, Folder): return self.sys.io.display.warning("Cannot jump to a file.") 
        self.sys.io.display.print(f"Jumped to address {target.hex_addr}.")   
        self.sys.fs.disk.current = target
        return target