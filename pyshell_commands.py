"""
Purpose: Implementation of the commands in pyshell.
Author: Roei Samuel
Time: 01.07.25
"""
import getpass
import os


def ls(arguments):
    """
    Return a list of all files and directories in current directory.
    """
    if len(arguments) == 0:
        return " ".join(os.listdir())

    all_files = ""
    for file in arguments:

        if os.path.isdir(file):
            files_in_dir = " ".join(os.listdir(file))
            all_files += "{0}:\n{1}\n".format(file, files_in_dir)
        elif os.path.exists(file):
            all_files += "{0}\n".format(file)
        else:
            all_files += "{0}: No such file or directory\n".format(file)
    return all_files


def cd(arguments):
    """
    Enter to directory dir.
    """
    if len(arguments) != 1:
        print("Usage: cd [directory]")
    else:
        try:
            os.chdir(arguments[0])
        except FileNotFoundError:
            print("Directory doesn't exists")
        except PermissionError:
            print("You dont have permission to enter this directory")
        except NotADirectoryError:
            print("This is not a directory")


def pwd(arguments):
    """
    Return the current location path.
    """
    return os.getcwd()


def echo(arguments):
    """
    Return all arguments as a string.
    """
    return " ".join(arguments)


def logname(arguments):
    """
    Return user´s login name
    """
    return getpass.getuser()

