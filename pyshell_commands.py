"""
Purpose: Implementation of the commands in pyshell.
Author: Roei Samuel
Time: 01.07.25
"""
import glob
import os

def ls() -> str:
    """
    Return a list all files and directories in current directory.
    """
    all_files = glob.glob("*")
    return all_files

def cd(dir: str) -> None:
    """
    Enter to directory dir.
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
    Return the current location path.
    """
    return os.getcwd()
