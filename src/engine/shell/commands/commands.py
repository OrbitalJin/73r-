from engine.shell.commands.fetch import fetch
from engine.shell.commands.addr import addr
from engine.shell.commands.tree import tree
from engine.shell.commands.find import find
from engine.shell.commands.edit import edit
from engine.shell.commands.cat import cat
from engine.shell.commands.ls import ls
from engine.shell.commands.ll import ll
from engine.shell.commands.rm import rm
from engine.shell.commands.mv import mv
import inspect

class Commands:
    def __init__(self, shell) -> None:
        self._generateCogData()

        self.fetch = fetch(shell)
        self.tree = tree(shell)
        self.find = find(shell)
        self.edit = edit(shell)
        self.addr = addr(shell)
        self.cat = cat(shell)
        self.rm = rm(shell)
        self.ls = ls(shell)
        self.ll = ll(shell)
        self.mv = mv(shell)

    def cog(self) -> dict: return self._generateCogData()
    def _generateCogData(self) -> dict:
        """
        Generate cog data from self.commands, every construction attribute is a command.
        """
        data = {}
        for cmd, obj in inspect.getmembers(self):
            if not cmd.startswith("_") and cmd != "cog":
                data[cmd] = {
                    "func": obj.execute,
                    "desc": obj.description,
                    "usage": obj.usage,
                    "options": obj.options
                }
        return data