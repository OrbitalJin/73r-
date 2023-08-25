from core.console import console
from core.dotfile import DotFile
from core.folder import Folder
from core.file import File
import inspect, sys, os
from rich.tree import Tree

# TODO: Implement options for rm e.g rm -r for recursive removal
class Shell:
    """
    The shell is the user interface for the system.
    """
    def __init__(self, sys):
        self.sys = sys
        self._cogData = self._generateCogData()
        self._history: list[str] = []

    def warn(self, args: dict = None) -> None:
        """
        Display a warning message.
        """
        self.sys.display.warning("This is a warning message.")

    def ls(self, args: dict = None) -> None:
        """
        List the contents of the current directory.
        """
        if self.sys.disk.current.count() == 0: return console.print("[italic]Empty")

        for item in self.sys.disk.current.list():
            if type(item) == Folder: console.print(f"[bold blue]{item.name}[/]", end = " ")
            if type(item) == File: console.print(f"[green]{item.name}[/]", end = " ")
        console.print(
            "\n\n{fC} file(s), {dirC} folder(s).".format(
                fC = self.sys.disk.current.fileCount(),
                dirC = self.sys.disk.current.folderCount()
        ))        

    def ll(self, args: dict = None) -> None:
        """
        List the contents of the current directory with details.
        """
        console.print("[bold blue]Parent\tAddr\tType\tName")
        for item in self.sys.disk.current.list():
            console.print(
                "{parent}\t{addr}\t{type}\t{name}".format(
                    parent = item.parent.name if item.parent else "/",
                    type = item.type,
                    addr = item.addr,
                    name = item.name,
            ))
        
        console.print(
            "\n{fC} file(s), {dfC} .file(s), {dirC} folder(s).".format(
                fC = self.sys.disk.current.fileCount(),
                dfC = self.sys.disk.current.dotFileCount(),
                dirC = self.sys.disk.current.folderCount()
        ))

    def rm(self, args: dict = None) -> None:
        """
        Remove a file or folder. rm <name>
        """
        if not args: return self.sys.display.error("No file or folder specified.")
        name: str = args.get(0)
        self.sys.disk.current.remove(name = name)

    def tree(self, args: dict = None) -> None:
        """
        Display the directory structure as a tree.
        """
        self._tree(self.sys.disk.current, depth = 0)

    def pwd(self, args: dict = None) -> None:
        """
        Print the current directory's path.
        """
        self.sys.display.info(self.sys.disk.current.path(), bold = True)

    def cd(self, args: dict = None) -> None:
        """
        Change directory. cd <path>
        """
        # if no args, go to root
        if not args: self.sys.disk.current = self.sys.disk; return
        path: str = args.get(0)
        self.sys.disk.navigate(path = path)

    def mkdir(self, args: dict = None) -> None:
        """
        Create a new folder. mkdir <name>
        """
        if not args: return self.sys.display.warning("No folder name specified.")
        name: str = args.get(0)
        self.sys.disk.current.createFolder(name = name, addr = self.sys.allocate())

    def touch(self, args: dict = None) -> None:
        """
        Create a new file. touch <name>
        """
        if not args: return self.sys.display.warning("No file name specified.")
        name: str = args.get(0)
        self.sys.disk.current.createFile(name = name, addr = self.sys.allocate())

    def edit(self, args: dict = None) -> None:
        """
        Edit the content of a file. edit <name>
        """
        if not args: return self.sys.display.warning("No file name specified.")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        self.clear()
        self.sys.display.editorHeader(filename = file.name)
        content = self.sys.collector.promptEdit(prompt = ">>> ", prefill = file.content)
        file.edit(content = content)
        self.clear()
    
    def cat(self, args: dict = None) -> None:
        """
        Display the content of a file.
        """
        if not args: return self.sys.display.warning("No file name specified.")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        console.print(file.content)
    
    # TODO: Implement options for find e.g find -r for recursive search
    def find(self, args: dict = None) -> None:
        """
        Recursively Find a file or folder by name. find <options> <name>
        """
        if not args: return self.sys.display.warning("No file or folder name specified.")
        name: str = args.get(0)
        result = self._find(self.sys.disk.current, name)
        if not result: return print(f"File or folder not found: {name}")
        console.print(
            "{type}\t{addr}\t{path}".format(
                type = result.type,
                addr = result.addr,
                path = result.path()
        ))

    def history(self, args: dict = None) -> None:
        """
        Display the command history.
        """
        for index, cmd in enumerate(self._history): console.print(f"{index + 1}\t{cmd}")

    def clear(self, args: dict = None) -> None:
        """
        Clear the screen.
        """
        os.system("clear")
        self.sys.display.header()

    def exit(self, args: dict = None) -> None:
        """
        Exit the system.
        """
        self.sys.saveState()
        self.sys.display.log("Terminated - State Saved")
        sys.exit(0)

    def help(self, args: dict = None) -> None:
        """
        Display this help message.
        """
        for cmd, data in self._cogData.items():
            self.sys.display.print(f"[bold blue]{cmd}[/] - {data.get('desc')}")

