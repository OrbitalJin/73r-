# To prevent running into circular imports when annotating, we use the __future__ module
from __future__ import annotations
import system.system as sys
from system.core.interfaces.structs import colors

from typing import Any
import readline

class AutoCompleter:
    """
    The Autocompleter is responsible for tab completion.
    """
    options: list[str]
    
    def __init__(self) -> None:
        """
        Setup tab completion.
        """
        # Set the tab completer function
        readline.set_completer(self.tabCompletionHook)
        # Enable tab completion
        readline.parse_and_bind('tab: complete')

    def setOptions(self, options: list[str]) -> None:
        """
        Set the options for tab completion.
        """
        self.options = options
        readline.set_completer(self.tabCompletionHook)
    
    # A list of commands for tab completion
    def tabCompletionHook(self, text, state):
        """
        Simple tab completer function.
        """
        options = [cmd for cmd in self.options if cmd.startswith(text)]
        return options[state] if state < len(options) else None


class Collector:
    """
    The collector is responsible for collecting user input across the system.
    """
    completer: AutoCompleter = AutoCompleter()
    def __init__(self, sys: sys.System) -> None:
        self.sys = sys
        self._cmd: str | None = None
        self._args: dict[str, str] | None = None
        self._options: dict[str, str] | None = None

    def readCmd(self) -> tuple[str | None]:
        """
        Read a command from the user.
        """
        return self.prompt(
            prompt = "{green}>>>{end} {blue}{path}{end} ".format(
                green = colors.OKGREEN,
                blue  = colors.OKCYAN,
                end   = colors.ENDC,
                path  = self.sys.fs.disk.current.path(),
            ))

    def prompt(self, prompt: str) -> tuple[str | None]:
        """
        Prompt the user for input.
        """
        entry: Any = input(prompt).strip()
        if not entry: return (None, None, None)
        self.cmd, self.args, self.options = self._parse(entry)
        return (self.cmd, self.args, self.options)

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
