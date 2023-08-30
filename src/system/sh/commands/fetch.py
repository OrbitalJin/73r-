from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.meta.ascii import ascii
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

        system_info: str = (
            "{host}\n{os}\n{cpu}\n{ram}\n{pkgs}"
            .format(
                os   = f":computer_disk: os: {self.sys.name}",
                host = f":house: host: {platform.node()}",
                cpu  = f":computer: cpu: {platform.processor() or 'unknown'}",
                pkgs = f":package: pkgs: {len(self.shell.cog())}",
                ram  = f":brain: ram: {self.ram()}"
            )
        )
        self._render(system_info)

    def ram(self) -> str:
        """
        Helper function for fetch.
        """
        ram = psutil.virtual_memory()
        return "{used}MiB / {total}MiB".format(
            used = int(ram.used / 1024**2),
            total = int(ram.total / 1024**2)
        )
    
    def _render(self, info: str) -> str:
        """
        Helper function for fetch.
        """
        artRows   = ascii.splitlines()
        maxArtCol = max(len(line) for line in artRows)
        infoLines = f"\n{info}".splitlines()

        # Added empty to the art of the info depending on which is longer.
        if len(artRows) > len(infoLines): infoLines += [''] * (len(artRows) - len(infoLines))
        else: artRows += [''] * (len(infoLines) - len(artRows))

        # Print the art and info side by side.
        for art_line, info_line in zip(artRows, infoLines):
            art_padding = ' ' * (maxArtCol - len(art_line))
            self.sys.io.display.print(f"{art_line}{art_padding}    {info_line}")

        # Print the author.
        self.sys.io.display.print(f"\nMade with :heart: by {self.sys.author}.")

