from system.sh.commands.fetch import fetch
from system.sh.commands.addr import addr
from system.sh.commands.tree import tree
from system.sh.commands.find import find
from system.sh.commands.edit import edit
from system.sh.commands.del_ import del_
from system.sh.commands.cat import cat
from system.sh.commands.jmp import jmp
from system.sh.commands.ls import ls
from system.sh.commands.ll import ll
from system.sh.commands.rm import rm
from system.sh.commands.mv import mv
from system.sh.commands.tp import tp
from system.sh.commands.cp import cp
import inspect

class Commands:
    """
    The commands class is a collection of all commands available in the shell.
    """
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
        self.cp = cp(shell)
        self.del_ = del_(shell)

    def cog(self) -> dict: return self._generateCogData()
    def _generateCogData(self) -> dict:
        """
        Generate cog data from self.commands, every construction attribute is a command.
        """
        data = {}
        for cmd, obj in inspect.getmembers(self):
            if not cmd.startswith("_") and cmd != "cog":
                data[obj.name] = {
                    "func": obj.execute,
                    "desc": obj.description,
                    "usage": obj.usage,
                    "options": obj.options
                }
        return data
    
    def __str__(self) -> str: return f"<Commands: {len(self.cog())}>"
    def __repr__(self) -> str: return self.__str__()