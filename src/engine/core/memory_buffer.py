
class MemoryBuffer:
    def __init__(self, addr: int, name: str = None, parent: "MemoryBuffer" = None):
        self._addr: int = addr
        self._hex_addr: str = f"0x{addr:02x}"
        self._name: str | None = name
        self._parent: MemoryBuffer | None = None
        self._type: str = "raw"

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
    def hex_addr(self) -> str: return self._hex_addr

    @property
    def parent(self) -> "MemoryBuffer": return self._parent
    @parent.setter
    def parent(self, parent: "MemoryBuffer") -> None: self._parent = parent

    @property
    def type(self) -> str: return self._type
    @type.setter
    def type(self, type: str) -> None: self._type = type

    def __repr__(self) -> str: return f"<MemoryBuffer({self.addr})>"
    def __str__(self) -> str: return f"MemoryBuffer({self.addr})"