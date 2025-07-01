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
    if command[0].startswith("!"):
        if command[0][1] == "!":
            wanted_command = LAST_COMMAND
        elif command[0][1:].isdigit():
            wanted_command = int(command[0][1:]) - 1
        elif command[0][1] == "-" and command[0][2:].isdigit():
            wanted_command = -int(command[COMMAND_NAME][2:])
        # else:
        #     return command
        try:
            for i in range(len(commands_history[wanted_command].split())):
                command.insert(i + 1, commands_history[wanted_command].split()[i])
            del command[0]
            print(" ".join(command))
        except (IndexError, UnboundLocalError):
            pass
    return command


def pyshell() -> None:
    """
    The pyshell! Get a command from user and execute.
    :return: None
    """
    commands_history = []
    print("Welcome to the Python Shell!")
    while True:
        command = input(f"{logname([])}:{pwd([])} -> ")
        if command:
            command = convert_command(command, commands_history)
            commands_history.append(" ".join(command))
            command.append(commands_history)
            try:
                return_string = eval(f"{command[COMMAND_NAME]}({command[FIRST_ARGUMENT:]})")
                if return_string:
                    print(return_string)
            except (NameError, SyntaxError):
                print("No such command")

def main() -> None:
    pyshell()

if __name__ == "__main__":
    main()
