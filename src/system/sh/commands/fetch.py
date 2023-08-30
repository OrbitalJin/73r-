from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from typing import Optional
import platform, psutil

class fetch(Command):
    """
    Display system information.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.name = "fetch"
        self.usage = "fetch"
        self.options = {"-h": "Display the help message."}

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())
        
        self.sys.io.display.print(
            "{host}\n{os}\n{cpu}\n{ram}\n{pkgs}"
            .format(
                os   = f":computer_disk: os: {self.sys.name}",
                host = f":house: host: {platform.node()}",
                cpu  = f":computer: cpu: {platform.processor() or 'unknown'}",
                pkgs = f":package: pkgs: {len(self.shell.cog())}",
                ram  = f":brain: ram: {self.ram()}"
        ))
        self.sys.io.display.print(f"\nMade with :heart: by {self.sys.author}.")

    def ram(self) -> str:
        """
        Helper function for fetch.
        """
        ram = psutil.virtual_memory()
        return "{used}MiB / {total}MiB".format(
            used = int(ram.used / 1024**2),
            total = int(ram.total / 1024**2)
        )