from engine.interfaces.command import Command
from engine.core.folder import Folder
from engine.core.file import File
from typing import Optional
from rich.tree import Tree

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

        self._tree(folder, depth = 0)

    # TODO: Ignore dotfiles & dotfolders
    # TODO: Print the hex_addr attribute of each item in the tree on the far left
    def _tree(self, dir: Folder, depth: int = 0, last: bool = True) -> None:
        indent: str = "    " * depth + "├── "
        indent_final : str = "    " * depth + "└── "
        if depth == 0: self.sys.io.display.print(f"{indent_final}[{dir.hex_addr}] {dir.name}")

        else:
            if last == True or len(dir.list()) == 1: self.sys.io.display.print(f"{indent_final}[{dir.hex_addr}] {dir.name}")
            else: self.sys.io.display.print(f"{indent}[{dir.hex_addr}] {dir.name}")
            
        for item in dir.list():   
            if type(item) == Folder: self._tree(item, depth + 1, item == dir.list()[-1])
            if isinstance(item, File):
                if item == dir.list()[-1]: self.sys.io.display.print(f"    {indent_final}[{item.hex_addr}] {item.name}")
                else: self.sys.io.display.print(f"    {indent}[{item.hex_addr}] {item.name}")


