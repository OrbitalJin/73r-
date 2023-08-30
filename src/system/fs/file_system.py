from __future__ import annotations
import system.system as sys

from system.core.disk import Disk

class FileSystem:
    def __init__(self, sys: sys.System):
        self._sys: sys.System = sys
        self._disks: list[Disk] = []
        self._disk: Disk = None

    def add(self, disk: Disk) -> None:
        """
        Add a disk to the system.
        """
        self._disks.append(disk)

    def eject(self, disk: Disk) -> Disk:
        """
        Eject a disk from the system.
        """
        return self._disks.pop(disk)
    
    def find(self, name: str) -> Disk | None:
        """
        Find a disk by name.
        """
        for disk in self._disks:
            if disk.name == name: return disk
        return None

    def mount(self, disk: Disk) -> None:
        """
        Mount a disk to the system.
        """
        disk.sys = self
        self._disk = disk

    def unmount(self) -> Disk:
        """
        Unmount the current disk from the system.
        """
        disk = self._disks.pop(self._disk)
        self._disk = None
        return disk
    
    @property
    def disk(self) -> Disk | None: return self._disk
    @disk.setter
    def disk(self, other: Disk): self._disk = other

    @property
    def sys(self): return self._sys