"""
Purpose: Implementation of the commands in pyshell.
Author: Roei Samuel
Time: 01.07.25
"""
import getpass
import glob
import os
from typing import List


def ls(arguments: List[str]) -> str:
    """
    Return a list of all files and directories in current directory.
    """
    if len(arguments) == 0:
        return " ".join(glob.glob("*"))
    else:
        all_files = ""
        for file in arguments:
            if os.path.isfile(file):
                all_files += f"{file}\n"
            elif os.path.isdir(file):
                all_files += f"{file}:\n{" ".join(glob.glob(f"{file}/*"))}\n"
            else:
                all_files += f"{file}: No such file or directory\n"
        return all_files


def cd(arguments: List[str]) -> None:
    """
    Enter to directory dir.
    """
    if len(arguments) == 1:
        try:
            os.chdir(arguments[0])
        except FileNotFoundError:
            print("Directory doesn't exists")
        except PermissionError:
            print("You dont have permission to enter this directory")
        except NotADirectoryError:
            print("This is not a directory")
    else:
        print("Usage: cd [directory]")


def pwd(arguments: List[str]) -> str:
    """
    Return the current location path.
    """
    return os.getcwd()


def echo(arguments: List[str]) -> str:
    """
    Return all arguments as a string.
    """
    return " ".join(arguments)


def logname(arguments: List[str]) -> str:
    """
    Return user´s login name
    """
    return getpass.getuser()

