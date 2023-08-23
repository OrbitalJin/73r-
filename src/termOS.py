from core.system import System
from core.disk import Disk
import time

def setup(sys: System) -> None:
    """
    Setup the system.
    """
    print("No saved state found. Initializing system...")
    time.sleep(4)
    # Setup the root disk
    drive = Disk(name = "/")
    sys.add(drive)
    sys.mount(drive)
    # Populate the root disk
    drive.createFolder("bin", addr = sys.allocate())
    drive.createFolder("etc", addr = sys.allocate())
    var = drive.createFolder("var", addr = sys.allocate())
    var.createFolder("log", addr = sys.allocate())
    var.createFile("tmp.txt", addr = sys.allocate())
    drive.createFolder("tmp", addr = sys.allocate())
    # Populate the home directory with dummy users
    home = drive.createFolder("home", addr = sys.allocate())
    home.createFolder("guest", addr = sys.allocate())
    home.createFolder("root", addr = sys.allocate())
    # Populate the root user's home directory
    johan = home.createFolder("Johan", addr = sys.allocate())
    johan.createFile("hello.txt", addr = sys.allocate())
    johan.createFile("world.txt", addr = sys.allocate())
    johan.createFolder("Documents", addr = sys.allocate())

def boot(path: str) -> System:
    """
    Boot the system.
    """
    sys = System("TermOS")
    # Attempt to load a saved state
    try: sys.loadState(path = path)
    except FileNotFoundError: setup(sys)
    return sys

def loop(sys: System):
    """
    The main loop of the system.
    """
    sys.shell.clear()
    while sys.disk:
        cmd, args = sys.collector.prompt(f"{sys.disk.current.name} $ ")
        command = sys.shell.cog().get(cmd)
        if not command: print(f"Unknown Command: {cmd}")
        else: command.get("func")(args = args)

# Entry point
if __name__ == "__main__":
    system: System = boot("./data/termOS.state")
    loop(system)