from core.dotfile import DotFile
from core.folder import Folder
from core.file import File
import inspect
import os


class Shell:
    """
    The shell is the user interface for the system.
    """
    def __init__(self, sys):
        self.sys = sys
        self.cogData = self._generateCogData()

    def ls(self, args: dict = None) -> None:
        """
        List the contents of the current directory.
        """
        for item in self.sys.disk.current.list():
            print(item.name, end = " ") if not isinstance(item, DotFile) else None
        print(f"\n\n{self.sys.disk.current.fileCount()} file(s), {self.sys.disk.current.folderCount()} folder(s).")


    def ll(self, args: dict = None) -> None:
        """
        List the contents of the current directory with details.
        """
        print("parent\taddr\ttype\tname")
        for item in self.sys.disk.current.list():
            print(item.parent.name, item.addr, item.type, item.name, sep = "\t")
        print(
            "\n{fC} file(s), {dfC} dotFile(s), {dirC} folder(s).".format(
                fC = self.sys.disk.current.fileCount(),
                dfC = self.sys.disk.current.dotFileCount(),
                dirC = self.sys.disk.current.folderCount()
        ))

    # TODO: Implement options for rm e.g rm -r for recursive removal
    def rm(self, args: dict = None) -> None:
        """
        Remove a file or folder. rm <name>
        """
        if not args: return print("No file or folder name specified. Expecting: rm <options> <name>")
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
        print(self.sys.disk.current.path())

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
        if not args: return print("No folder name specified. Expecting: mkdir <name>")
        name: str = args.get(0)
        self.sys.disk.current.createFolder(name = name, addr = self.sys.allocate())

    def touch(self, args: dict = None) -> None:
        """
        Create a new file. touch <name>
        """
        if not args: return print("No file specified. Expecting: touch <name>")
        name: str = args.get(0)
        self.sys.disk.current.createFile(name = name, addr = self.sys.allocate())

    def edit(self, args: dict = None) -> None:
        """
        Edit the content of a file. edit <name>
        """
        if not args: return print("No file specified. Expecting: edit <name>")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        print(f"Editing: {file.name}")
        content = self.sys.collector.promptEdit(prompt = ">>> ", prefill = file.content)
        file.edit(content = content)
    
    def cat(self, args: dict = None) -> None:
        """
        Display the content of a file.
        """
        if not args: return print("No file specified. Expecting: cat <name>")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        print(file.content)
    
    # TODO: Implement options for find e.g find -r for recursive search
    def find(self, args: dict = None) -> None:
        """
        Recursively Find a file or folder by name. find <options> <name>
        """
        if not args: return print("No file or folder name specified. Expecting: find <name>")
        name: str = args.get(0)
        # Recursively search for the file or folder
        result = self._find(self.sys.disk.current, name)
        if not result: return print(f"File or folder not found: {name}")
        print(f"({result.addr})\t{result.path()}\t{result.type}\t{result.name}")
    
    def clear(self, args: dict = None) -> None:
        """
        Clear the screen.
        """
        os.system("clear")
        print(self.sys)

    def exit(self, args: dict = None) -> None:
        """
        Exit the system.
        """
        self.sys.saveState(path = "./data/termOS.state")
        self.sys.disk = None
        print("Saving State...")
        exit(1)

    def help(self, args: dict = None) -> None:
        """
        Display this help message.
        """
        for cmd, data in self.cog().items():
            print(f"{cmd} - {data.get('desc')}")

    def _tree(self, dir: Folder, depth: int = 0) -> None:
        if isinstance(dir, File): return
        indent: str = "--" * depth + ">"
        print(f"({dir.addr})\t{indent} {dir.name}")
        for item in dir.list():
            if isinstance(item, Folder): self._tree(item, depth + 1)
            if isinstance(item, File): print(f"({item.addr})\t--{indent} {item.name}")

    # Recursive search for a file or folder not dotfile
    def _find(self, dir: Folder, name: str) -> File | DotFile | Folder | None:
        if dir and dir.name == name and type(dir) != DotFile: return dir
        if isinstance(dir, File): return None

        for item in dir.list():
            result = self._find(item, name)
            if result: return result
        return None

    def cog(self) -> dict:
        return self.cogData

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