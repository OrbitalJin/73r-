from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.core.file import File
from typing import Optional


class clock(Command):
    """
    Display the current time.
    """
    def __init__(self, shell: sh.Shell) -> None:
        super().__init__(shell)
        self.usage = f"{self.name}"
        self.options = None

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        ClockApp(self.shell).run() 


from textual.app import App, ComposeResult
from textual.widgets import Digits

class ClockApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #clock {
        width: auto;
    }
    """
    def __init__(self, shell) -> None:
        super().__init__()
        self.shell: sh.Shell = shell
        self.Clock: Digits = Digits("", id = "clock")

    def compose(self) -> ComposeResult:
        yield self.Clock

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        self.Clock.update(self.shell.sys.time)