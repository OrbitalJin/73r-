from core.dotfile import DotFile
from core.system import System
from core.file import File
import inspect
import os

class Shell:
    """
    The shell is the user interface for the system.
    """
    def __init__(self, sys: System):
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
        for item in self.sys.disk.current.list(): print(item.name)
        print(
            "\n{fC} file(s), {dfC} dotFile(s), {dirC} folder(s).".format(
                fC = self.sys.disk.current.fileCount(),
                dfC = self.sys.disk.current.dotFileCount(),
                dirC = self.sys.disk.current.folderCount()
        ))

    def rm(self, args: dict = None) -> None:
        """
        Remove a file or folder.
        """
        name: str = args.get(0)
        self.sys.disk.current.remove(name = name)

    def tree(self, args: dict = None) -> None:
        """
        Display the directory structure as a tree.
        """
        self.sys.disk.current.tree()

    def pwd(self, args: dict = None) -> None:
        """
        Print the current directory's path.
        """
        print(self.sys.disk.current.path())

    def cd(self, args: dict = None) -> None:
        """
        Change directory.
        """
        path: str = args.get(0)
        self.sys.disk.navigate(path = path)

    def mkdir(self, args: dict = None) -> None:
        """
        Create a new folder.
        """
        name: str = args.get(0)
        self.sys.disk.current.createFolder(name = name)

    def touch(self, args: dict = None) -> None:
        """
        Create a new file.
        """
        name: str = args.get(0)
        self.sys.disk.current.createFile(name = name)

    def edit(self, args: dict = None) -> None:
        """
        Edit the content of a file.
        """
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file: return print(f"File not found: {name}")
        content = input("> content: ")
        file.edit(content = content)
    
    def cat(self, args: dict = None) -> None:
        """
        Display the content of a file.
        """
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file: return print(f"File not found: {name}")
        print(file.content)
    
    def clear(self, args: dict = None) -> None:
        """
        Clear the screen.
        """
        os.system("clear")
        print(self.sys)

    def help(self, args: dict = None) -> None:
        """
        Display this help message.
        """
        for cmd, data in self.cog().items():
            print(f"{cmd} - {data.get('desc')}")

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
