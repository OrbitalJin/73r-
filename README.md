# TermOS

termos is a lightweight, cross-platform, open-source, terminal-based operating system written in python. it is a "ring 0" operating system, meaning that it is the first program to run when the computer boots up. it is designed to be a simple, yet powerful, and extensible providing a documented sdk enabling user to extend the operating system with their own custom shell commands and apps.

## Arch

Architectural overview of the project using mermaid class diagrams

```mermaid
classDiagram
    class System {
        IOController
        FileSystem
        Shell
        boot()
        malloc()
        loop()
        saveState()
        loadState()
    }

    class FileSystem {
        disk
        disks
        add()
        eject()
        mount()
        unmount()
    }

    class Shell {
        Commands
        CogData
        exec()
        exit()
        cd()
        clear()
        touch()
        mkdir()
        history()
    }

    class Commands {
        CogData
        ls(), ll()
        cat(), edit()
        rm(), mv()
        find(), tree()
        addr(), jmp()
        fetch()
    }

    class IOController {
        Display
        Collector
        *exists()
        *isFile()
        *isFolder()
        *isDotFile()
        *isDotFolder()
    }

    class Collector {
        readCmd()
        prompt()
        parseArgs()
        parseCmd()
        parseOptions()
    }

    class Display {
        print(), printLn()
        error(), warning()
        success(), info()
    }

    class Core {
        MemoryBuffer
        File
        Folder
        Disk
        DotFolders
        DotFiles
    }

    System <|-- Shell
    System <|-- IOController
    System <|-- FileSystem
    System <|--> Core
    Shell <|-- Commands
    IOController <|-- Collector
    IOController <|-- Display

```

## Core

-   [x] Memory Buffer
-   [x] File
-   [x] Folder
-   [x] Disk
-   [x] DotFolders
-   [x] DotFiles
-   [x] System
-   [x] Shell

## Shell

-   [x] Implement `runpy` command 
-   [x] Implement `clock` app 
-   [x] Implement `tedit` app 
-   [x] Implement `del` command (_Not thoroughly tested_)
-   [x] Implement `cp` command (_Not thoroughly tested_)
-   [x] Implement `tp` command
-   [x] Implement `jmp` command
-   [x] Implement `addr` command
-   [x] Implement `mv` command
-   [x] Implement `fetch`
-   [x] Implement `rm` command
-   [x] Implement `find` command
-   [x] Implement `history` command
-   [x] Implement `cat` command
-   [x] Implement `edit` command
-   [x] Implement `cd` command
-   [x] Implement `tree` command
-   [x] Implement `ll` command
-   [x] Implement `ls` command
-   [x] Implement `mkdir` command
-   [x] Implement `touch` command
-   [x] Implement `clear` command
-   [x] Implement `exit` command

## System

-   [x] Implement `io` for system
-   [x] Implement state saving & loading
-   [x] Override KeyboardInterrupt
-   [x] Migrate from `disk` to `fs` architecture

## IOController

-   [x] Implement `IOController` for system
-   [x] Implement `Collector` for system
-   [x] Implement `display` for system

# TODO

-   [ ] Implement `env` variables
-   [ ] Recursive tree using `rich` (hide dotfiles & dotfolders)
-   [ ] Implement user setup
-   [x] Implemented context a-somewhat-conext-aware tab completion
-   [x] Improved the `read` command (richified)
-   [x] Implemented `tedit` command
-   [x] SDK for creating custom shell commands & apps
-   [x] Implement `echo` command
-   [x] Implement option parsing & handling
-   [x] Handle args within the imlementation of each method (within the controller object)
-   [x] Change folder architecture
-   [x] Find a platform agnostic alternitive to `readline`
-   [x] Prettifying using Rich
-   [x] Move booting and mainLoopEvents to `system`
-   [x] Implement input with prefill
-   [x] Break down `shell` into smaller components i.e. `shell`, `shellCommands` (bin, interfaces, shell.exec) that can be "attached"
-   [x] Outsourced `tree` to `shell`
-   [x] Prevent files or folders from having the same name
-   [x] Disable `find` on dotfiles
-   [x] DotFile & File counting
-   [x] Guard statement for Null args
-   [x] Unknown command None bug
-   [x] Refactoring shell commands implementations
-   [x] Implement command line arguments parsing for shell commands

# Hot Fixes

-   [x] HOT FIX: `tp` crash when arg[0] is not a number
-   [x] HOT FIX: `mv` command, check if file or folder exists in destination
-   [x] HOT FIX: `cp` command, check if file or folder exists in destination
-   [x] HOT FIX: cd to root directory
-   [x] HOT FIX: cat not working on Files
-   [x] HOT FIX: edit not working on Files
-   [x] HOT FIX: rm not working on Files
