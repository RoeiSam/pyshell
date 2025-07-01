"""
Purpose: Implementation of shell
Author: Roei Samuel
Time: 01.07.25
"""
from pyshell_commands import ls, cd, pwd, echo, logname, man, history

COMMAND_NAME = 0
FIRST_ARGUMENT = 1

def pyshell() -> None:
    """
    The pyshell! Get a command from user and execute.
    :return: None
    """
    commands_history = []
    print("Welcome to the Python Shell!")
    while True:
        command = input(f"{logname()}:{pwd()} -> ")
        command = command.split()
        if len(command) > 0:
            commands_history.append(" ".join(command))
            if command[COMMAND_NAME] == "ls":
                print(" ".join(ls()))
            elif command[COMMAND_NAME] == "cd":
                cd(command[FIRST_ARGUMENT])
            elif command[COMMAND_NAME] == "pwd":
                print(pwd())
            elif command[COMMAND_NAME] == "echo":
                print(echo(command[FIRST_ARGUMENT:]))
            elif command[COMMAND_NAME] == "man":
                print(man(command[FIRST_ARGUMENT]))
            elif command[COMMAND_NAME] == "history":
                print(history(commands_history))

def main() -> None:
    pyshell()

if __name__ == "__main__":
    main()
