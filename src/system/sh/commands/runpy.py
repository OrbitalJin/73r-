from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from typing import Optional



class runpy(Command):
    """
    Run a python script inside the shell.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell = shell)
        self.usage   =  "python <script>"
        self.options = {"-h": "Display the help message."}
    
    def execute(self, args: dict = None, options: dict = None) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())
        if not args: return self.sys.io.display.print(self.help())
        file = self.sys.fs.disk.current.find(args[0])
        if not file: return self.sys.io.display.error(f"File {args[0]} not found.")
        if file.type != "py": return self.sys.io.display.warning(f"File {args[0]} is not a python script.")
        try: exec(file.content)
        except Exception as e: self.sys.io.display.error(e)