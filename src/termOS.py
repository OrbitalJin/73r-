from system.system import System
from system.sdk import Command

from typing import Optional

class MyCMD(Command):
    """
    My awesome very useful command. (Definitely not a hello world)
    """
    def __init__(self, shell) -> None:
        super().__init__(shell = shell)
        self.usage: str = "mycmd [args] [options]"
        self.options: Optional[dict] = {
            "-h": "Display the help message.",
            "-v": "Display the version."
        }

    def execute(self, args: dict = None, options: dict = None) -> None:
        if options and "-h" in options: return self.help()
        if options and "-v" in options: return self.version()
        
        if not args: return self.sys.io.display.print("Hello, world!")
        if args:
            for arg in args.values(): self.sys.io.display.print(f"Hello, {arg}!")

    def version(self) -> None:
        self.sys.io.display.print("MyCMD v1.0.0")

class time(Command):
    """
    Display the current time.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell = shell)
        self.usage      : str = "time [options]"
        self.options    : Optional[dict] = {
            "-h": "Display the help message.",
        }
    
    def execute(self, args: dict = None, options: dict = None) -> None:
        if options and "-h" in options: return self.help()
        print(self.shell.sys.time)

# Entry point
if __name__ == "__main__":
    system: System = System(name = "TermOS")
    system.shell.commands.attach(MyCMD(system.shell))
    system.shell.commands.attach(time(system.shell))
    system.boot("./data/termOS.state")
    system.loop()