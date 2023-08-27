from engine.interfaces.command import Command
from engine.core.file import File
from typing import Optional

class cat(Command):
    """
    Display the content of a file.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.usage = "cat <file>"
        self.options = None

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.display.print(self.help())

        if not args: return self.sys.display.warning("No file name specified.")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        self.sys.display.print(file.content)
