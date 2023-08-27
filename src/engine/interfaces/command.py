from typing import Optional

class Command:
    def __init__(self, shell) -> None:
        self.shell = shell
        self.sys = shell.sys
        self.description: str 
        self.usage: str
        self.options: Optional[dict]

    def execute(
            self,
            args: Optional[dict] = None,
            options: Optional[dict] = {}
        ) -> None: ...
    
    def help(self) -> str:
        return f"Description: {self.description}\nUsage: {self.usage}\n{self._format_options()}"
    
    def _format_options(self) -> str:
        formatted = "Options:\n"
        for option, description in self.options.items():
            formatted += f"     {option}: {description}\n"
        return formatted

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...