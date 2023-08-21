from core.folder import Folder
from core.file import File

class Disk(Folder):
    def __init__(self, name: str):
        super().__init__(addr = 0, name = "/", parent = None)
        self._name: str = name
        self._children: list[File | Folder] = []
        self._current: Folder | None = self
        self._currentPath: str = "/"

    def pwd(self) -> str: return self._currentPath

    def navigate(self, path: str) -> Folder | None:
        if path == "..":
            self._current = self._current.parent if self._current.parent else self._current
            return self._current
        
        dir = self.find(path)
        if not dir: return print("No such directory in .")
        self._current = dir

    def find(self, name: str) -> Folder | None:
        if not self._current: return "/"
        for dir in self._current.list():
            if isinstance(dir, Folder):
                if dir.name == name: return dir
        return None

    @property
    def current(self) -> Folder | None: return self._current
    @current.setter
    def current(self, current: Folder | None) -> None: self._current = current
    
    def __repr__(self) -> str: return f"<Disk({self.name})>"
    def __str__(self) -> str: return f"Disk({self.name})"
