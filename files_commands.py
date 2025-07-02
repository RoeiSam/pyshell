"""
Purpose: Implement files related pyshell commands.
Author: Roei Samuel
Time: 01.07.25
"""
import shutil
import os
from pathlib import Path
from typing import List, Union

HISTORY_LOCATION = -1
SOURCE = 0
DESTINATION = 1
MV_CP_ARGUMENTS_NUMBER = 3


def touch(arguments: List[str]) -> Union[str, None]:
    """
    Create new file.
    Usage: touch [filename]...
    """
    exceptions = ""
    if len(arguments) <= 1:
        exceptions += "touch: missing file operand"
    else:
        for file in arguments[:HISTORY_LOCATION]:
            try:
                Path.touch(file)
            except FileNotFoundError:
                exceptions += f"touch: cannot touch '{file}': No such file or directory\n"
    return exceptions


def cat(arguments: List[str]) -> str:
    """
    return  content of files.
    Usage: cat [filename]...
    """
    content = ""
    for file in arguments[:HISTORY_LOCATION]:
        try:
            with open(file, "r") as read_file:
                content = content + read_file.read() + "\n"
        except IsADirectoryError:
            content += f"cat: {file}: is a directory\n"
        except FileNotFoundError:
            content += f"cat: {file}: no such file or directory\n"
    return content


def cp(arguments: List[str]) -> Union[str, None]:
    """
    Copy files and directories.
    Usage: cp [source] [destination]
    """
    if len(arguments) == MV_CP_ARGUMENTS_NUMBER:
        try:
            shutil.copy(arguments[SOURCE], arguments[DESTINATION])
        except FileNotFoundError:
            return f"cp: no such file as {arguments[SOURCE]}"
        except IsADirectoryError:
            return f"cp: {arguments[SOURCE]} is a directory"
    else:
        return "Usage: cp [source] [destination]"


def mv(arguments: List[str]) -> Union[str, None]:
    """
    Move or rename a file or a directory.
    Usage: mv [source] [dest]
    """
    if len(arguments) == MV_CP_ARGUMENTS_NUMBER:
        try:
            shutil.move(arguments[SOURCE], arguments[DESTINATION])
        except FileNotFoundError:
            return f"mv: no such file or directory {arguments[SOURCE]}"
        except FileExistsError:
            return f"mv: can't move a directory ({arguments[SOURCE]}) to a file ({arguments[DESTINATION]})"
        except shutil.Error:
            return f"mv: destination {arguments[DESTINATION]} already exists"
    else:
        return "Usage: mv [source] [destination]"


def mkdir(arguments: List[str]) -> Union[str, None]:
    """
    Create new directory.
    Usage: mkdir [filename]...
    """
    exceptions = ""
    if len(arguments) <= 1:
        exceptions += "mkdir: missing directory operand"
    else:
        for directory in arguments[:HISTORY_LOCATION]:
            try:
                os.mkdir(directory)
            except FileExistsError:
                exceptions += f"mkdir: file or directory {directory} already exists\n"
            except NotADirectoryError:
                exceptions += f"mkdir: cannot create directory ‘{directory}’: Not a directory\n"
            except FileNotFoundError:
                exceptions += f"mkdir: cannot create directory ‘{directory}’: No such file or directory\n"
    return exceptions

def rmdir(arguments: List[str]) -> Union[str, None]:
    """
    Delete an empty directory.
    Usage: rmdir [directory]...
    """
    exceptions = ""
    if len(arguments) <= 1:
        exceptions += "rkdir: missing directory operand"
    else:
        for directory in arguments[:HISTORY_LOCATION]:
            try:
                os.rmdir(directory)
            except NotADirectoryError:
                exceptions += f"rmdir: failed to remove '{directory}': Not a directory\n"
            except FileNotFoundError:
                exceptions += f"rmdir: failed to remove '{directory}': No such file or directory\n"
            except OSError:
                exceptions += f"rmdir: failed to remove '{directory}': Directory not empty\n"

    return exceptions


def rm(arguments: List[str]) -> Union[str, None]:
    """
    Delete files.
    Usage: rm [file]...
    """
    exceptions = ""
    if len(arguments) <= 1:
        exceptions += "rm: missing file operand"
    else:
        for file in arguments[:HISTORY_LOCATION]:
            try:
                os.remove(file)
            except IsADirectoryError:
                exceptions += f"rm: cannot remove '{file}': Is a directory\n"
            except (FileNotFoundError, NotADirectoryError):
                exceptions += f"rm: cannot remove '{file}': No such file or directory\n"

    return exceptions