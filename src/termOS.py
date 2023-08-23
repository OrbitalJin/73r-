from core.collector import Collector
from core.system import System
from core.shell import Shell
from core.disk import Disk

def boot() -> (System, Shell):
    sys = System("TermOS")
    drive = Disk(name = "/")
    sys.add(drive)
    sys.mount(drive)
    shell = Shell(sys)
    return (sys, shell)

def setup(sys: System) -> None:
    drive = sys.disk
    drive.createFolder("bin", addr = sys.allocate())
    drive.createFolder("etc", addr = sys.allocate())
    var = drive.createFolder("var", addr = sys.allocate())
    var.createFolder("log", addr = sys.allocate())
    var.createFile("tmp.txt", addr = sys.allocate())
    drive.createFolder("tmp", addr = sys.allocate())

    home = drive.createFolder("home", addr = sys.allocate())
    home.createFolder("guest", addr = sys.allocate())
    home.createFolder("root", addr = sys.allocate())

    johan = home.createFolder("Johan", addr = sys.allocate())
    johan.createFile("hello.txt", addr = sys.allocate())
    johan.createFile("world.txt", addr = sys.allocate())
    johan.createFolder("Documents", addr = sys.allocate())

def loop(sys: System, shell: Shell):
    collector = Collector()
    while sys.disk:
        cmd, args = collector.prompt(f"{sys.disk.current.name} $ ")
        if cmd == "exit": break
        command = shell.cog().get(cmd)
        if not command: print(f"Unknown Command: {cmd}")
        else: command.get("func")(args = args)


if __name__ == "__main__":
    system, shell = boot()
    setup(system)
    shell.clear()
    loop(system, shell)

# def loop(sys: System, shell: Shell):
# collector = Input()
# while sys.disk:
#     cmd, args = collector.parseArgs(f"{sys.disk.current.name} $ ", ["name", "age", "height"])
#     if cmd == "exit": break
    