"""
Purpose: Implement files related pyshell commands.
Author: Roei Samuel
Time: 01.07.25
"""
import shutil
from pathlib import Path
from typing import List

HISTORY_LOCATION = -1
CP_SOURCE = 0
CP_DST = 1
CP_ARGUMENTS_NUMBER = 3


def touch(arguments: List[str]) -> None:
    """
    Create new file.
    Usage: touch [filename]...
    """
    if len(arguments) <= 1:
        print("touch: missing file operand")
    else:
        for file in arguments[:HISTORY_LOCATION]:
            try:
                Path.touch(file)
            except NotADirectoryError:
                print(f"touch: cannot touch '{file}': No such file or directory")


def cat(arguments: List[str]) -> str:
    """
    Print content of files.
    Usage: cat [filename]...
    """
    content = ""
    for file in arguments[:HISTORY_LOCATION]:
        try:
            with open(file, "r") as read_file:
                content = content + read_file.read() + "\n"
        except IsADirectoryError:
            print(f"cat: {file}: Is a directory")
        except FileNotFoundError:
            print(f"cat: {file}: No such file or directory")
    return content


def cp(arguments: List[str]) -> None:
    """
    Copy files and directories.
    Usage: cp [source] [destination]
    """
    if len(arguments) == CP_ARGUMENTS_NUMBER:
        try:
            shutil.copy(arguments[CP_SOURCE], arguments[CP_DST])
        except FileNotFoundError:
            print(f"cp: No such file as {arguments[CP_SOURCE]}")
        except IsADirectoryError:
            print(f"cp: {arguments[CP_SOURCE]} is a directory")
    else:
        print("Usage: cp [source] [destination]")
