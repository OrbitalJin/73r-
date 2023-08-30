from system.sh.commands.fetch import fetch
from system.sh.commands.addr import addr
from system.sh.commands.tree import tree
from system.sh.commands.find import find
from system.sh.commands.edit import edit
from system.sh.commands.cat import cat
from system.sh.commands.jmp import jmp
from system.sh.commands.ls import ls
from system.sh.commands.ll import ll
from system.sh.commands.rm import rm
from system.sh.commands.mv import mv
from system.sh.commands.tp import tp
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
        self.jmp = jmp(shell)
        self.rm = rm(shell)
        self.ls = ls(shell)
        self.ll = ll(shell)
        self.mv = mv(shell)
        self.tp = tp(shell)

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