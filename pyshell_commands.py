"""
Purpose: Implementation of the commands in pyshell.
Author: Roei Samuel
Time: 01.07.25
"""
import glob

def ls() -> str:
    """
    Return a list all files and directories in current directory.
    """
    all_files = glob.glob("*")
    return all_files
