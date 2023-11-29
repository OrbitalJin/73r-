from __future__ import annotations
import system.sh.shell as sh

from system.core.interfaces.command import Command
from system.core.file import File
from typing import Optional

class tedit(Command):
    """
    Edit the content of a file.
    """
    def __init__(self, shell: sh.Shell):
        super().__init__(shell)
        self.usage = 'tedit <file>'
        self.options = {"-h": "Display the help message."}

    def execute(self, args: Optional[dict], options: Optional[dict]) -> None:
        if options and "-h" in options: return self.sys.io.display.print(self.help())

        if not args: return self.sys.io.display.warning("No file name specified. Use -h for help")
        name: str = args.get(0)
        file: File = self.sys.fs.disk.current.find(name = name)
        if not file or not isinstance(file, File): return print(f"File not found: {name}")
        app = TEdit(
            filename = file.name,    
            content  = file.content,
            type     = file.type
        )
        app.run()
        file.content = app.content

from textual.app import App, ComposeResult
from textual.widgets import Footer, TextArea, Label
from textual.containers import Center
from textual.binding import Binding
from textual import on

# This is the acutal application
class TEdit(App):
    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Quit."),
        Binding(key="ctrl+s", action="save", description="Save."),
    ]
    lang: dict[str, str] = {
        "py": "python",
        "md": "markdown",
        "toml": "toml",
        "yaml": "yaml",
        "json": "json",
        "html": "html",
        "css": "css",
        "sql": "sql",
    }
    def __init__(
            self,
            filename: str = None,
            content: str = None,
            type: str = None,
        ):
        super().__init__()
        self.content: str = content or ""
        self.filename: str = filename or ""
        self.type: str = type or ""
        self.placeholder: str = f"[bold] tedit[/] - Editing [underline]{self.filename}[/]"
        self.setupWidget()

    # Setup the widgets
    def setupWidget(self):
        self.TitleBar = Label(self.placeholder)
        self.TextArea = TextArea(
            text = self.content,
            language = self.lang.get(self.type, "markdown")
        )
        self.Doc = self.TextArea.document
        self.TextArea.move_cursor((
            self.Doc.line_count - 1,
            len(self.Doc.get_line(self.Doc.line_count - 1)),
        ))
        self.Footer = Footer()

    # Render the application
    def compose(self) -> ComposeResult:
        with Center(): yield self.TitleBar
        yield self.TextArea
        yield self.Footer

    # Actions
    def action_save(self):
        self.placeholder = f"[bold] tedit[/] - Editing [underline]{self.filename}[/]"
        self.TitleBar.update(self.placeholder)
        self.content = self.TextArea.text

    # Events
    @on(TextArea.Changed)
    def text_area_changed(self, value: str):
        self.placeholder = f"[bold](*) tedit[/] - Editing [underline]{self.filename}[/]"
        self.TitleBar.update(self.placeholder)