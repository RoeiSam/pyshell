"""
Purpose: Implementation of the commands in pyshell.
Author: Roei Samuel
Time: 01.07.25
"""
import getpass
import glob
import os
from typing import List, Union
from files_commands import touch, cat, cp, mv, mkdir, rmdir, rm

HISTORY_LOCATION = -1


def ls(arguments: List[str]) -> str:
    """
    Print all files and directories in current directory.
    """
    if len(arguments) == 1:
        return " ".join(glob.glob("*"))
    else:
        all_files = ""
        for file in arguments[:HISTORY_LOCATION]:
            if os.path.isfile(file):
                all_files += f"{file}\n"
            elif os.path.isdir(file):
                all_files += f"{file}:\n{" ".join(glob.glob(f"{file}/*"))}\n"
            else:
                all_files += f"{file}: No such file or directory\n"
        return all_files


def cd(arguments: List[str]) -> Union[str, None]:
    """
    Enter to directory dir.
    Usage: cd [directory]
    """
    try:
        os.chdir(arguments[0])
    except FileNotFoundError:
        return "Directory doesn't exists"
    except PermissionError:
        return "You dont have permission to enter this directory"
    except NotADirectoryError:
        return "This is not a directory"


def pwd(arguments: List[str]) -> str:
    """
    Print the current location path.
    """
    return os.getcwd()


def echo(arguments: List[str]) -> str:
    """
    Print all arguments.
    Usage: echo [argument] [argument]...
    """
    return " ".join(arguments[:HISTORY_LOCATION])


def logname(arguments: List[str]) -> str:
    """
    Print user´s login name
    """
    return getpass.getuser()


def man(arguments: List[str]) -> str:
    """
    Print explanation and usage of the command.
    Usage: man [command]
    """
    return eval(f"{arguments[0]}.__doc__")


def history(arguments: List[str]) -> str:
    """
    Print the history of your commands.
    """
    commands_history = ""
    for i in range(len(arguments[HISTORY_LOCATION])):
        commands_history += (f"{i + 1}\t{arguments[HISTORY_LOCATION][i]}\n")
    return commands_history