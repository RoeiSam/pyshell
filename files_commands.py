"""
Purpose: Implement files related pyshell commands.
Author: Roei Samuel
Time: 01.07.25
"""
import shutil
import os
from pathlib import Path
from typing import List

HISTORY_LOCATION = -1
SOURCE = 0
DESTINATION = 1
MV_CP_ARGUMENTS_NUMBER = 3


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
    if len(arguments) == MV_CP_ARGUMENTS_NUMBER:
        try:
            shutil.copy(arguments[SOURCE], arguments[DESTINATION])
        except FileNotFoundError:
            print(f"cp: No such file as {arguments[SOURCE]}")
        except IsADirectoryError:
            print(f"cp: {arguments[SOURCE]} is a directory")
    else:
        print("Usage: cp [source] [destination]")


def mv(arguments: List[str]) -> None:
    """
    Move or rename a file or a directory.
    Usage: mv [source] [dest]
    """
    if len(arguments) == MV_CP_ARGUMENTS_NUMBER:
        try:
            shutil.move(arguments[SOURCE], arguments[DESTINATION])
        except FileNotFoundError:
            print(f"mv: No such file or directory {arguments[SOURCE]}")
        except FileExistsError:
            print(f"mv: Can't move a directory ({arguments[SOURCE]}) to a file ({arguments[DESTINATION]})")
        except shutil.Error:
            print(f"mv: Destination {arguments[DESTINATION]} already exists")
    else:
        print("Usage: mv [source] [destination]")


def mkdir(arguments: List[str]) -> None:
    """
    Create new directory.
    Usage: mkdir [filename]...
    """
    if len(arguments) <= 1:
        print("mkdir: missing directory operand")
    else:
        for directory in arguments[:HISTORY_LOCATION]:
            try:
                os.mkdir(directory)
            except FileExistsError:
                print(f"mkdir: File or directory {directory} already exists")
            except NotADirectoryError:
                print(f"mkdir: Cannot create directory ‘{directory}’: Not a directory")
            except FileNotFoundError:
                print(f"mkdir: Cannot create directory ‘{directory}’: No such file or directory")