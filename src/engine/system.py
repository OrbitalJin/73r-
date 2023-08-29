from engine.core.memory_buffer import MemoryBuffer
from engine.core.disk import Disk

from engine.shell.console import console

from engine.shell.shell import Shell
from engine.io.collector import Collector
from engine.io.display import Display

import pickle, time, os

class System(MemoryBuffer):
    """
    The system is the core of the operating system.
    """
    def __init__(self, name: str = "State Machine"):
        super().__init__(addr = -1)
        self._name: str = name
        self._shell: Shell = Shell(self)
        self._collector: Collector = Collector(self)
        self._display: Display = Display(self)
        self._disks: list[Disk] = []
        self._disk: Disk | None = None
        self._memPtr: int = 0
        self._author: str = "Johan & Mumei"
    
    def add(self, disk: Disk) -> None:
        """
        Add a disk to the system.
        """
        self._disks.append(disk)

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
    
    def malloc(self) -> int:
        """
        Allocate a memory address.
        """
        self._memPtr += 1
        return self._memPtr
    
    def boot(self, path: str = "./data/termOS.state") -> "System":
        """
        Boot the system.
        """
        # Attempt to load a saved state
        self.shell.clear()
        try: self.loadState(path = path)
        except FileNotFoundError: self.setup()
        return self
    
    def loop(self) -> None:
        """
        The main loop of the system.
        """
        self.shell.clear()
        try: self._loop()
        except KeyboardInterrupt: print("\n"); self.shell.exit()

    def saveState(self, path: str = "./data/termOS.state"):
        """
        Save the current state of the system to a file.
        """
        state = {
            "name": self._name,
            "shell": self._shell,
            "disks": self._disks,
            "disk": self._disk,
            "mem_ptr": self._memPtr
        }
        with open(path, 'wb') as f: pickle.dump(state, f)

    def loadState(self, path: str) -> "System":
        """
        Load the state of the system from a file.
        """
        with open(path, 'rb') as f: state = pickle.load(f)
        self._name = state["name"]
        self._shell = state["shell"]
        self._disks = state["disks"]
        self._disk = state["disk"]
        self._memPtr = state["mem_ptr"]
        return self
    
    def setup(self) -> None:
        """
        Setup the system if no saved state is found.
        """
        with console.status("No saved state found. Initializing system..."): time.sleep(3)
        os.system("mkdir -p ./data")
        # Setup the root disk
        drive = Disk(name = "/")
        self.add(drive)
        self.mount(drive)
        # Populate the root disk
        drive.createFolder("bin", addr = self.malloc())
        drive.createFolder("etc", addr = self.malloc())
        drive.createFolder("tmp", addr = self.malloc())
        # Populate the home directory with dummy users
        home = drive.createFolder("home", addr = self.malloc())
        home.createFolder("guest", addr = self.malloc())
        home.createFolder("root", addr = self.malloc())
        # Populate the root user's home directory
        user = home.createFolder("user", addr = self.malloc())
        user.createFile("Hello.txt", addr = self.malloc())
        user.createFolder("Documents", addr = self.malloc())

    def _loop(self):
        """
        Helper function for the main loop of the system.
        """
        while self.disk:
            cmd, args, options = self.collector.readCmd()
            self.shell.execute(
                cmd     = cmd,
                args    = args,
                options = options
            )
    
    @property
    def disk(self) -> Disk | None: return self._disk
    @disk.setter
    def disk(self, other: Disk): self._disk = other

    @property
    def shell(self) -> Shell: return self._shell
    @property
    def collector(self) -> Collector: return self._collector
    @property
    def display(self) -> Display: return self._display

    @property
    def author(self) -> str: return self._author
    
    def __repr__(self) -> str: return f"<System({self.name})>"
    def __str__(self) -> str: return f"System({self.name})"
