from engine.interfaces.command import Command
from engine.shell.console import console
from engine.core.file import File

class cat(Command):
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "cat"
        self.description = "Display the content of a file."
        self.usage = "cat <file>"
        self.options = None

    def execute(self, args: dict = None, options: dict = None) -> None:
        """
        Display the content of a file.
        """
        if not args: return self.sys.display.warning("No file name specified.")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        console.print(file.content)