<<<<<<< HEAD
    def _tree(self, dir: Folder, depth: int = 0, last: bool = True) -> None:
        indent: str = "    " * depth + "├── "
        indent_final : str = "    " * depth + "└── "
        if depth == 0: self.sys.display.print(f"{indent_final}{dir.name}")

        else:
            if last == True or len(dir.list()) == 1: self.sys.display.print(f"{indent_final}{dir.name}")
            else: self.sys.display.print(f"{indent}{dir.name}")
            
        for item in dir.list():   
            if isinstance(item, Folder): self._tree(item, depth + 1, item == dir.list()[-1])
            if isinstance(item, File):
                if item == dir.list()[-1]: self.sys.display.print(f"    {indent_final}{item.name}")
                else: self.sys.display.print(f"    {indent}{item.name}")

=======
    # Recursive tree traversal
    def _tree(self, dir: Folder, depth: int = 0, last: bool = True) -> None:
        indent: str = "    " * depth + "├── "
        indent_final : str = "    " * depth + "└── "

        if depth == 0:
            print(f"{indent_final}{dir.name}")
        else:
            if last == True or len(dir.list()) == 1:
                print(f"{indent_final}{dir.name}")
            else:
                print(f"{indent}{dir.name}")
        for item in dir.list():   
            if isinstance(item, Folder):
                self._tree(item, depth + 1,item == dir.list()[-1])
            if isinstance(item, File):
                if item == dir.list()[-1]:
                    print(f"    {indent_final}{item.name}")
                else:
                    if isinstance(item, File):
                        print(f"    {indent}{item.name}")
    # Recursive search for a file or folder not dotfile
>>>>>>> af406fea597d7f61c64dd8bb69a2ee9ac97a18ba
    def _find(self, dir: Folder, name: str) -> File | DotFile | Folder | None:
        """
        Helper Function for find.
        """
        if dir and dir.name == name and type(dir) != DotFile: return dir
        if isinstance(dir, File): return None

        for item in dir.list():
            result = self._find(item, name)
            if result: return result
        return None
    
    def _generateCogData(self) -> dict[str, dict]:
        methods = inspect.getmembers(self, predicate = inspect.ismethod)
        cogData = {}
        for name, method in methods:
            if not name.startswith("_") and name != "cog":
                docstring = inspect.getdoc(method)
                if docstring:
                    cogData[name] = {
                        "func": method,
                        "desc": docstring
                    }
        return cogData
    
    def cog(self, cmd: str) -> dict[str, dict] | None:
        self._history.append(cmd)
        return self._cogData.get(cmd)
<<<<<<< HEAD
    


# Rich Tree
# def _tree(self, folder: Folder, depth: int = 0) -> None:
#     """
#     Helper Function for tree.
#     """
#     if isinstance(dir, File): return
#     tree: Tree = Tree(folder.name)

#     for item in folder.list():
#         if isinstance(item, Folder): self._branch(tree, item, depth + 1)
#         elif isinstance(item, File): tree.add(item.name)

#     self.sys.display.print(tree)

# def _branch(self, tree: Tree, folder: Folder, depth: int) -> None:
#     """
#     Helper Function for tree.
#     """
#     branch: Tree = Tree(folder.name)

#     for item in folder.list():
#         if isinstance(item, Folder): self._branch(branch, item, depth + 1)
#         elif isinstance(item, File): branch.add(item.name)

#     tree.add(branch)


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
=======

    # def _tree(self, dir: Folder, depth: int = 0) -> None:
    #     if isinstance(dir, File): return
    #     indent: str = "--" * depth + ">"
    #     print(f"({dir.addr})\t{indent} {dir.name}")
    #     for item in dir.list():
    #         if isinstance(item, Folder): self._tree(item, depth + 1)
    #         if isinstance(item, File): console.print(f"({item.addr})\t--{indent} {item.name}")
    #
    #
    #
>>>>>>> af406fea597d7f61c64dd8bb69a2ee9ac97a18ba
