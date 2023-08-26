from engine.interfaces.command import Command

class rm(Command):
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "rm"
        self.description = "Remove a file."
        self.usage = "rm <file>"
        self.options = None

    def execute(self, args: dict = None, options: dict = None) -> None:
        """
        Remove a file or folder. rm <name>
        """
        if not args: return self.sys.display.error("No file or folder specified.")
        name: str = args.get(0)
        self.sys.disk.current.remove(name = name)