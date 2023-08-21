import os
from core.system import System
from core.disk import Disk
from core.shell import Shell

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
    system.clear()

def loop(sys: System, shell: Shell):
    while sys.disk:
        request = input(f"{sys.disk.current.name} $ ").strip()
        if request == "exit": break
        cmd = shell.cog().get(request)
        if not cmd: print(f"Unknown Command: {request}")
        else: cmd.get("func")()

if __name__ == "__main__":
    system, shell = boot()
    setup(system)
    loop(system, shell)