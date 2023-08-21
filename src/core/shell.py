from core.system import System
from core.file import File

class Shell:
    def __init__(self, sys: System):
        self.sys = sys

    def ls(self):
        self.sys.ls()

    def tree(self):
        self.sys.disk.current.tree()

    def pwd(self):
        print(self.sys.disk.current.path())

    def cd(self):
        path = input("> path: ").strip()
        self.sys.disk.navigate(path = path)

    def mkdir(self):
        name = input("> name: ")
        self.sys.disk.current.createFolder(name = name)

    def touch(self):
        name = input("> name: ")
        self.sys.disk.current.createFile(name = name)

    def edit(self):
        name = input("> name: ")
        file: File = self.sys.disk.current.find(name = name)
        if not file: return print(f"File not found: {name}")
        content = input("> content: ")
        file.edit(content = content)
    
    def cat(self):
        name = input("> name: ")
        file: File = self.sys.disk.current.find(name = name)
        if not file: return print(f"File not found: {name}")
        print(file.content)
    
    def clear(self):
        self.sys.clear()

    def help(self):
        for cmd, data in self.cog().items():
            print(f"{cmd} - {data.get('desc')}")

    def cog(self):
        return  {
        "ls": {
            "func": self.ls,
            "desc": "List the contents of the current directory.",
        },
        "tree": {
            "func": self.tree,
            "desc": "Display the directory structure as a tree.",
        },
        "pwd": {
            "func": self.pwd,
            "desc": "Print the current directory's path.",
        },
        "cd": {
            "func": self.cd,
            "desc": "Change directory.",
        },
        "mkdir": {
            "func": self.mkdir,
            "desc": "Create a new folder.",
        },
        "touch": {
            "func": self.touch,
            "desc": "Create a new file.",
        },
        "edit": {
            "func": self.edit,
            "desc": "Edit the content of a file.",
        },
        "cat": {
            "func": self.cat,
            "desc": "Display the content of a file.",
        },
        "clear": {
            "func": self.clear,
            "desc": "Clear the screen.",
        },
        "help": {
            "func": self.help,
            "desc": "Display this help message.",
        },
    }