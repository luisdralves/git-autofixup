# git-autofixup

Automatically fixup changed files to the right commits.

## Demo
[![asciicast](https://asciinema.org/a/R6uSGgWxSk9EcaUAVPk9xbQ03.svg)](https://asciinema.org/a/R6uSGgWxSk9EcaUAVPk9xbQ03)

## Usage
 - Copy the script somewhere (i.e. `~/.git-utils/git-autofixup.py`)
 - Mark as executable `chmod +x ~/.git-utils/git-autofixup.py`
 - Add this alias to your git config: `autofixup = !sh -c 'git add . && git stp | ~/.git-utils/git-autofixup.py'`

This script requires `status-plus`
