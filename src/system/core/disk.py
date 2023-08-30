from __future__ import annotations
import system.system as sys

from system.core.folder import Folder
from system.core.file import File

class Disk(Folder):
    def __init__(self, name: str, sys: sys.System = None):
        super().__init__(addr = 0, name = "/", parent = None)
        self._fs: sys.System = sys
        self._name: str = name
        self._root: Folder = self
        self._children: list[File | Folder] = []
        self._current: Folder | None = self
        self._currentPath: str = "/"

    def list(self) -> list[File | Folder]: return self._children

    def navigate(self, path: str) -> Folder | None:
        if path == "..":
            self._current = self._current.parent if self._current.parent else self._current
            return self._current
        
        folder = self._current.find(path)
        if not folder or not isinstance(folder, Folder): return self.sys.io.display.warning("No such directory in .")
        self._current = folder
        return self._current
    
    @property
    def current(self) -> Folder | None: return self._current
    @current.setter
    def current(self, current: Folder | None) -> None: self._current = current

    @property
    def root(self) -> Folder: return self._root

    @property
    def sys(self): return self._sys
    @sys.setter
    def sys(self, sys) -> None: self._sys = sys
    
    def __repr__(self) -> str: return f"<Disk({self.name})>"
    def __str__(self) -> str: return f"Disk({self.name})"
