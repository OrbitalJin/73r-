from core.memory_buffer import MemoryBuffer
from core.io.collector import Collector
from core.shell import Shell
from core.disk import Disk
import pickle, time

class System(MemoryBuffer):
    """
    The system is the core of the operating system.
    """
    def __init__(self, name: str = "State Machine"):
        super().__init__(addr = -1)
        self._name: str = name
        self._shell: Shell = Shell(self)
        self._collector: Collector = Collector(self)
        self._disks: list[Disk] = []
        self._disk: Disk | None = None
        self._memPtr: int = 0
    
    def add(self, disk: Disk) -> None:
        """
        Add a disk to the system.
        """
        self._disks.append(disk)

    def mount(self, disk: Disk) -> None:
        """
        Mount a disk to the system.
        """
        self._disk = disk

    def unmount(self) -> Disk:
        """
        Unmount the current disk from the system.
        """
        disk = self._disks.pop(self._disk)
        self._disk = None
        return disk
    
    def allocate(self) -> int:
        """
        Allocate a memory address.
        """
        self._memPtr += 1
        return self._memPtr
    
    def boot(self, path: str) -> "System":
        """
        Boot the system.
        """
        # Attempt to load a saved state
        try: self.loadState(path = path)
        except FileNotFoundError: self.setup()
        return self
    
    def loop(self):
        """
        The main loop of the system.
        """
        self.shell.clear()
        while self.disk:
            cmd, args = self.collector.prompt(f"{self.disk.current.name} $ ")
            command = self.shell.cog().get(cmd)
            if not command: print(f"Unknown Command: {cmd}")
            else: command.get("func")(args = args)

    def saveState(self, path: str):
        """
        Save the current state of the system to a file.
        """
        state = {
            "name": self._name,
            "shell": self._shell,
            "collector": self._collector,
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
        self._collector = state["collector"]
        self._disks = state["disks"]
        self._disk = state["disk"]
        self._memPtr = state["mem_ptr"]
        return self
    
    def setup(self) -> None:
        """
        Setup the system if no saved state is found.
        """
        print("No saved state found. Initializing system...")
        time.sleep(2)
        # Setup the root disk
        drive = Disk(name = "/")
        self.add(drive)
        self.mount(drive)
        # Populate the root disk
        drive.createFolder("bin", addr = self.allocate())
        drive.createFolder("etc", addr = self.allocate())
        drive.createFolder("tmp", addr = self.allocate())
        # Populate the home directory with dummy users
        home = drive.createFolder("home", addr = self.allocate())
        home.createFolder("guest", addr = self.allocate())
        home.createFolder("root", addr = self.allocate())
        # Populate the root user's home directory
        user = home.createFolder("user", addr = self.allocate())
        user.createFile("Hello.txt", addr = self.allocate())
        user.createFolder("Documents", addr = self.allocate())
    
    @property
    def disk(self) -> Disk | None: return self._disk
    @disk.setter
    def disk(self, other: Disk): self._disk = other

    @property
    def shell(self) -> Shell: return self._shell
    @property
    def collector(self) -> Collector: return self._collector
    
    def __repr__(self) -> str: return f"<System({self.name})>"
    def __str__(self) -> str: return f"System({self.name})"
