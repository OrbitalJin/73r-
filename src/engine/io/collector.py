from engine.shell.console import console
from engine.interfaces.structs import colors
from typing import Any
import readline

class Collector:
    def __init__(self, sys) -> None:
        self.sys = sys
        self.cmd: str | None = None
        self.args: dict[str, str] | None = None

    def readCmd(self) -> tuple[str] | None:
        cmd, args  = self.prompt(
            prompt = "{green}>>>{end} {blue}{path}{end} ".format(
                green = colors.OKGREEN,
                blue  = colors.OKCYAN,
                end   = colors.ENDC,
                path  = self.sys.disk.current.path(),
            ))
        return (
            cmd if cmd else None,
            args if args else None
            )

    def prompt(self, prompt: str) -> tuple[str] | None:
        entry: Any = input(prompt)
        if not entry: return (None, None)
        collection: list[str] = entry.split()
        if len(collection) == 1: return (collection[0], None)
        cmd, *args = collection
        self.cmd = cmd
        self.args = {
            index: arg
            for index, arg in enumerate(args)
        }
        return (self.cmd, self.args)
    
    def promptEdit(self, prompt: str = "", prefill: str = None) -> str | None:
        def hook():
            readline.insert_text(prefill)
            readline.redisplay()

        readline.set_pre_input_hook(hook)
        result = input(prompt)
        readline.set_pre_input_hook()
        return result
        
    def getCmd(self) -> str | None: return self.cmd
    def getArgs(self) -> dict[str, str] | None: return self.args


# def promptEdit(self, prompt: str, prefill: str = None) -> str | None:
    # lines = []
    # def hook():
        # readline.insert_text(prefill + "\n" + "\n".join(lines))
        # readline.redisplay()
    # readline.set_pre_input_hook(hook)
# 
    # try:
        # while True:
            # line = input(prompt)
            # if line == "wx": break
            # if line == "q": return prefill
            # lines.append(line)
# 
    # except KeyboardInterrupt:  print("\n Done editing.")
    # finally: readline.set_pre_input_hook()
    # return "\n".join(lines)