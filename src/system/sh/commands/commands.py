from system.core.interfaces.command import Command
from system.sh.commands.fetch import fetch
from system.sh.commands.tedit import tedit
from system.sh.commands.clock import clock
from system.sh.commands.addr import addr
from system.sh.commands.tree import tree
from system.sh.commands.find import find
from system.sh.commands.read import read
from system.sh.commands.del_ import del_
from system.sh.commands.jmp import jmp
from system.sh.commands.ls import ls
from system.sh.commands.ll import ll
from system.sh.commands.rm import rm
from system.sh.commands.mv import mv
from system.sh.commands.tp import tp
from system.sh.commands.cp import cp
from typing import Any

class Commands:
    def __init__(self, shell) -> None:
        self.commands: dict[str, Any] = {}
        self.shell = shell
        self.attach(fetch(shell))
        self.attach(tedit(shell))
        self.attach(clock(shell))
        self.attach(tree(shell))
        self.attach(find(shell))
        self.attach(addr(shell))
        self.attach(read(shell))
        self.attach(jmp(shell))
        self.attach(rm(shell))
        self.attach(ls(shell))
        self.attach(ll(shell))
        self.attach(mv(shell))
        self.attach(tp(shell))
        self.attach(cp(shell))
        self.attach(del_(shell))

    def attach(self, command: Command) -> None:
        """
        Attach a custom command to the shell.
        """
        assert isinstance(command, Command), "Command must be an instance of Command."
        self.commands[command.name] = {
            "func": command.execute,
            "desc": command.description,
            "usage": command.usage,
            "options": command.options
        }
        # so that it can be accessed as a property i.e. shell.commands.<command>
        setattr(self, command.name, command)

    def cog(self) -> dict:
        return self.commands

    def __str__(self) -> str:
        return f"<Commands: {len(self.commands)}>"

    def __repr__(self) -> str:
        return self.__str__()