from engine.interfaces.command import Command
import platform
import psutil

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
            "{host}\n{os}\n{cpu}\n{ram}\n{pkgs}"
            .format(
                os   = f":computer_disk: os: {self.sys.name}",
                host = f":house: host: {platform.node()}",
                cpu  = f":computer: cpu: {platform.processor() or 'unknown'}",
                pkgs = f":package: pkgs: {len(self.shell.cog())}",
                ram  = f":brain: ram: {self.ram()}"
        ))

    def ram(self) -> str:
        """
        Helper function for fetch.
        """
        ram = psutil.virtual_memory()
        return "{used}MiB / {total}MiB".format(
            used = int(ram.used / 1024**2),
            total = int(ram.total / 1024**2)
        )