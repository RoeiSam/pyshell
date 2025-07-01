"""
Purpose: Implementation of shell
Author: Roei Samuel
Date: 01.07.25
"""
from pyshell_commands import ls, cd, pwd, echo, logname, man, history
from typing import List

COMMAND_NAME = 0
FIRST_ARGUMENT = 1
LAST_COMMAND = -1


def convert_command(command: str, commands_history: List[str]) -> str:
    """
    Convert input from user to command and arguments.
    :param command: The input from the user.
    :param commands_history: History of all commands so far.
    :return: The command seperated to command name and arguments.
    """
    command = command.split()
    if command[0] == "!!":
        del command[0]
        for i in range(len(commands_history[LAST_COMMAND].split())):
            command.insert(i, commands_history[LAST_COMMAND].split()[i])
        print(" ".join(command))
    elif command[0].startswith("!") and command[0][1].isdigit():
        for i in range(len(commands_history[int(command[0][1]) - 1].split())):
            command.insert(i + 1, commands_history[int(command[0][1]) - 1].split()[i])
        del command[0]
        print(" ".join(command))
    elif command[0].startswith("!-") and command[0][2].isdigit():
        for i in range(len(commands_history[-int(command[COMMAND_NAME][2])].split())):
            command.insert(i + 1, commands_history[-int(command[COMMAND_NAME][2])].split()[i])
        del command[0]
        print(" ".join(command))
    return command


def pyshell() -> None:
    """
    The pyshell! Get a command from user and execute.
    :return: None
    """
    commands_history = []
    print("Welcome to the Python Shell!")
    while True:
        command = input(f"{logname()}:{pwd()} -> ")

        if len(command) > 0:
            command = convert_command(command, commands_history)
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
