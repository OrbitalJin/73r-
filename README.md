# TermOS

## TODO

- [ ] Implement DotFolders
- [ ] Recursive tree using `rich`

- [x] Change folder architecture
- [x] Override keyoboardinterrupt
- [x] Implement `io` for system

  - [x] Implement `display` for system
  - [x] Implement log in system

- [x] Implement option parsing & handling
- [x] Break down `shell` into smaller components i.e. `shell`, `shellCommands` (bin, interfaces, shell.exec) that can be "attached"
- [x] Implement `fetch` in `shell`
- [x] Handle args within the imlementation of each method (within the controller object)
- [x] Find a platform agnostic alternitive to `readline`
- [x] Prettifying using Rich
- [x] Implement `history` for shell
- [x] Move booting and mainLoopEvents to `system`
- [x] Implement state saving & loading
- [x] Implement input with prefill
- [x] Outsourced `tree` to `shell`
- [x] Prevent files or folders from having the same name
- [x] Disable `find` on dotfiles
- [x] DotFile & File counting
- [x] Implement find - Recursive global search
- [x] Guard statement for Null args
- [x] HOT FIX: cd to root directory
- [x] HOT FIX: cat not working on Files
- [x] HOT FIX: edit not working on Files
- [x] HOT FIX: rm not working on Files
- [x] Unknown command None bug
- [x] Refactoring shell commands implementations
- [x] Implement DotFiles
- [x] Implement command line arguments parsing for shell commands

## Core

- [x] Memory Buffer
- [x] File
- [x] Folder
- [x] Disk
- [x] System
- [x] Basic shell
