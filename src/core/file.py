from core.memory_buffer import MemoryBuffer

class File(MemoryBuffer):
    def __init__(self, addr: int, name: str, content: str = None, parent: MemoryBuffer = None):
        super().__init__(addr)
        self._name: str = name
        self._content: str = content
        self._parent: MemoryBuffer | None = parent
        self.name = name

    def edit(self, content: str) -> None: self.content = content
    def path(self) -> str: return self.parent.path() + self.name + "/" 

    @property
    def content(self) -> str: return self._content

    @content.setter
    def content(self, content: str) -> None: self._content = content

    @property
    def name(self) -> str: return self._name
    @name.setter
    def name(self, name: str) -> None:
        if "." in name:
            self._name = name
            self._type = name.split(".")[-1]

    def __repr__(self) -> str: return f"<File({self.name})>"
    def __str__(self) -> str: return f"File({self.name})"

