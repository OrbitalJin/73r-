
class MemoryBuffer:
    def __init__(self, addr: int, name: str = None, parent: "MemoryBuffer" = None):
        self._addr: int = addr
        self._name: str | None = name
        self._parent: MemoryBuffer | None = None

    def rename(self, name: str) -> None: self._name = name

    @property
    def name(self) -> str | None: return self._name
    @name.setter
    def name(self, name: str) -> None: self._name = name

    @property
    def addr(self) -> int: return self._addr
    @addr.setter
    def addr(self, addr: int) -> None: self._addr = addr

    @property
    def parent(self) -> "MemoryBuffer": return self._parent
    @parent.setter
    def parent(self, parent: "MemoryBuffer") -> None: self._parent = parent


    def __repr__(self) -> str: return f"<MemoryBuffer({self.addr})>"
    def __str__(self) -> str: return f"MemoryBuffer({self.addr})"