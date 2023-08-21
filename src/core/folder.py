from core.memory_buffer import MemoryBuffer
from core.file import File

class Folder(MemoryBuffer):
    def __init__(self, addr: int, name: str, parent: "Folder" = "/"):
        super().__init__(addr)
        self._name: str = name
        self._parent: Folder | None = parent
        self._children: list[File | Folder] = []

    def list(self) -> list[MemoryBuffer]: return self._children
    def find(self, name: str) -> MemoryBuffer | None:
        for child in self._children:
            if child.name == name: return child
        return None

    def createFile(self, name: str) -> "File":
        file = File(addr = len(self._children), name = name, parent = self)
        self.add(file)
        return file

    def createFolder(self, name: str) -> "Folder":
        folder = Folder(addr = len(self._children), name = name, parent = self)
        self.add(folder)
        return folder

    def add(self, child: MemoryBuffer) -> None:
        self._children.append(child)
        child.parent = self

    def path(self) -> str:
        if self.parent is None: return "/"
        return self.parent.path() + "/" + self.name
    
    def tree(self, depth: int = 0):
        indent: str = "--" * depth + ">"
        print(f"{indent} {self.name}")
        if not self.list(): return
        for item in self.list():
            if isinstance(item, Folder): item.tree(depth + 1)
            else: print(f"--{indent} {item.name}")
 
    def __repr__(self) -> str: return f"<Folder({self.name})>"
    def __str__(self) -> str: return f"Folder({self.name})"