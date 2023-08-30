# To prevent running into circular imports when annotating, we use the __future__ module
from __future__ import annotations
import engine.system as sys

from engine.interfaces.structs import colors
from typing import Any
import readline

class Collector:
    """
    The collector is responsible for collecting user input across the system.
    """
    def __init__(self, sys: sys.System) -> None:
        self.sys = sys
        self._cmd: str | None = None
        self._args: dict[str, str] | None = None
        self._options: dict[str, str] | None = None

    def readCmd(self) -> tuple[str] | None:
        """
        Read a command from the user.
        """
        self.cmd, self.args, self.options = self.prompt(
            prompt = "{green}>>>{end} {blue}{path}{end} ".format(
                green = colors.OKGREEN,
                blue  = colors.OKCYAN,
                end   = colors.ENDC,
                path  = self.sys.fs.disk.current.path(),
            ))
        return (self.cmd, self.args, self.options)

    def prompt(self, prompt: str) -> tuple[str | None]:
        """
        Prompt the user for input.
        """
        entry: Any = input(prompt).strip()
        if not entry: return (None, None, None)
        self.cmd, self.args, self.options = self._parse(entry)
        return (self.cmd, self.args, self.options)

    def promptEdit(self, prompt: str = "", prefill: str = None) -> str | None:
        def hook():
            readline.insert_text(prefill)
            readline.redisplay()

        readline.set_pre_input_hook(hook)
        result = input(prompt)
        readline.set_pre_input_hook()
        return result
    
    def _parse(self, entry: str) -> tuple[str | None | dict]:
        """
        Parse the user's input.
        """
        cmd, args, options = None, {}, {}
        self.cmd, self.args, self.options = cmd, args, options
        if not entry: return (None, {}, {})
        collection: list[str] = entry.split()
        self.cmd = collection.pop(0)
        self.options = self._parseOptions(collection)
        self.args = self._parseArgs(collection)
        return (self.cmd, self.args, self.options)

    def _parseOptions(self, collection: list[str]) -> dict[str, int]:
        """
        Parse the user's options.
        """
        options: dict[str, int] = {}
        pointer: int = 0
        for arg in collection:
            if arg.startswith("-"):
                options[arg] = pointer
                pointer += 1
        return options
    
    def _parseArgs(self, collection: list[str]) -> dict[int, str]:
        """
        Parse the user's arguments.
        """
        args: dict[int, str] = {}
        pointer: int = 0
        for arg in collection:
            if not arg.startswith("-"):
                args[pointer] = arg
                pointer += 1
        return args

    @property
    def cmd(self) -> str | None: return self._cmd
    @cmd.setter
    def cmd(self, value: str | None) -> None: self._cmd = value

    @property
    def args(self) -> dict[str, str] | None: return self._args
    @args.setter
    def args(self, value: dict[str, str] | None) -> None: self._args = value

    @property
    def options(self) -> dict[str, str] | None: return self._options
    @options.setter
    def options(self, value: dict[str, str] | None) -> None: self._options = value       



# def promptEdit(self, prompt: str, prefill: str = None) -> str | None:
    # lines = []
    # def hook():
        # readline.insert_text(prefill + "\n" + "\n".join(lines))
        # readline.redisplay()
    # readline.set_pre_input_hook(hook)
# 
    # try:
        # while True:
            # line = input(prompt)
            # if line == "wx": break
            # if line == "q": return prefill
            # lines.append(line)
# 
    # except KeyboardInterrupt:  print("\n Done editing.")
    # finally: readline.set_pre_input_hook()
    # return "\n".join(lines)