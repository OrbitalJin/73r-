
class MemoryBuffer:
    def __init__(self, addr: int, name: str = None, parent: "Folder" = None):
        self._addr: int = addr
        self._name: str | None = name
        self._parent: Folder | None = None

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
    def parent(self) -> "Folder": return self._parent
    @parent.setter
    def parent(self, parent: "Folder") -> None: self._parent = parent


    def __repr__(self) -> str: return f"<MemoryBuffer({self.addr})>"
    def __str__(self) -> str: return f"MemoryBuffer({self.addr})"

class Folder(MemoryBuffer):
    def __init__(self, addr: int, name: str, parent: "Folder" = None):
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

    def navigate(self, path: str) -> "Folder":
        if path not in self.children: return self
        if path == "/": return self
        return self.children[path]
    
    def tree(self, depth: int = 0):
        indent: str = "--" * depth + ">"
        print(f"{indent} {self.name}")
        if not self.list(): return
        for item in self.list():
            if isinstance(item, Folder): item.tree(depth + 1)
            else: print(f"--{indent} {item.name}")
 
    def __repr__(self) -> str: return f"<Folder({self.name})>"
    def __str__(self) -> str: return f"Folder({self.name})"

class File(MemoryBuffer):
    def __init__(self, addr: int, name: str, content: str = None, parent: Folder | None = None):
        super().__init__(addr)
        self._name: str = name
        self._content: str = content
        self._parent: Folder | None = parent

    def edit(self, content: str) -> None: self.content = content
    def path(self) -> str: return self.parent.path() + "/" + self.name

    @property
    def content(self) -> str: return self._content

    @content.setter
    def content(self, content: str) -> None: self._content = content

    def __repr__(self) -> str: return f"<File({self.name})>"
    def __str__(self) -> str: return f"File({self.name})"

class Disk(Folder):
    def __init__(self, name: str):
        super().__init__(addr = 0, name = "/", parent = None)
        self._name: str = name
        self._children: list[File | Folder] = []
        self._current: Folder | None = None

    def navigate(self, path: str) -> Folder | None:
        self.current = super().navigate(path)

    def pwd(self) -> str: return self.current.path()

    @property
    def current(self) -> Folder | None: return self._current
    @current.setter
    def current(self, current: Folder | None) -> None: self._current = current
    
    def __repr__(self) -> str: return f"<Disk({self.name})>"
    def __str__(self) -> str: return f"Disk({self.name})"

class System(MemoryBuffer):
    def __init__(self, name: str):
        super().__init__(addr = -1)
        self._name: str = name
        self._children: list[Disk] = []
        self._current: Disk | None = None
    
    def add(self, disk: Disk) -> None: self._children.append(disk)
    def mount(self, disk: Disk) -> None: self._current = disk

    @property
    def name(self) -> str: return self._name
    @name.setter
    def name(self, name: str) -> None: self._name = name    
    
    def __repr__(self) -> str: return f"<System({self.name})>"
    def __str__(self) -> str: return f"System({self.name})"


def main():
    sys = System("TermOS")
    print(sys)
    drive = Disk(name = "/")
    sys.add(drive)
    sys.mount(drive)
    drive.createFolder("bin")
    drive.createFolder("etc")
    var = drive.createFolder("var")
    var.createFolder("log")
    var.createFile("tmp.txt")
    drive.createFolder("tmp")

    home = drive.createFolder("home")
    home.createFolder("guest")
    home.createFolder("root")

    johan = home.createFolder("Johan")
    johan.createFile("hello.txt")
    johan.createFile("world.txt")
    johan.createFolder("Documents")
    drive.tree()


if __name__ == "__main__":
    main()