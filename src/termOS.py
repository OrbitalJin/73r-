from system.system import System
from system.sdk import Command

from typing import Optional

# Defining a custom command 
class MyCMD(Command):
    """
    My custom command
    """
    def __init__(self, shell) -> None:
        super().__init__(shell = shell)
        self.usage      : str = "mycommand [args] [options]"
        self.options    : Optional[dict] = {
            "-v": "Display the version of this command.",
        }
    
    def execute(self, args: dict = None, options: dict = None) -> None:
        # Handle options
        if options:
            if "-v" in options: return self.version()
            else: return self.shell.sys.io.display.error("Invalid option.")
        # Handle args
        if not args: return print("Hello World!")
        for arg in args.values():
            print(f"Hello {arg}!")
        
    def version(self) -> None:
        print("1.0.0")

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
    system: System = System(name = "termOS")
    system.shell.commands.attach(MyCMD(system.shell))
    system.shell.commands.attach(time(system.shell))
    system.boot("./data/termOS.state")
    system.loop()