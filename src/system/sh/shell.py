# To prevent running into circular imports, we use the __future__ module
from __future__ import annotations
import system.system as sys

from system.sh.commands import Commands
from system.sh.console import console
import inspect, sys, os, platform

# TODO: Implement options for rm e.g rm -r for recursive removal
class Shell:
    """
    The shell is the user interface for the system.
    """
    def __init__(self, sys: sys.System):
        self.sys = sys
        self._commands: Commands   = Commands(self)
        self._cogData : dict[dict] = self._generateCogData()
        self._history : list[str]  = []

    def say(self, args: dict = None, options: dict = None) -> None:
        """
        Print a message to the screen.
        """
        if not args: return self.sys.io.display.warning("No message specified.")
        self.sys.io.display.print(" ".join(args.values()))

    def cd(self, args: dict = None, options: dict = None) -> None:
        """
        Change directory.
        """
        # if no args, go to root
        if not args: self.sys.fs.disk.current = self.sys.fs.disk; return
        path: str = args.get(0)
        self.sys.fs.disk.navigate(path = path)

    def pwd(self, args: dict = None, options: dict = None) -> None:
        """
        Print the current directory's path.
        """
        self.sys.io.display.info(self.sys.fs.disk.current.path(), bold = True)

    def mkdir(self, args: dict = None, options: dict = None) -> None:
        """
        Create a new folder.
        """
        if not args: return self.sys.io.display.warning("No folder name specified.")
        name: str = args.get(0)
        self.sys.fs.disk.current.createFolder(name = name, addr = self.sys.malloc())

    def touch(self, args: dict = None, options: dict = None) -> None:
        """
        Create a new file.
        """
        if not args: return self.sys.io.display.warning("No file name specified.")
        name: str = args.get(0)
        self.sys.fs.disk.current.createFile(name = name, addr = self.sys.malloc())

    def clear(self, args: dict = None, options: dict = None) -> None:
        """
        Clear the screen.
        """
        match platform.platform():
            case "Windows": os.system("cls")
            case _: os.system("clear")
        self.sys.io.display.header()

    def exit(self, args: dict = None, options: dict = None) -> None:
        """
        Exit the system.
        """
        self.sys.io.display.log("Terminated - State Saved")
        self._exit()

    def man(self, args: dict = None, options: dict = None) -> None:
        """
        Display this manual.
        """
        for cmd, data in self._cogData.items():
            self.sys.io.display.print(
                "[bold blue]{cmd}[/] \t {desc}".format(
                    cmd  = cmd,
                    desc = data.get("desc")
                ))
            
    def record(self, args: dict = None, options: dict = None) -> None:
        """
        Display the command history.
        """
        for index, cmd in enumerate(self._history): console.print(f"{index + 1}\t{cmd}")


    def execute(self, cmd: str, args: dict = None, options: dict = None) -> None:
        self._history.append(cmd)
        if cmd in self.cog().keys(): self.cog()[cmd].get("func")(args, options)
        else: self.sys.io.display.error(f"Command '{cmd}' not found.")

    def cog(self) -> dict: return self._cogData

    def _exit(self) -> None:
        self.sys.saveState()
        sys.exit(0)

    def _generateCogData(self) -> dict:
        """
        Generate cog data from self.commands, every construction attribute is a command.
        """
        data = self.commands.cog()
        for cmd, obj in inspect.getmembers(self, predicate = inspect.ismethod):
            if not cmd.startswith("_") and cmd != "cog" and cmd != "execute":
                data[cmd] = {
                    "func": obj,
                    "desc": inspect.getdoc(obj),
                }
        return data
    

    @property
    def commands(self) -> Commands: return self._commands
    @property   
    def history(self) -> list: return self._history
    


# def _tree(self, folder: Folder, depth: int = 0) -> None:
    # """
    # Helper Function for tree.
    # """
    # if isinstance(folder, File): return
    # tree: Tree = Tree(f"[bold blue]{folder.name}[/]")
# 
    # for item in folder.list():
        # if isinstance(item, Folder): self._branch(tree, item, depth + 1)
        # elif isinstance(item, File): tree.add(f"[green]{item.name}[/]")
# 
    # self.sys.io.display.print(tree)
# 
# def _branch(self, tree: Tree, folder: Folder, depth: int) -> None:
    # """
    # Helper Function for tree.
    # """
    # branch: Tree = Tree(f"[bold blue]{folder.name}[/]")
# 
    # for item in folder.list():
        # if isinstance(item, Folder): self._branch(branch, item, depth + 1)
        # elif isinstance(item, File): branch.add(f"[green]{item.name}[/]")
# 
    # tree.add(branch)


#def _tree(self, dir: Folder, depth: int = 0) -> None:
#     if isinstance(dir, File): return
#     indent: str = "--" * depth + ">"
#     print(f"({dir.addr})\t{indent} {dir.name}")
#     for item in dir.list():
#         if isinstance(item, Folder): self._tree(item, depth + 1)
#         if isinstance(item, File): console.print(f"({item.addr})\t--{indent} {item.name}")
#
#
#
