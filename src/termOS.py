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

def loop(sys: System, shell: Shell):
    collector = Collector()
    while sys.disk:
        cmd, args = collector.prompt(f"{sys.disk.current.name} $ ")
        if cmd == "exit": break
        cmd = shell.cog().get(cmd)
        if not cmd: print(f"Unknown Command: {cmd}")
        else: cmd.get("func")(args = args)


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
    