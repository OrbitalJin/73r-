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
            options: Optional[dict] = None
        ) -> None: ...
    
    def help(self) -> str:
        return f"""
        {self.name} - {self.description}
        Usage: {self.usage}
        Options: {self.options}
        """


    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...