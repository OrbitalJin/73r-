from engine.interfaces.command import Command
from engine.core.file import File

class edit(Command):
    """
    Edit the content of a file. edit <name>
    """
    def __init__(self, shell):
        super().__init__(shell)
        self.name = 'edit'
        self.description = 'Edit a file'
        self.help = 'Edit a file'
        self.usage = 'edit <file>'
        self.options = []

    def execute(
            self,
            args: dict | None = None,
            options: dict | None = None
        ) -> None:

        if not args: return self.sys.display.warning("No file name specified.")
        name: str = args.get(0)
        file: File = self.sys.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        self.shell.clear()
        self.sys.display.editorHeader(filename = file.name)
        content = self.sys.collector.promptEdit(prompt = ">>> ", prefill = file.content)
        file.edit(content = content)
        self.shell.clear()