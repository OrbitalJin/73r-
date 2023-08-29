from engine.interfaces.command import Command
from engine.core.folder import Folder
from engine.core.file import File
from typing import Optional

class tree(Command):
    """
    Display the current directory tree.
    """
    def __init__(self, shell) -> None:
        super().__init__(shell)
        self.usage = "tree"
        self.options = {
            "-h": "Display the help message."
        }
    
    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        self._tree(self.sys.disk.current, depth = 0)

    # TODO: Ignore dotfiles & dotfolders
    def _tree(self, dir: Folder, depth: int = 0, last: bool = True) -> None:
        indent: str = "    " * depth + "├── "
        indent_final : str = "    " * depth + "└── "
        if depth == 0: self.sys.io.display.print(f"{indent_final}{dir.name}")

        else:
            if last == True or len(dir.list()) == 1: self.sys.io.display.print(f"{indent_final}{dir.name}")
            else: self.sys.io.display.print(f"{indent}{dir.name}")
            
        for item in dir.list():   
            if type(item) == Folder: self._tree(item, depth + 1, item == dir.list()[-1])
            if isinstance(item, File):
                if item == dir.list()[-1]: self.sys.io.display.print(f"    {indent_final}{item.name}")
                else: self.sys.io.display.print(f"    {indent}{item.name}")