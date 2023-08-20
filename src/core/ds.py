
class Node:
    """Node class for FileTree"""
    def __init__(self, name: str, content: str, type: str = "dir") -> None:
        self._name    : str  = name
        self._content : str = content
        self._type    : str  = type
        self._parent  : Node = None
        self._children: list[Node] = []

    def cat(self) -> str: return self.content
    def edit(self, content: str) -> None: self.content = content
    def rename(self, name: str) -> None: self.name = name
    def changeType(self, type: str) -> None: self.type = type

    @property
    def name(self) -> str: return self._name
    @property
    def parent(self) -> "Node": return self._parent
    @property
    def type(self) -> str: return self._type
    @property
    def content(self) -> str: return self._content

    @name.setter
    def name(self, name: str) -> None: self._name = name
    @parent.setter
    def parent(self, parent: "Node") -> None: self._parent = parent
    @type.setter
    def type(self, type: str) -> None: self._type = type
    @content.setter
    def content(self, content: str) -> None: self._content = content

class FileTree:
    def __init__(self, root: Node | None = None) -> None | Node:
        self.root: Node | None = root
