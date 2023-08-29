from engine.core.memory_buffer import MemoryBuffer
from engine.core.file import File, DotFile

class Folder(MemoryBuffer):
    """
    A folder.
    """
    def __init__(self, addr: int, name: str, parent: "Folder" = "/"):
        super().__init__(addr)
        self._name: str = name
        self._type: str = "dir"
        self._parent: Folder | None = parent
        self._children: list[File | Folder] = []

    def list(self) -> list[MemoryBuffer]:
        return self._children

    def find(self, name: str) -> MemoryBuffer | None:
        for child in self._children:
            if child.name == name: return child
        return None

    def createFile(self, name: str, addr: int) -> File | DotFile:
        if not name: return print("File name cannot be empty.")
        if self.find(name = name): return print(f"Name already in use: {name}")
        match name[0]:
            case ".": file = DotFile(addr = addr, name = name, parent = self)
            case _: file = File(addr = addr, name = name, parent = self)
        return self.add(file)

    def createFolder(self, name: str, addr: int) -> "Folder":
        if not name: return print("File name cannot be empty.")
        if self.find(name = name): return print(f"Name already in use: {name}")
        match name[0]:
            case ".": folder = DotFolder(addr = addr, name = name, parent = self)
            case _: folder = Folder(addr = addr, name = name, parent = self)
        return self.add(folder)

    def add(self, child: MemoryBuffer) -> MemoryBuffer:
        self._children.append(child)
        child.parent = self
        return child
    
    def remove(self, name: str) -> None:
        target = self.find(name = name)
        if not target: return print(f"File not found: {name}")
        if isinstance(target, Folder) and not target.isEmpty(): return print(f"Folder not empty: {name}")
        else: return self._children.remove(target)

    def path(self) -> str:
        if self.parent is None: return "/"
        return self.parent.path() + self.name + "/"

    def folderCount(self) -> int:
        count = 0
        for item in self.list():
            if isinstance(item, Folder): count += 1
        return count
    
    def fileCount(self) -> int:
        count = 0
        for item in self.list():
            if type(item) == File: count += 1
        return count
    
    def dotFileCount(self) -> int:
        count = 0
        for item in self.list():
            if type(item) == DotFile: count += 1
        return count
    
    def count(self) -> int:
        return len(self.list())
    
    def isEmpty(self) -> bool:
        return len(self.list()) == 0
 
    def __repr__(self) -> str: return f"<Folder({self.name})>"
    def __str__(self) -> str: return f"Folder({self.name})"


class DotFolder(Folder):
    """
    A folder that starts with a dot.
    """
    def __init__(
            self,
            addr: int,
            name: str,
            parent: MemoryBuffer = None
            ):
        super().__init__(
            addr = addr,
            name = name,
            parent = parent
        )
