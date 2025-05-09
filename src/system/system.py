from system.core.memory_buffer import MemoryBuffer
from system.core.disk import Disk

from system.io.io_controller import IOController
from system.fs.file_system import FileSystem

from system.sh.console import console
from system.sh.shell import Shell

import pickle, time, os

class System(MemoryBuffer):
    """
    The system is the core of the operating system.
    """
    def __init__(self, name: str = "State Machine"):
        super().__init__(addr = -1)
        self._name: str = name
        self._shell: Shell = Shell(self)
        self._io: IOController = IOController(self)
        self._fs: FileSystem = FileSystem(self)
        self._memPtr: int = 0
        self._author: str = "Johan & Mumei"
        
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
        self.shell.clear()
        try: self.loadState(path = path)
        except FileNotFoundError: self.setup()
        return self
    
    def loop(self) -> None:
        """
        The main loop of the system.
        """
        self.shell.clear()
        self.shell.commands.fetch.execute(args = None, options = None)
        try: self._loop()
        except KeyboardInterrupt: print("\n"); self.shell.exit()
        # except Exception as e: self.io.display.fatal(e)
    
    def setup(self) -> None: self._boilerPlate()

    def saveState(self, path: str = os.path.join(os.getcwd(), "data", "termOS.state")) -> None:
        """
        Save the current state of the system to a file.
        """
        state = {
            "name": self._name,
            "fs": self._fs,
            "mem_ptr": self._memPtr
        }
        # Create the data directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok = True)
        with open(path, 'wb+') as f: pickle.dump(state, f)

    def loadState(self, path: str) -> "System":
        """
        Load the state of the system from a file.
        """
        with open(path, 'rb') as f: state = pickle.load(f)
        self._name = state["name"]
        self._fs = state["fs"]
        self._memPtr = state["mem_ptr"]
        return self

    def _loop(self):
        """
        Helper function for the main loop of the system.
        """
        while self.fs.disk:
            self._updateCompleter()
            cmd, args, options = self.io.collector.readCmd()
            self.shell.execute(
                cmd     = cmd,
                args    = args,
                options = options
            )

    # TODO: Implement the setup page
    def _setup(self) -> None: ...
    def _boilerPlate(self) -> None:
        """
        Helper function for the setup function.
        """
        with console.status("No saved state found. Initializing system..."): time.sleep(3)
        os.system("mkdir -p ./data")
        # Setup the root disk
        drive = Disk(name = "/")
        self.fs.add(drive)
        self.fs.mount(drive)
        # Populate the root disk
        drive.createFolder("bin", addr = self.malloc())
        drive.createFolder("tmp", addr = self.malloc())
        etc = drive.createFolder("etc", addr = self.malloc())
        etc.createFile("passwd", addr = self.malloc())
        # Populate the home directory with dummy users
        home = drive.createFolder("home", addr = self.malloc())
        home.createFolder("guest", addr = self.malloc())
        home.createFolder("root", addr = self.malloc())
        # Populate the root user's home directory
        user = home.createFolder("user", addr = self.malloc())
        user.createFile("Hello.txt", addr = self.malloc())
        user.createFolder("Documents", addr = self.malloc())

    def _updateCompleter(self) -> None:
        """
        Update the tab completion options.
        """
        self.io.collector.completer.setOptions(
            list(self.shell.cog().keys()) + [buf.name for buf in self.fs.disk.current.list()]
        )
    
    @property
    def shell(self) -> Shell: return self._shell
    @property
    def io(self) -> IOController: return self._io
    @property
    def fs(self) -> FileSystem: return self._fs
    @property
    def author(self) -> str: return self._author
    @property
    def time(self) -> str: return time.strftime("%H:%M:%S")
    
    def __repr__(self) -> str: return f"<System({self.name})>"
    def __str__(self) -> str: return f"System({self.name})"
