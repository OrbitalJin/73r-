from typing import Any

class Collector:
    def prompt(self, prompt: str) -> tuple[str] | None:
        entry: Any = input(prompt)
        if not entry: return None
        collection: list[str] = entry.split()
        if len(collection) == 1: return (collection[0], None)
        cmd, *args = collection
        return (cmd, {
                    index: arg
                    for index, arg in enumerate(args)
            })

if __name__ == "__main__":
    inputManager = Collector()
    cmd, args = inputManager.prompt("> ")
    print(cmd, args)