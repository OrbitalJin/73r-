from engine.interfaces.command import Command
from engine.core.file import File
from typing import Optional

class edit(Command):
    """
    Edit the content of a file.
    """
    def __init__(self, shell):
        super().__init__(shell)
        self.usage = 'edit <file>'
        self.options = {"-h": "Display the help message."}

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.display.print(self.help())

        if not args: return self.sys.display.warning("No file name specified. Use -h for help")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        self.shell.clear()
        self.sys.display.editorHeader(filename = file.name)
        content = self.sys.collector.promptEdit(prompt = ">>> ", prefill = file.content)
        file.edit(content = content)
        self.shell.clear()