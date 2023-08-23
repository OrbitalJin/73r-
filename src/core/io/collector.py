from typing import Any
import readline

class Collector:
    def __init__(self, sys) -> None:
        self.sys = sys
        self.cmd: str | None = None
        self.args: dict[str, str] | None = None

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
    
    def promptEdit(self, prompt: str, prefill: str = None) -> str | None:
        def hook():
            readline.insert_text(prefill)
            readline.redisplay()

        readline.set_pre_input_hook(hook)
        return input(prompt)
    
    def getCmd(self) -> str | None: return self.cmd
    def getArgs(self) -> dict[str, str] | None: return self.args

if __name__ == "__main__":
    inputManager = Collector()
    cmd, args = inputManager.prompt("> ")
    print(cmd, args)