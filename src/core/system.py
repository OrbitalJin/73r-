from core.memory_buffer import MemoryBuffer
from core.dotfile import DotFile
from core.folder import Folder
from core.file import File
from core.disk import Disk
import os

class System(MemoryBuffer):
    def __init__(self, name: str):
        super().__init__(addr = -1)
        self._name: str = name
        self._disks: list[Disk] = []
        self._disk: Disk | None = None
        self._memPtr: int = 0
    
    def add(self, disk: Disk) -> None: self._disks.append(disk)
    def mount(self, disk: Disk) -> None: self._disk = disk
    def unmount(self) -> Disk:
        disk = self._disks.pop(self._disk)
        self._disk = None
        return disk
    
    def allocate(self) -> int:
        self._memPtr += 1
        return self._memPtr
    
    @property
    def name(self) -> str: return self._name
    @name.setter
    def name(self, name: str) -> None: self._name = name 
    @property
    def disk(self) -> Disk | None: return self._disk
    @disk.setter
    def disk(self, other: Disk): self._disk = other
    
    def __repr__(self) -> str: return f"<System({self.name})>"
    def __str__(self) -> str: return f"System({self.name})"
