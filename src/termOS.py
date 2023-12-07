from system.system import System
from system.sdk import Command

from typing import Optional

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
        if options and "-h" in options: return self.sys.io.display.print(self.help())
        print(self.shell.sys.time)

# Entry point
if __name__ == "__main__":
    system: System = System(name = "TermOS")
    system.shell.commands.attach(time(system.shell))
    system.boot("./data/termOS.state")
    system.loop()