"""
Purpose: Implementation of shell
Author: Roei Samuel
Date: 01.07.25
"""
from pyshell_commands import ls, cd, pwd, echo, logname, man

COMMAND_NAME = 0
FIRST_ARGUMENT = 1


def pyshell():
    """
    The pyshell! Get a command from user and execute.
    :return: None
    """
    print("Welcome to the Python Shell!")
    while True:
        command = input("{0}:{1} -> ".format(logname([]), pwd([])))
        command = command.split()
        try:
            if command:
                return_string = eval("{0}({1})".format(command[COMMAND_NAME], command[FIRST_ARGUMENT:]))
                if return_string:
                    print(return_string)
        except NameError:
            print("No such command")


def main():
    pyshell()

if __name__ == "__main__":
    main()
