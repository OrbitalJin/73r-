from system.core.interfaces.command import Command
from system.core.folder import Folder, DotFolder
from system.core.file import File, DotFile
from typing import Optional
from rich.tree import Tree
from rich.text import Text
from rich import print

class tree(Command):
    """
    Display the content of a folder in a tree-like structure.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.usage = "tree [path]"
        self.options = {
            "-h": "Display the help message.",
            "-a": "Display the entire system tree."
        }
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())
        if not args:
            if options and "-a" in options: folder = self.sys.fs.disk.root
            else: folder = self.sys.fs.disk.current

        else: folder = self.sys.fs.disk.current.find(name = args.get(0))
        if not folder or not isinstance(folder, Folder): return self.sys.io.display.error(f"Folder not found: {args.get(0)}")

        self._tree(folder)

    # TODO: Ignore dotfiles & dotfolders
    # TODO: Print the hex_addr attribute of each item in the tree on the far left

    def tree(self, dir: Folder,tree : Tree = Tree(""), depth : int = 0):
        if depth == 0:
            tree = Tree("[blue]" + "["+ dir.hex_addr + "] " + dir.name + "[/]")
        else:
            if len(dir.list()) == 0: color_file = "[green]"
            else: color_file = "[bold green]"

            tree = tree.add("[" + "[cyan]" + dir.hex_addr + "[/]" + "] " + color_file + dir.name + "[/]")
            
        for item in dir.list():   
            if type(item) == Folder : self.tree(item, tree, depth + 1)
            if type(item) ==  File:
                tree.add("[" +  "[cyan]" + dir.hex_addr + "[/]" + "] " + item.name)
        return tree
    def _tree(self, dir: Folder):
        self.sys.io.display.print(self.tree(dir))
