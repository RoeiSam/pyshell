"""
Purpose: Implementation of the commands in pyshell.
Author: Roei Samuel
Time: 01.07.25
"""
import getpass
import glob
import os
from typing import List


def ls() -> str:
    """
    Print all files and directories in current directory.
    """
    return glob.glob("*")


def cd(dir: str) -> None:
    """
    Enter to directory dir.
    Usage: cd [directory]
    """
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print("Directory doesn't exists")
    except PermissionError:
        print("You dont have permission to enter this directory")
    except NotADirectoryError:
        print("This is not a directory")


def pwd() -> str:
    """
    Print the current location path.
    """
    return os.getcwd()


def echo(arguments: List[str]) -> str:
    """
    Print all arguments.
    Usage: echo [argument] [argument]...
    """
    return " ".join(arguments)


def logname() -> str:
    """
    Print user´s login name
    """
    return getpass.getuser()


def man(command: str) -> str:
    """
    Print explenation and usage of the command.
    Usage: man [command]
    """
    return eval(f"{command}.__doc__")

