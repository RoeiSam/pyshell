"""
Purpose: Implementation of shell
Author: Roei Samuel
Date: 01.07.25
"""
from pyshell_commands import ls, cd, pwd, echo, logname

COMMAND_NAME = 0
FIRST_ARGUMENT = 1

def pyshell() -> None:
    """
    The pyshell! Get a command from user and execute.
    :return: None
    """
    print("Welcome to the Python Shell!")
    while True:
        command = input(f"{logname([])}:{pwd([])} -> ")
        command = command.split()
        if command:
            return_string = eval(f"{command[COMMAND_NAME]}({command[FIRST_ARGUMENT:]})")
            if return_string:
                print(return_string)

def main() -> None:
    pyshell()

if __name__ == "__main__":
    main()
