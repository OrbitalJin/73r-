from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.core.file import File, DotFile
from system.sh.commands.tedit import TEdit

from rich.syntax import Syntax
from typing import Optional

class read(Command):
    """
    Display the content of a file.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = f"{self.name} <file>"
        self.options = None

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        if not args: return self.sys.io.display.warning("No file name specified. Use -h for help.")
        name: str = args.get(0)
        file: File = self.sys.fs.disk.current.find(name = name)
        if not file or not isinstance(file, File | DotFile): return print(f"File not found: {name}")
        if not file.content: return None
        
        is_supported: bool = file.type in TEdit.lang
        if not is_supported:  return self.sys.io.display.boxed(
            message = file.content,
            title   = file.name,
            sub     = "EOF",
        )
        renderable: Syntax = Syntax(
                code = file.content,
                lexer = TEdit.lang.get(file.type, "markdown"),
                theme = "nord",
                line_numbers = True,
            )
        self.sys.io.display.boxed(
            message = renderable,
            title   = file.name,
            sub     = "EOF",
        )

