# To prevent running into circular imports when annotating, we use the __future__ module
from __future__ import annotations

import engine.shell.shell as sh
import engine.system as sys

from typing import Optional

class Command:
    def __init__(self, shell: sh.Shell) -> None:
        self.shell: sh.Shell = shell
        self.sys  : sys.System = shell.sys
        self.name : str = self.__class__.__name__.lower()
        
        self.description: str = self._get_description()
        self.usage      : str
        self.options    : Optional[dict]

    def execute(
            self,
            args: Optional[dict] = {},
            options: Optional[dict] = {}
        ) -> None: ...
    
    def help(self) -> str:
        return f"Description: {self.description}\nUsage: {self.usage}\n{self._format_options()}"
    
    def _get_description(self) -> str:
        description = self.__doc__
        if not description: return "No description provided."
        return description.strip()

    def _format_options(self) -> str:
        if not self.options: return "Options: None\n"
        formatted = "Options:\n"
        for option, description in self.options.items():
            formatted += f"     {option}: {description}\n"
        return formatted

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...