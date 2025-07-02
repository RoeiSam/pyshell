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
    if len(arguments) <= 1:
        return "touch: missing file operand"
    else:
        for file in arguments[:HISTORY_LOCATION]:
            try:
                Path.touch(file)
            except NotADirectoryError:
                return f"touch: cannot touch '{file}': No such file or directory"


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
            content += f"cat: {file}: Is a directory\n"
        except FileNotFoundError:
            content += f"cat: {file}: No such file or directory\n"
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
            return f"cp: No such file as {arguments[SOURCE]}"
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
            return f"mv: No such file or directory {arguments[SOURCE]}"
        except FileExistsError:
            return f"mv: Can't move a directory ({arguments[SOURCE]}) to a file ({arguments[DESTINATION]})"
        except shutil.Error:
            return f"mv: Destination {arguments[DESTINATION]} already exists"
    else:
        return "Usage: mv [source] [destination]"


def mkdir(arguments: List[str]) -> Union[str, None]:
    """
    Create new directory.
    Usage: mkdir [filename]...
    """
    if len(arguments) <= 1:
        return "mkdir: missing directory operand"
    else:
        for directory in arguments[:HISTORY_LOCATION]:
            try:
                os.mkdir(directory)
            except FileExistsError:
                return f"mkdir: File or directory {directory} already exists"
            except NotADirectoryError:
                return f"mkdir: Cannot create directory ‘{directory}’: Not a directory"
            except FileNotFoundError:
                return f"mkdir: Cannot create directory ‘{directory}’: No such file or directory"


def rmdir(arguments: List[str]) -> Union[str, None]:
    """
    Delete an empty directory.
    Usage: rmdir [directory]...
    """
    if len(arguments) <= 1:
        return "rkdir: missing directory operand"
    else:
        for directory in arguments[:HISTORY_LOCATION]:
            try:
                os.rmdir(directory)
            except NotADirectoryError:
                return f"rmdir: Failed to remove '{directory}': Not a directory"
            except FileNotFoundError:
                return f"rmdir: Failed to remove '{directory}': No such file or directory"
            except OSError:
                return f"rmdir: Failed to remove '{directory}': Directory not empty"