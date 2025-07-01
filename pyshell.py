"""
Purpose: Implementation of shell
Author: Roei Samuel
Time: 01.07.25
"""
from pyshell_commands import ls

COMMAND_NAME = 0

def pyshell() -> None:
    """
    The pyshell! Get a command from user and execute.
    :return: None
    """
    while True:
        command = input("-> ")
        command = command.split()

        if(command[COMMAND_NAME] == "ls"):
            print(" ".join(ls()))

def main() -> None:
    print("Welcome to the Python Shell!")
    pyshell()

if __name__ == "__main__":
    main()
