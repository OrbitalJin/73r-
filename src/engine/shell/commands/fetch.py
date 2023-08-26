from engine.interfaces.command import Command
import platform

class fetch(Command):
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.name = "fetch"
        self.description = "Display system information."
        self.usage = "fetch"
        self.options = None

    def execute(self, args: dict = None, options: dict = None) -> None:
        """
        Display system information.
        """
        self.sys.display.print(
            "name: {name}\nos: {os}\ncpu: {cpu}\ngpu: {gpu}\nram: {ram} "
            .format(
                name = platform.node(),
                os = self.sys.name,
                cpu = platform.processor(),
                gpu = "NVIDIA GeForce GTX 1650",
                ram = "16 GB",
        ))