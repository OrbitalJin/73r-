from core.memory_buffer import MemoryBuffer
from core.dotfile import DotFile
from core.file import File

class Folder(MemoryBuffer):
    def __init__(self, addr: int, name: str, parent: "Folder" = "/"):
        super().__init__(addr)
        self._name: str = name
        self._parent: Folder | None = parent
        self._children: list[File | Folder] = []

    def list(self) -> list[MemoryBuffer]:
        return self._children

    def find(self, name: str) -> MemoryBuffer | None:
        for child in self._children:
            if child.name == name: return child
        return None

    def createFile(self, name: str) -> "File":
        if not name: return print("File name cannot be empty.")
        match name[0]:
            case ".": file = DotFile(addr = len(self._children), name = name, parent = self)
            case _: file = File(addr = len(self._children), name = name, parent = self)
        return self.add(file)

    def createFolder(self, name: str) -> "Folder":
        folder = Folder(addr = len(self._children), name = name, parent = self)
        self.add(folder)
        return folder

    def add(self, child: MemoryBuffer) -> MemoryBuffer:
        self._children.append(child)
        child.parent = self
        return child
    
    def remove(self, name: str) -> None:
        target = self.find(name = name)
        if not target: return print(f"File not found: {name}")
        if isinstance(target, Folder):
            if target.list(): return print(f"Folder not empty: {name}")
            else: return self._children.remove(target)
        else: return self._children.remove(target)

    def path(self) -> str:
        if self.parent is None: return "/"
        return self.parent.path() + "/" + self.name
    
    def tree(self, depth: int = 0):
        indent: str = "--" * depth + ">"
        print(f"{indent} {self.name}")
        if not self.list(): return
        for item in self.list():
            if isinstance(item, Folder): item.tree(depth + 1)
            if isinstance(item, File): print(f"--{indent} {item.name}")

    def folderCount(self) -> int:
        count = 0
        for item in self.list():
            if isinstance(item, Folder): count += 1
        return count
    
    def fileCount(self) -> int:
        count = 0
        for item in self.list():
            if isinstance(item, File): count += 1
        return count
    
    def dotFileCount(self) -> int:
        count = 0
        for item in self.list():
            if isinstance(item, DotFile): count += 1
        return count
 
    def __repr__(self) -> str: return f"<Folder({self.name})>"
    def __str__(self) -> str: return f"Folder({self.name})"