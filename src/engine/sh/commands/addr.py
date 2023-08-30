from __future__ import annotations
import engine.sh.shell as sh

from engine.interfaces.command import Command

class addr(Command):
    """
    Display the address of the current directory.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = "addr"
        self.options = {
            "-h": "Display the help message."
        }
    
    def execute(self, args: dict, options: dict) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())


        addr: int = self.sys.fs.disk.current.hex_addr
        self.sys.io.display.print(addr)