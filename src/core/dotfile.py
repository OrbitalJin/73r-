from core.file import File
from core.memory_buffer import MemoryBuffer

class DotFile(File):
    def __init__(
            self,
            addr: int,
            name: str,
            content: str = None,
            parent: MemoryBuffer = None
            ):
        super().__init__(
            addr = addr,
            name = name,
            content = content,
            parent = parent
        )
